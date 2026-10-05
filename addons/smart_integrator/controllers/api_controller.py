from odoo import http
from odoo.http import request


class IoTIntegrationController(http.Controller):

    @http.route('/api/iot/consume', type='json', auth='none', methods=['POST'], csrf=False)
    def iot_consume_material(self, **kwargs):
        employee_id = kwargs.get('employee_id')
        product_id = kwargs.get('product_id')
        quantity = kwargs.get('quantity')

        if not all([employee_id, product_id, quantity]):
            return {'status': 'error', 'message': 'Missing parameters'}

        try:
            env = request.env(su=True)
            consumption = env['smart.consumption'].create({
                'employee_id': employee_id,
                'product_id': product_id,
                'quantity': quantity
            })
            consumption.action_process()

            return {
                'status': 'success',
                'consumption_id': consumption.id,
                'message': 'Stock deducted and rules evaluated'
            }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}