# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UploadBulkBooks(models.TransientModel):
    _name = "bulk.books"
    _description = "Upload Bulk Books"

    book_name = fields.Text(string="Book Name", required=True, default="")
    author_id = fields.Many2one('res.partner', string="Author", required=True)
    price = fields.Integer(string='Price')
    capacity = fields.Integer(string='Capacity')
    product_count = fields.Integer(string="Count", compute="_count_product_books")
    state= fields.Boolean(string="state")

    def create_product(self):
        books = self.book_name.split(",")
        vals_list = []
        for book in books:
            exist_book = self.env['product.template'].search(domain=[('name','=',book)])
            if exist_book:
                continue
            vals_list.append({'name': book, 'author':self.author_id.name})
        self.env['product.template'].create(vals_list)
        self.state = True

    def revert_changes(self):
        books = self.book_name.split(",")
        for book in books:
            exist_book = self.env['product.template'].search(domain=[('name', '=', book)])
            exist_book.unlink()
        self.state = False

    @api.depends('state','product_count')
    def _count_product_books(self):
        books = self.book_name.split(",")
        if self.state:
            self.product_count = len(books)
        else:
            self.product_count = 0

    def action_product_count(self):
        if self.product_count == 1:
            print("\n\n\n\n\nhello from if start\n\n\n")
            search_product = self.env['product.template'].search(domain=[('name','=',self.book_name)])
            print(search_product)
            print("\n\n\n\n\nhello from if start search product\n\n\n")
            return {
                'type': 'ir.actions.act_window',
                'name': 'Product Count',
                'res_model': 'product.template',
                'view_mode': 'form',
                'res_id': search_product.id,
            }
            print("\n\n\nHello from if end\n\n\n")
        else:
            print("\n\nHello from else start\n\n\n\n")
            books = self.book_name.split(",")
            print(books)
            print("\n\nBook split\n\n\n\n")
            return {
                'type': 'ir.actions.act_window',
                'name': 'Product Count',
                'res_model': 'product.template',
                'view_mode': 'list,form',
                'domain': [('name','in',books)],
            }
            print("\n\n\n\nHello from End\n\n\n")
