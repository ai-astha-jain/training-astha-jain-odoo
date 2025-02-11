# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Library Management',
    'version': '18.0.1.0.0',
    'author':'Aastha Jain',
    'summary': 'A library management module is a software system designed to '
               'automate and streamline all aspects of a library'
               ' operations, including book cataloging, member management, '
               'book issuing and returning, overdue fine calculations, '
               'and generating reports, allowing librarians to '
               'efficiently track and manage library resources with '
               'accurate data access, minimizing manual record-keeping and '
               'improving overall user experience',
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

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
