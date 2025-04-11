# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta
from re import search

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BorrowTransaction(models.Model):
    """Show the borrow transaction of books by the customer."""
    _name = "borrow.transaction.history"
    _description = "Borrow Transaction History"
    _rec_name = 'customer_id'

    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer', required=True)
    books_ids = fields.Many2many(comodel_name='product.template',
                                 string='Books')
    borrow_start_date = fields.Date(string='Start Date', default=datetime.today())
    borrow_end_date = fields.Date(string='End Date', required=True)
    deposit_amount = fields.Float(string='Deposit Amount')
    is_member = fields.Boolean(related="customer_id.is_member")
    is_active_transactions = fields.Boolean(string='Is Active Transactions',
                                            store=True,
                                            compute="_compute_active_transaction")
    check_borrow_limit = fields.Boolean(string='Borrow Limit',
                                        store=True,
                                        compute="_compute_borrow_books_limit")

    @api.depends('borrow_end_date')
    def _compute_active_transaction(self):
        for record in self:
            record.is_active_transactions = record.borrow_end_date >= date.today()

    @api.depends('books_ids')
    def _compute_borrow_books_limit(self):
        for record in self:
            record.check_borrow_limit = False
            search_record = self.search([('customer_id', '=', self.customer_id.id)])
            no_of_books = [books for rec in search_record for books in rec.books_ids]
            borrow_limit = int(record.env['ir.config_parameter'].get_param('ak_library_management.borrowing_limits'))
            if len(no_of_books) > borrow_limit:
                record.check_borrow_limit = True

    @api.constrains('borrow_start_date', 'borrow_end_date')
    def _check_date(self):
        """checks if end date is greater than start date
        param: None
        return: Exception"""
        for record in self:
            if record.borrow_start_date > record.borrow_end_date:
                raise ValidationError("End date should be greater tha start date.")

    def _get_warning(self, name, message):
        """ dynamic wizard to show the warnings.
        param: name, message
        return: warning"""
        return {
            'type': 'ir.actions.act_window',
            'name': name,
            'res_model': 'borrow.book.warnings.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_message': message}
        }

    def action_confirm(self):
        """checks the condition on customers not trust worthy, low stock product
        and according to len of books.
        param:None
        return:True"""
        if self.customer_id.not_trust_worthy:
            return self._get_warning('Not Trust Worthy',
                                     'Customer is not trustworthy. Are you sure you '
                                     'want to continue?')

        low_stock_product = [rec.name for rec in self.books_ids if rec.qty_available == 0]
        if low_stock_product:
            return self._get_warning('Low Stock Product',
                                     f"The following books are out of stock: {low_stock_product}."
                                     " Are you sure you want to continue?")

        if len(self.books_ids) >= 5:
            # Case A: Open Borrow Transactions Exist
            active_borrow_customer = self.search([('customer_id', '=', self.customer_id.id)])
            books_name = []
            search_book = [books_name.append(book.name) for record in active_borrow_customer[:-1]
                           for book in record.books_ids if book.name not in books_name]
            if books_name:
                return self._get_warning('Again Borrow Books',
                                         f"Customer already has {len(active_borrow_customer) - 1} open borrow "
                                         f"transactions with {books_name} books."
                                         f" Are you sure you want to borrow more books?")
            # Case B: No Open Borrow Transactions:
            else:
                return self._get_warning('Borrow Books',
                                         'Are you sure you want to allow borrowing'
                                         ' more than 5 books for this customer?')

    def book_reminder(self):
        """Book reminder before 2 days of end date. Send email to
        the customer.
        param:None
        return: True"""
        send_email_date = date.today() + timedelta(days=2)
        borrow_book_history = self.search([('books_ids.status', '=', 'borrowed'),
                                  ('borrow_end_date','=',send_email_date)])
        for records in borrow_book_history:
            mail_template = self.env.ref('ak_library_management.email_template_borrow_book_reminder')
            mail_template.send_mail(records.id, force_send=True)

    def return_borrow_book_reminder(self):
        """Return borrow books reminder when end date has passed. Send email to
        the customer.
        param:None
        return: True"""
        return_borrowed_history = self.search([('books_ids.status', '=', 'borrowed'),
                                  ('borrow_end_date', '<', date.today())])
        for history in return_borrowed_history:
            mail_template = self.env.ref('ak_library_management.return_borrow_book_reminder')
            mail_template.send_mail(history.id, force_send=True)

    def change_status_book(self):
        for rec in self.search([('books_ids.status', '=', 'borrowed')]):
            for book in rec.books_ids:
                self.env['bus.bus']._sendone(self.customer_id, 'simple_notification', {
                    'type': 'success',
                    'message': (f"{self.customer_id.name}, your book has been returned."),
                })
                book.mark_as_returned()

    def overdue_books(self):
        """raise the validation if borrowed books are overdue
        and try to borrow more books.
        param:None
        return:ValidationError"""
        overdue_book_records = self.search([('customer_id', '=', self.customer_id.id),
                                     ('books_ids.status', '=', 'borrowed'),
                                     ('borrow_end_date', '<', date.today())])
        for history in overdue_book_records:
            raise ValidationError(f"{history.customer_id.name} with overdue books "
                                  f"cannot borrow new ones until "
                                  f"they return the overdue items.")
