# -*- coding: utf-8 -*-

from odoo import models,fields


class SaleOrderWizard(models.TransientModel):
    """wizard for giving the message"""
    _name = "sale.order.wizard"
    _description = "validation Error"

    message = fields.Text(string="Message")
