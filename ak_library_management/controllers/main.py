# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Library(http.Controller):
    @http.route('/contacts', type='http', auth='public', website=True)
    def library_details(self, **kwargs):
        contact_details = request.env['res.partner'].search([])
        values = {
            'contacts': contact_details,
        }
        return request.render('ak_library_management.website_contacts_page', values)

    @http.route('/contacts/<slug>', type='http', auth='public', website=True)
    def fetch_contacts_data(self, slug):
        data = request.env['res.partner'].search([('contacts_slug','=',slug)])
        values = {
            'data': data,
        }
        return request.render('ak_library_management.fetch_contacts_data_page', values)
