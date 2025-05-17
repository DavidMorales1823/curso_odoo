{
    'name': 'primer modulo',
    'version': '1.0',
    'summary': 'primer modulo',
    'author': 'david',
    'website': 'https://tuempresa.com',
    'category': 'Accounting',
    'license': 'LGPL-3',
    'depends': ['base', 'account','mail','hr'],
    'data': [
        'views/menu_view.xml',
        'views/libros_view.xml',
        'views/hr_employee_view.xml',
        'security/libreria_security.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'application': True,
    'auto_install': True,
}
