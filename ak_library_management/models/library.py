# -*- coding: utf-8 -*-

from odoo import models,fields

class LibraryBook(models.Model):
    """" Model name of this model is library.library, It has fields that has information
    related to library name, location, capacity to store books, and book_ids.
    Test one2many field on book_ids and inverse name is library_id."""
    _name = 'library.library'
    _description = 'Library'


    name = fields.Char(string='Name', required=True)
    location = fields.Char(string='Location')
    capacity = fields.Integer(string='Capacity')
    notes = fields.Text(string='Notes')
    book_ids = fields.One2many('library.book', string='Book Ids', inverse_name='library_id')
