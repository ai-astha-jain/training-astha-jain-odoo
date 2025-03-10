# -*- coding: utf-8 -*-

from odoo import models, fields


class Warehouse(models.Model):
    """Inherits stock.warehouse"""
    _inherit = 'stock.warehouse'

    library_assistant = fields.Many2one(string="Library Assistant")
    library_worker = fields.Many2many(string="Library Worker")

    _sql_constraints = [
        ('name_uniq', 'UNIQUE (library_assistant)', 'Assistant name must be unique')
    ]

    _sql_constraints = [
        ('name_uniq', 'UNIQUE (library_worker)', 'Worker name must be unique')
    ]
