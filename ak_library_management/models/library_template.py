# -*- coding: utf-8 -*-

from odoo import models,fields,api


class Library(models.Model):
    """" This model gives the information about the library."""
    _name = 'library.library'
    _description = 'Library'

    name = fields.Char(string='Name', required=True)
    location = fields.Char(string='Location')
    capacity = fields.Integer(string='Capacity')
    notes = fields.Text(string='Notes')
    book_id = fields.Many2many(comodel_name='product.template',
                                string='Book Ids',
                                domain="[('is_library_book','=',1)]")

    count = fields.Integer(string='Count Borrowed Books', compute="count_borrowed_book")

    """function to count borrowed books"""
    @api.depends('book_id')
    def count_borrowed_book(self):
        for rec in self:
            borrowed_books = rec.filtered(lambda reg: reg.book_id.status == 'borrowed')
            self.count = len(borrowed_books)

    """function of smart button name borrowed"""
    def action_count_borrowed_books(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Borrowed Books List',
            'res_model': 'product.template',
            'view_mode': 'list',
            'domain': [('status', '=', 'borrowed'), ('id', 'in', self.book_id.ids)],
        }
