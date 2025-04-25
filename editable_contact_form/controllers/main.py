# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Library(http.Controller):
    @http.route('/contacts', type='http', auth='public', website=True)
    def library_details(self, **kwargs):
        contact_details = request.env['res.partner'].sudo().search([])
        values = {
            'contacts': contact_details,
        }
        return request.render('editable_contact_form.website_contacts_page', values)

    @http.route('/contacts/<slug>', type='http', auth='public', website=True)
    def fetch_contacts_data(self, **args):
        data = request.env['res.partner'].sudo().search([('contacts_slug', '=', args['slug'])])
        values = {
            'data': data,
        }
        return request.render('editable_contact_form.fetch_contacts_data_page', values)

    @http.route('/contacts/save', type='json',methods=['POST'], csrf=True, auth='public', website=True)
    def save_customer_details(self, **args):
        print("args---",args)
        save_contact = request.env['res.partner'].sudo().search([('id', '=', args.get('id'))])
        print("save contactssss----",save_contact)
        save_contact.write(args)
