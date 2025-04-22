# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Product(Add to cart)',
    'version': '18.0.1.0.1',
    'author': 'Aastha Jain',
    'summary': 'A library management module is a software system designed to '
               'automate and streamline all aspects of a library',
    'sequence': 0,
    'category': 'Management/Management',
    'website': 'https://www.aktivsoftware.com',
    'depends': ["website", "website_sale", ""],
    'depends': [
        "sale_management",
        "purchase",
        "website",
        "website_sale",
        "stock",
    ],
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'product_add_to_cart/static/src/js/add_to_cart.js',
        ],
    },

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
