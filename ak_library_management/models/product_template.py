# -*- coding: utf-8 -*-

from odoo import models, fields


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