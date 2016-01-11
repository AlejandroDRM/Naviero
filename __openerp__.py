#################################################################
# MS2 Consulting Group                                          #
#################################################################
{
    'name': 'Global Shipping Naviero',
    'version': '1.0',
    'depends': [
        'base',
        'mail',
        'account_accountant',
        'sale',
        'account_anglo_saxon'
    ],
    'author': 'MS2 Consulting Group',
    'category': 'Naviero',
    'description': u"""Modulo Naviero""",
    'website': '',
    'data': [
        'security/naviero_security.xml',
        'security/ir.model.access.csv',
        'views/buque_view.xml',
        'views/viaje_view.xml',
        'views/bl_view.xml',
        'views/booking_view.xml',
        'views/contenedor_view.xml',
        'views/contenedor_tipo_view.xml',
        'views/contenedor_movimiento_view.xml',
        'views/puerto_view.xml',
        'views/patio_view.xml',
        'views/ruta_view.xml',
        'views/linea_view.xml',
        'views/beneficiario_view.xml',
        'views/servicio_view.xml',
        'workflows/equipo_workflow.xml',
        'views/contenedor_tipo_view.xml',
        'views/contenedor_movimiento_view.xml',
        'views/beneficiario_view.xml',
        'data/account_user_types.xml',
        'data/account_chart_template.xml',
        'data/account_tax_code.xml',
        'data/account_tax.xml',
        'data/bl_reports.xml',
        'data/reports_control_de_equipos.xml',
        #'data/products_data.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': True
}
