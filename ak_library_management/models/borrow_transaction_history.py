# -*- coding: utf-8 -*-

from datetime import datetime
from itertools import count

from odoo import models,fields,api
from odoo.exceptions import ValidationError


class BorrowTransaction(models.Model):
    """this model is based on the history of the borrowed books."""
    _name = "borrow.transaction.history"
    _description = "Borrow Transaction History"

    customer_id = fields.Many2one('res.partner', string='Customer')
    books_ids = fields.Many2many('product.template', string='Books')
    borrow_start_date = fields.Date(string='Start Date',default=datetime.today())
    borrow_end_date = fields.Date(string='End Date',required=True)
    deposit_amount = fields.Float(string='Deposit Amount')
    is_member = fields.Boolean(related="customer_id.is_member")

    @api.constrains('borrow_start_date','borrow_end_date')
    def _check_date(self):
        """give validation on end date that should be
        greater than start date."""
        for record in self:
            if record.borrow_start_date > record.borrow_end_date:
                raise ValidationError("End date should be greater tha start date.")

    def _get_warning(self,name,message):
        return {
            'type': 'ir.actions.act_window',
            'name': name,
            'res_model': 'borrow.book.warnings.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_message': message}
        }

    def action_confirm(self):
        """Method of button to raise warning according to the condition."""
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
            active_borrow_customer = self.search([('customer_id','=',self.customer_id.id)])
            books_name = []
            search_book = [books_name.append(book.name) for record in active_borrow_customer[:-1]
                           for book in record.books_ids if book.name not in books_name]
            if books_name:
                return self._get_warning('Again Borrow Books',
                                 f"Customer already has {len(active_borrow_customer)-1} open borrow "
                                 f"transactions with {books_name} books."
                                 f" Are you sure you want to borrow more books?")
            # Case B: No Open Borrow Transactions:
            else:
                return self._get_warning('Borrow Books',
                                                 'Are you sure you want to allow borrowing'
                                                 ' more than 5 books for this customer?')
