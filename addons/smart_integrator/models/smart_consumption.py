from odoo import models, fields, api, exceptions


class SmartConsumption(models.Model):
    _name = 'smart.consumption'
    _description = 'IoT Material Consumption'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity Consumed', required=True)
    total_cost = fields.Float(string='Cost', compute='_compute_total_cost', store=True)
    state = fields.Selection([('draft', 'Draft'), ('processed', 'Processed')], default='draft')

    @api.depends('product_id', 'quantity')
    def _compute_total_cost(self):
        for rec in self:
            rec.total_cost = rec.product_id.standard_price * rec.quantity

    @api.constrains('quantity', 'employee_id')
    def _check_budget(self):
        for rec in self:
            if rec.employee_id.consumed_total > rec.employee_id.department_budget:
                raise exceptions.ValidationError("Budget Exceeded for this employee's department.")

    def action_process(self):
        for rec in self:
            if rec.state == 'processed':
                continue

            stock_location = self.env.ref('stock.stock_location_stock')
            customer_location = self.env.ref('stock.stock_location_customers')

            self.env['stock.move'].create({
                'name': f'Consumption {rec.id}',
                'product_id': rec.product_id.id,
                'product_uom_qty': rec.quantity,
                'product_uom': rec.product_id.uom_id.id,
                'location_id': stock_location.id,
                'location_dest_id': customer_location.id,
            })._action_confirm()

            rec.state = 'processed'
            rec._check_and_trigger_rfq()

    def _check_and_trigger_rfq(self):
        min_qty = 10.0
        current_qty = self.product_id.qty_available

        if current_qty < min_qty:
            supplierinfo = self.env['product.supplierinfo'].search(
                [('product_tmpl_id', '=', self.product_id.product_tmpl_id.id)], limit=1)
            partner_id = supplierinfo.partner_id.id if supplierinfo else self.env.ref('base.res_partner_1').id

            self.env['purchase.order'].create({
                'partner_id': partner_id,
                'order_line': [(0, 0, {
                    'product_id': self.product_id.id,
                    'product_qty': min_qty * 2,
                    'price_unit': self.product_id.standard_price,
                })]
            })
            