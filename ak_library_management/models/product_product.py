# -*- coding: utf-8 -*-


from odoo import fields, models,api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    seller_ids = fields.One2many(comodel_name='product.supplierinfo',
                                 inverse_name='product_id',
                                 string='Vendors')
    variant_seller_ids = fields.One2many(comodel_name='product.supplierinfo',
                                         inverse_name='product_id')
