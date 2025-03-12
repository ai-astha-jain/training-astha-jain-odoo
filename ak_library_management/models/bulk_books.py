# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class UploadBulkBooks(models.TransientModel):
    """transient model for uploading multiple books at once."""
    _name = "bulk.books"
    _description = "Upload Bulk Books"

    book_name = fields.Text(string="Book Name", required=True, default="")
    author_id = fields.Many2one('res.partner', string="Author", required=True)
    price = fields.Integer(string='Price')
    capacity = fields.Integer(string='Capacity')
    product_count = fields.Integer(string="Count", compute="_count_product_books")
    state = fields.Boolean(string="state")

    def action_bulk_books(self):
        """create a new books record as a product at the same time.
        param: None
        return: True"""
        books = self.book_name.split(",")
        vals_list = []
        for book in books:
            exist_book = self.env['product.template'].search(domain=[('name', '=', book)])
            if exist_book:
                continue
            vals_list.append({'name': book, 'author': self.author_id.name})
            self.env['bus.bus']._sendone(self.env.user.partner_id, 'simple_notification', {
                'type': 'success',
                'sticky': True,
                'message': _(f"{book} have been created."),
            })
        self.env['product.template'].create(vals_list)

        self.state = True

    def revert_changes(self):
        """delete all the books now as product.
        param: None
        return: True"""
        books = self.book_name.split(",")
        for book in books:
            exist_book = (self.env['product.template']
                          .search(domain=[('name', '=', book)]))
            exist_book.unlink()
        self.state = False

    @api.depends('state', 'product_count')
    def _count_product_books(self):
        """count the number of borrowed book.
        param: None
        return: integer"""
        books = self.book_name.split(",")
        if self.state:
            self.product_count = len(books)
        else:
            self.product_count = 0

    def action_product_count(self):
        """opens the form if only 1 book will be borrowed
        else open the list.
        param: None
        return: True"""
        if self.product_count == 1:
            search_product = (self.env['product.template']
                              .search(domain=[('name', '=', self.book_name)]))
            print(search_product)
            return {
                'type': 'ir.actions.act_window',
                'name': 'Product Count',
                'res_model': 'product.template',
                'view_mode': 'form',
                'res_id': search_product.id,
            }
        else:
            books = self.book_name.split(",")
            print(books)
            return {
                'type': 'ir.actions.act_window',
                'name': 'Product Count',
                'res_model': 'product.template',
                'view_mode': 'list,form',
                'domain': [('name', 'in', books)],
            }
