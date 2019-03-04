# -*- coding: utf-8 -*-
{
    'name': "Bibliteca",

    'summary': """
       Modulo de una bilioteca de libros.""",

    'description': """
		moodulo para la gestion de una biblioteca
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
		'views/templates.xml',
    'views/libros.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
