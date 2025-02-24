# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Library Management',
    'version': '18.0.1.0.0',
    'author':'Aastha Jain',
    'summary': 'A library management module is a software system designed to '
               'automate and streamline all aspects of a library',
    'sequence': 0,
    'category': 'Management/Management',
    'website': 'https://www.aktivsoftware.com',
    'depends': ['base','product','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_template_views.xml',
        'views/book_tag_views.xml',
        'views/book_category_views.xml',
        'views/library_member_views.xml',
        'views/product_views.xml',
        'views/sale_menus.xml',
        'views/product_view_inherit_barcode_move_views.xml',
        'views/bulk_books_views.xml',
        'data/sequence.xml',
        'views/res_users.xml',
        'views/sale_order_views.xml',
        'views/res_partner_views.xml',
        'views/borrow_transaction_views.xml',
        'views/sale_order_wizard.xml',

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
