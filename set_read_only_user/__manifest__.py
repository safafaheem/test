{
    'name': 'Read Only User',
    'description': 'Set Raed Only User',
    'version': '15.0.1.0.0',
    'license': 'LGPL-3',

    'depends': ['base'],

    'data': {
        'security/ir.model.access.csv',
        'security/user_group.xml',
        'views/res_users.xml',

    }
}
