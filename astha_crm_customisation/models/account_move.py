# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountMove(models.Model):
    """Inherit account.move model to add a new field."""
    _inherit = "account.move"

    job_name = fields.Char(string="Job Name")