# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Library(models.Model):
    """" This model gives the information about the library."""
    _name = 'library.library'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Library'

    name = fields.Char(string='Name', required=True)
    location = fields.Char(string='Location')
    capacity = fields.Integer(string='Capacity')
    notes = fields.Text(string='Notes')
    book_ids = fields.Many2many(comodel_name='product.template',
                                string='Book Ids',
                                domain="[('is_library_book','=',1)]")

    count = fields.Integer(string='Count Borrowed Books',
                           compute="count_borrowed_book")

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
         'library cannot be with the same name.'),
    ]

    @api.depends('book_ids')
    def count_borrowed_book(self):
        """count all the books borrowed by the customer.
        param: None
        return : True"""
        for rec in self:
            borrowed_books = rec.filtered(lambda reg: reg.book_ids.status == 'borrowed')
            self.count = len(borrowed_books)

    def action_count_borrowed_books(self):
        """open the list of the borrowed books
        param: None
        return: True"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Borrowed Books List',
            'res_model': 'product.template',
            'view_mode': 'list',
            'domain': [('status', '=', 'borrowed'),
                       ('id', 'in', self.book_ids.ids)],
        }
