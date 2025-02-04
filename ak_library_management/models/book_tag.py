# -*- coding: utf-8 -*-

from odoo import models,fields

class LibraryBookTags(models.Model):
    """Model name is library.book.tags, This file contains Book tags."""
    _name = 'library.book.tags'
    _description = 'Library Book Tags'


    name = fields.Char(string='Book Tags', required=True)
