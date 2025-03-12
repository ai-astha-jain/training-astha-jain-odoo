# -*- coding: utf-8 -*-

from odoo import models,fields


class Warehouse(models.Model):
    """Inherit stock.warehouse"""
    _inherit = "stock.warehouse"

    library_assistant = fields.Many2one(comodel_name='hr.employee', string="Library Assistant")
    worker = fields.Many2many(comodel_name='hr.employee', string="Library Worker")

    _sql_constraints = [
        ('name_uniq', 'unique (library_assistant)', "Assistant name already exists!"),
    ]

    _sql_constraints = [
        ('name_uniq', 'unique (worker)', "Worker name already exists!"),
    ]
