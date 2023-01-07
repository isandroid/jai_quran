# -*- coding: utf-8 -*-
{
    'name': "Alquran JAI",

    'summary': """Aplikasi Web Alquran JAI""",

    'description': """
        Aplikasi Web Alquran JAI
    """,

    'author': "Isa Mujahid Islam",
    'website': "https://isa.web.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/surat.xml',
        'views/ayat.xml',
        'views/tafsir.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
