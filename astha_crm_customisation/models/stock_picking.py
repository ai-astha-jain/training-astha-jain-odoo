# -*- coding: utf-8 -*-

from odoo import models, fields


class Picking(models.Model):
    """inherit stock picking model to add a new field."""
    _inherit = "stock.picking"

    job_name = fields.Char(string="Job Name")