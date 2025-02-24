# -*- coding: utf-8 -*-

from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import datetime


class BorrowTransaction(models.Model):

    _name = "borrow.transaction.history"
    _description = "Borrow Transaction History"

    customer_id = fields.Many2one('res.partner', string='Customer')
    books = fields.Many2many('product.template', string='Books')
    borrow_start_date = fields.Date(string='Start Date',default=datetime.today())
    borrow_end_date = fields.Date(string='End Date')
    deposit_amount = fields.Float(string='Deposit Amount')

    @api.constrains('borrow_start_date','borrow_end_date')
    def _check_date(self):
        for record in self:
            if record.borrow_start_date > record.borrow_end_date:
                raise ValidationError("End date should be greater tha start date.")

    def confirm(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Borrow Book',
            'res_model': 'borrow.transaction.history',
            'view_mode': 'form',
            'target': 'new'
        }
