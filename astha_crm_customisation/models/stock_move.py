# -*- coding: utf-8 -*-

from odoo import models, fields


class StockMove(models.Model):
    """inheriting stock.move to add a new field with more functionality."""
    _inherit = "stock.move"

    job_name = fields.Char(string="Job Name")

    def _get_new_picking_values(self):
        """Override: Get New Picking Values
        :param None
        :rtype: return the job name value in the deliveries
        """
        res = super()._get_new_picking_values()
        res["job_name"] = self.group_id.sale_id.job_name
        return res

    def _prepare_procurement_values(self):
        """Override: Prepare procurement Values
        :param None
        :rtype: return the dict value.
        """
        val = super()._prepare_procurement_values()
        val["sale"] = self.group_id.sale_id
        return val
