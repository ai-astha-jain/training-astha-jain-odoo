{
    'name': 'Library Management',
    'version': '18.0.1.0.0',
    'author':'Aastha Jain',
    'summary': 'A solution to a problem - Library',
    'sequence': 0,
    'category': 'Management/Management',
    'website': 'https://www.aktivsoftware.com',
    'depends': ['product','base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_view.xml',
        'views/library.xml',
        'views/library_book_tag.xml',
        'views/library_book_category.xml',
        'views/library_member_view.xml',
        'views/product_view.xml',
        'views/sale_menus.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
