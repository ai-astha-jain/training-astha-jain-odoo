# -*- coding: utf-8 -*-

from odoo import models,fields

class LibraryBook(models.Model):
    """Model name is library.book, It contains data about book.
    Many2one firld has been tested on category_id and tag_ids and tag_id
    is related to category id. State field has selection with widget of
    borrowed and available. library_id has Many2one field with comodel library.library"""
    _name = 'library.book'
    _description = 'Library Book'


    name = fields.Char(string='Book Name', required=True)
    author = fields.Char(string='Author Name')
    ISBN = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Date of Publication')
    category_id = fields.Many2one('library.book.category' ,string='Book Category')
    tag_ids = fields.Many2many('library.book.tags',string='Tags', related='category_id.tag_ids')
    state = fields.Selection(
        string='Book Availability',
        selection=[('available', 'borrowed'),('borrowed','available')])
    description = fields.Text(string='Book Summary')
    library_id = fields.Many2one('library.library', string='Library Id')
