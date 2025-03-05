# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models,fields


class BorrowTransaction(models.Model):
    _name = "borrow.book.warnings.wizard"
    _description = "Warnings"

    message = fields.Text(string="Message")