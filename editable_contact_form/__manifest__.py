# -*- coding: utf-8 -*-

{
    'name': 'Contact Editable Form',
    'version': '18.0.1.0.0',
    'author': 'Aastha Jain',
    'summary': 'Contact Editable Form',
    'sequence': 0,
    'category': 'Website/Website',
    'website': 'https://www.aktivsoftware.com',
    'depends': [
        "website",
        "contacts",
    ],
    'data': [
        'views/website_menu.xml',
        'views/website_contacts_page.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'editable_contact_form/static/src/js/web_contact_controller.js',
            'editable_contact_form/static/src/js/website_contact_form_events.js',
        ],
    },

    'installable': True,
    'application': True,
}
