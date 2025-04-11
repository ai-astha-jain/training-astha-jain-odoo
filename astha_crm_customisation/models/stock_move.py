# -*- coding: utf-8 -*-

from odoo import models, fields


class StockMove(models.Model):
    """inheriting stock.move to add a new field with more functionality."""
    _inherit = "stock.move"

    job_name = fields.Char(string="Job Name")

    def _get_new_picking_values(self):
        res = super()._get_new_picking_values()
        res["job_name"] = self.group_id.sale_id.job_name
        return res

    def _prepare_procurement_values(self):
        val = super()._prepare_procurement_values()
        val["sale"] = self.group_id.sale_id
        return val
