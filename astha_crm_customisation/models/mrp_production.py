# -*- coding: utf-8 -*-

from odoo import models, fields


class MrpProduction(models.Model):
    """Here, inherit the mrp.production model."""
    _inherit = 'mrp.production'

    job_name = fields.Char(string="Job Name")