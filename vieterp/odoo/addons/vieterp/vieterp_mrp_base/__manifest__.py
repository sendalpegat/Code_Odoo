# -*- coding: utf-8 -*-
{
    'name': "vieterp_mrp_base",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "VietERP / Sang",
    'website': "http://www.vieterp.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'VietERP',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale',
        'mrp',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/mrp_bom_views.xml',
        'views/sale_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}