# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    """Here, inherit the sale.order model to
    add more functionality."""
    _inherit = 'sale.order'

    job_name = fields.Char(string="Job Name", compute="_compute_set_field", store=True)

    @api.depends('opportunity_id')
    def _compute_set_field(self):
        """Define: Compute Set Field
        :param None
        """
        for rec in self:
            if rec.opportunity_id:
                rec.job_name = rec.opportunity_id.name

    def _prepare_invoice(self):
        """Override: Prepare Invoice
        :param None
        :rtype: return the job name value
        """
        res = super()._prepare_invoice()
        res["job_name"] = self.job_name
        return res
