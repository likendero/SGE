# -*- coding: utf-8 -*-
{
    'name': "Productos",

    'summary': """
       Modulo de productos.""",

    'description': """
       Este es un modulo para odoo 10 de introducción de productos
    """,

    'author': "Pinky S.A",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/futbolistas.xml',
        'views/templates.xml',
        'views/productos.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}