# -*- coding: utf-8 -*-

from odoo import models, fields

class LibraryBookCategory(models.Model):
    """Model name is library.book.category. Test many2one field on tag_ids.
    This model has data related to category of books."""
    _name = 'library.book.category'
    _description = 'Library Book Category'


    name = fields.Char(string='Book Category', required=True)
    tag_ids = fields.Many2many('library.book.tags',  string='Book Tag')
