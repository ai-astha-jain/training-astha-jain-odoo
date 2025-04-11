# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'astha crm customisation',
    'version': '18.0.1.1.0',
    'author': 'Aastha Jain',
    'summary': 'A library management module is a software system designed to '
               'automate and streamline all aspects of a library',
    'sequence': 0,
    'category': 'Management/Management',
    'website': 'https://www.aktivsoftware.com',
    'depends': ["sale_management", "crm", "stock", "mrp", "project", "sale_project"],
    'data': [
        'views/sale_order_views.xml',
        'views/mrp_production_views.xml',
        'views/stock_picking_views.xml',
        'views/project_project_views.xml',
        'views/account_move_views.xml',
        'views/stock_move_views.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
