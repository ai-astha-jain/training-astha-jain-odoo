# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Product Catalog',
    'version': '18.0.1.4.8',
    'author': 'Aastha Jain',
    'summary': 'Product catalog',
    'sequence': 0,
    'category': 'Management/Management',
    'website': 'https://www.aktivsoftware.com',
    'depends': [
        "sale_management",
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/ir_action_report.xml',
        'report/product_catalog_pdf_report.xml',
        'views/product_catalog_views.xml',

    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
