{
    'name': 'Library Management',
    'version': '18.0.1.2.7',
    'author': 'Aastha Jain',
    'summary': 'A library management module is a software system designed to '
               'automate and streamline all aspects of a library',
    'sequence': 0,
    'category': 'Management/Management',
    'website': 'https://www.aktivsoftware.com',
    'depends': ['base', 'base_automation', 'product', 'sale', 'stock', 'website'],
    'data': [
        'security/library_management_security.xml',
        'security/ir.model.access.csv',
        'data/ir_cron_action.xml',
        'data/mail_template_data.xml',
        'data/sequence.xml',
        'wizards/check_low_stock_views.xml',
        'wizards/borrow_book_warnings_wizard.xml',
        'views/library_book_views.xml',
        'views/library_template_views.xml',
        'views/book_tag_views.xml',
        'views/book_category_views.xml',
        'views/library_member_views.xml',
        'views/product_views.xml',
        'views/sale_menus.xml',
        'views/product_view_inherit_barcode_move_views.xml',
        'views/bulk_books_views.xml',
        'views/res_users.xml',
        'views/sale_order_views.xml',
        'views/res_partner_views.xml',
        'views/borrow_transaction_views.xml',
        'views/stock_warehouse_views.xml',
        'views/res_config_settings_views.xml',
        'views/website_contacts_page.xml',
        'views/website_contacts_menu.xml',
        'report/ir_action_report.xml',
        'report/ir_action_report_templates_library.xml',
        'report/custom_report_invoicing.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'ak_library_management/static/src/*.js',
        ]
    },

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
