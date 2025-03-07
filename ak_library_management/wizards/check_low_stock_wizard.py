# -*- coding: utf-8 -*-

from odoo import models,fields


class CheckLowStockWizard(models.TransientModel):
    """wizard for giving the message"""
    _name = "check.low.stock.wizard"
    _description = "validation Error"

    message = fields.Text(string="Message")
