# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    """Here, inherit the sale.order model to
    add more functionality."""
    _inherit = 'sale.order'

    job_name = fields.Char(string="Job Name", readonly=False)

    @api.onchange('opportunity_id')
    def set_field(self):
        if self.opportunity_id:
            self.job_name = self.opportunity_id.name

    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        res["job_name"] = self.job_name
        return res
