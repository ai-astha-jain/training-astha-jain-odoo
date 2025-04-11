# -*- coding: utf-8 -*-

from odoo import models


class StockRule(models.Model):
    """inherit stock.rule to add new field and value in mrp production
    by calling a function _prepare_mo_vals"""
    _inherit = 'stock.rule'

    def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom):
        val = super()._prepare_mo_vals(product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom)
        val['job_name'] = values.get("sale").job_name
        return val
