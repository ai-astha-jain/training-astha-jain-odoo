# -*- coding: utf-8 -*-


from odoo import fields, models,api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    seller_ids = fields.One2many(comodel_name='product.supplierinfo',
                                 inverse_name='product_id',
                                 string='Vendors')
    variant_seller_ids = fields.One2many(comodel_name='product.supplierinfo',
                                         inverse_name='product_id',
                                         compute="_compute_variant_seller_ids",
                                         # inverse="_inverse_variant_seller_ids",
                                         store=True)

    @api.depends('product_tmpl_id.vendors_on_variants')
    def _compute_variant_seller_ids(self):
        for product in self:
            template = product.product_tmpl_id
            if template.vendors_on_variants:
                product.variant_seller_ids = self.env['product.supplierinfo'].browse()
            else:
                product.variant_seller_ids = product.product_tmpl_id.variant_seller_ids

    # def _inverse_variant_seller_ids(self):
    #     for product in self:
    #         if product.product_tmpl_id.vendors_on_variants:
    #             product.product_tmpl_id.variant_seller_ids = False
    #             product.seller_ids.write({'product_id': product.id,
    #                                       'product_tmpl_id': product.product_tmpl_id.id})
    #         else:
    #             product.product_tmpl_id.variant_seller_ids = product.variant_seller_ids
