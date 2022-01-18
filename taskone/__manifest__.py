{
    'name': 'Task 1',
    'version': '1.0',
    'summary': 'Task One software',
    'sequence': 10,
    'description': """my first task 1 from Engineer Ahmed Hefni""",
    'license': 'LGPL-3',
    'category': 'Task',
    'website': 'https://www.mywebsite.com/',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',

        'data/email_template.xml',

        'wizard/rejection_reason_view.xml',

        'views/purchase_request_view.xml',
        'views/purchase_request_line_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
