# -*- coding: utf-8 -*-

from odoo import models


class StockRule(models.Model):
    """inherit stock.rule to add new field and value in mrp production
    by calling a function _prepare_mo_vals"""
    _inherit = 'stock.rule'

    def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values,
                         bom):
        """Override : Prepare Mo Vals
        :param product_id: This is used to pass the prepared product values to the mo.
        :param product_qty: This is used to pass the prepared product quantity to the mo.
        :param product_uom: This is used to pass the unit of measure values to the mo.
        :param location_id: This is used to pass the location values.
        :param name: This is used to pass the reference.
        :param origin: This is used to pass source document.
        :param company_id: This is used to pass the company id values to the mo.
        :param values: This is used to pass the values.
        :param bom: this is used to pass the bill of material id.
        rtype: return the value of job_name in mo.
        """
        val = super()._prepare_mo_vals(product_id, product_qty, product_uom, location_id, name, origin, company_id,
                                       values, bom)
        val['job_name'] = values.get("sale").job_name
        return val
