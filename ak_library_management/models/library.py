# -*- coding: utf-8 -*-

from odoo import models,fields


class Library(models.Model):
    """" This model gives the information about the library."""
    _name = 'library.library'
    _description = 'Library'

    name = fields.Char(string='Name', required=True)
    location = fields.Char(string='Location')
    capacity = fields.Integer(string='Capacity')
    notes = fields.Text(string='Notes')
    book_ids = fields.One2many('library.book', string='Book Ids', inverse_name='library_id')
