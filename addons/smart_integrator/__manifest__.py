{
    'name': 'Smart Inventory & Procurement Integrator',
    'version': '1.0',
    'summary': 'IoT Integration for Inventory and Automated Procurement',
    'depends': ['base', 'stock', 'purchase', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/consumption_views.xml',
    ],
    'installable': True,
    'application': True,
}