# -*- coding: utf-8 -*-
{
    'name': "product_multi_select_sale",

    'summary': """
        product_multi_select_sale
    """,

    'description': """
        product_multi_select_sale
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
        'sale',
        'product',
        'stock',
        'sale_stock',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/add_multi_product.xml',
    ],
}