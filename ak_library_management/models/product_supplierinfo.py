# -*- coding: utf-8 -*-


from odoo import fields, models


class SupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'

    def write(self,vals):
        for variants in self:
            product_template = variants.product_tmpl_id
            print(product_template)
            if product_template.vendors_on_variants is False and 'product_id' in vals:
                vals['product_tmpl_id'].unlink()
            elif product_template.vendors_on_variants is True:
                vals['product_tmpl_id'] = product_template.id
        return super().write(vals)
