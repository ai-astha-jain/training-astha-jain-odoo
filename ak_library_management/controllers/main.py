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
    def fetch_contacts_data(self, **args):
        data = request.env['res.partner'].search([('contacts_slug','=',args['slug'])])
        values = {
            'data': data,
        }
        return request.render('ak_library_management.fetch_contacts_data_page', values)

    @http.route('/customers', type='http', auth='public', website=True, csrf=False)
    def fetch_customer_details(self, **args):
        return request.render('ak_library_management.customers_form_page')

    @http.route(['/customers/email'],type='json', auth='public', website=True,csrf=False)
    def customer_data(self,**args):
        customer = request.env['res.partner'].search([('email', '=', args.get('email'))])
        return {
            'name': customer.name,
            'website':customer.website,
            'phone': customer.phone,
        }
