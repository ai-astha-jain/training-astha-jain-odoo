# -*- coding: utf-8 -*-

from odoo import fields, models


class LibraryBookCategory(models.Model):
    """This class represents the category of the books available in the library."""
    _name = 'library.book.category'
    _description = 'Library Book Category'

    name = fields.Char(string='Book Category', required=True)
    tag_ids = fields.Many2many(comodel_name='library.book.tags', string='Book Tags')
