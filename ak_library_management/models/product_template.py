# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.addons.base.models.ir_actions_report import available
from odoo.http import borrow_request


class ProductTemplate(models.Model):
    """Here, inherit the product.template model to extend the ProductTemplate by library books information"""
    _inherit = 'product.template'

    is_library_book = fields.Boolean(string='Is Library Book' )
    author = fields.Char(string='Author')
    publisher = fields.Char(string='Publisher')
    edition = fields.Char(string='Edition')
    publish_date = fields.Date(string='Publish Date')
    pages = fields.Integer(string='Pages')
    available = fields.Boolean(string='Available')
    barcode = fields.Char(string='ISBN')
    status = fields.Selection([('available','Available'),('borrowed','Borrowed'),('reserved','Reserved')], string='Status')

    def mark_as_available(self):
        self.status = 'available'
        return self.status

    def mark_as_borrowed(self):
        self.status = 'borrowed'
        return self.status
