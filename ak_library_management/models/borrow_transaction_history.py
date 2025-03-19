# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BorrowTransaction(models.Model):
    """Show the borrow transaction of books by the customer."""
    _name = "borrow.transaction.history"
    _description = "Borrow Transaction History"

    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer', required=True)
    books_ids = fields.Many2many(comodel_name='product.template', string='Books')
    borrow_start_date = fields.Date(string='Start Date', default=datetime.today())
    borrow_end_date = fields.Date(string='End Date', required=True)
    deposit_amount = fields.Float(string='Deposit Amount')
    is_member = fields.Boolean(related="customer_id.is_member")

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
        all_record = self.search([('books_ids.status', '=', 'borrowed'),
                                  ('borrow_end_date','=',send_email_date)])
        for records in all_record:
            mail_template = self.env.ref('ak_library_management.email_template_borrow_book_reminder')
            mail_template.send_mail(records.id, force_send=True)

    def return_borrow_book_reminder(self):
        """Return borrow books reminder when end date has passed. Send email to
        the customer.
        param:None
        return: True"""
        all_record = self.search([('books_ids.status', '=', 'borrowed'),
                                  ('borrow_end_date', '<', date.today())])
        for records in all_record:
            mail_template = self.env.ref('ak_library_management.return_borrow_book_reminder')
            mail_template.send_mail(records.id, force_send=True)

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
        search_record = self.search([('customer_id', '=', self.customer_id.id),
                                     ('books_ids.status', '=', 'borrowed'),
                                     ('borrow_end_date', '<', date.today())])
        for record in search_record:
            raise ValidationError(f"{record.customer_id.name} with overdue books "
                                  f"cannot borrow new ones until "
                                  f"they return the overdue items.")
