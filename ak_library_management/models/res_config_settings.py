# -*- coding: utf-8 -*-

from odoo import models, fields, _


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    borrowing_limits = fields.Integer(string="Borrowing Limits", config_parameter="ak_library_management.borrowing_limits")