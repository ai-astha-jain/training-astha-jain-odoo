# -*- coding: utf-8 -*-

from odoo import models,fields


class LibraryBook(models.Model):
    """This model has all the information about the books in the library."""
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Book Name', required=True)
    author = fields.Char(string='Author Name')
    ISBN = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Date of Publication')
    category_id = fields.Many2one(comodel_name='library.book.category',
                                  string='Book Category')
    tag_ids = fields.Many2many(comodel_name='library.book.tags',
                               string='Tags',
                               related='category_id.tag_ids')
    state = fields.Selection(
        string='Book Availability',
        selection=[('available', 'Available'),
                   ('borrowed','Borrowed'),
                   ('unavailable','Unavailable')])
    description = fields.Text(string='Book Summary')
    library_id = fields.Many2one(comodel_name='library.library',
                                 string='Library Id')
