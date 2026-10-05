from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    department_budget = fields.Float(string="Department Material Budget", default=1000.0)
    consumed_total = fields.Float(string="Total Consumed", compute="_compute_consumed_total")

    def _compute_consumed_total(self):
        for rec in self:
            consumptions = self.env['smart.consumption'].search([('employee_id', '=', rec.id)])
            rec.consumed_total = sum(consumptions.mapped('total_cost'))
            