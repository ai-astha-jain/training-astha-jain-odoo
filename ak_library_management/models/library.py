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
    book_ids = fields.Many2many(comodel_name='product.template',
                                string='Book Ids',
                                domain="[('is_library_book','=',1)]")
