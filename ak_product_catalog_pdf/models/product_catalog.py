# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductCatalog(models.Model):
    """A model which will open on the click of menuitem in Sales/Reporting
    name Product catalog genrator as a wizard."""
    _name = 'product.catalog'
    _description = 'Product Catalog'

    page_style = fields.Selection([('style1', 'Style1'),
                               ('style2', 'Style2')],string="Page Style")
    page_break = fields.Integer(string="Page Break")
    product_ids = fields.Many2many(comodel_name="product.product", string="Product")
