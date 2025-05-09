# -*- coding: utf-8 -*-

from datetime import date, timedelta
from email.policy import default

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    """Here, inherit the product.template model to
    extend the ProductTemplate by library books
    information"""
    _inherit = 'product.template'

    is_library_book = fields.Boolean(string='Is Library Book')
    author = fields.Char(string='Author')
    publisher = fields.Char(string='Publisher')
    edition = fields.Char(string='Edition')
    publish_date = fields.Date(string='Publish Date')
    pages = fields.Integer(string='Pages')
    available = fields.Boolean(string='Available')
    barcode = fields.Char(string='ISBN')
    status = fields.Selection([('available', 'Available'),
                               ('borrowed', 'Borrowed'),
                               ('reserved', 'Reserved'),
                               ('unavailable', 'Unavailable')],
                              string='Status', tracking=True)
    reference = fields.Char(string='Reference', default=lambda s: s.env._('New'), copy=False)
    vendors_on_variants = fields.Boolean(string='Vendors on Variants', default=False)

    def mark_as_available(self):
        """change the status to available.
        param: None
        return: True"""
        self.status = 'available'

    def mark_as_borrowed(self):
        """change the status to borrowed and log the activity to show book due date.
        param: None
        return: True"""
        self.status = 'borrowed'
        activity_message = _("The book due date in 10 days")
        self.activity_schedule(
            date_deadline=date.today() + timedelta(days=10),
            user_id=self.env.user.id,
            note=activity_message,
            summary="due in 10 days"
        )

    @api.constrains('status')
    def log_message(self):
        """log the note in the chatter when customer will borrow the book.
        param: None
        return: True"""
        if self.status == 'borrowed':
            self.message_post(body=(_(f"The books is borrowed by {self.name} on {date.today()}")))
        if self.status == 'reserved':
            self.message_post(body=(_(f"The books is returned by {self.name}.")))

    @api.model_create_multi
    def create(self, vals_list):
        """generate the sequence for the product.
        param: vals_list.
        return: True"""
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == _('New'):
                vals['reference'] = (self.env['ir.sequence']
                                     .next_by_code('product.reference') or _('New'))
        return super().create(vals_list)

    # @api.constrains('status')
    def action_borrow_books(self):
        """Here I have added a python constraint which is not valid as
        py constraints only works in create and write method but according to
         the question I have tried to add the constraint in action button.
         Please check borrow button wizard where I have given the python
         constraint properly."""
        # if self.name and self.status == 'unavailable':
        #     raise ValidationError(_("You can not borrow the book as this book is unavailable."))
        # if self.env.user.library_admin:
        #     raise ValidationError(_('You do not have rights to borrow the books.'))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Borrow Book',
            'res_model': 'borrow.transaction.history',
            'view_mode': 'form',
            'target': 'new'
        }

    def write(self, vals):
        """send the notification when the status will get changed of the product.
        param: vals
        return: True"""
        for order in self:
            old_status = order.status
        result = super().write(vals)

        for order in self:
            new_status = order.status
            if old_status != new_status:
                self.env['bus.bus']._sendone(self.env.user.partner_id, 'simple_notification', {
                    'type': 'success',
                    'sticky': True,
                    'message': _(f"Status changes from {old_status} to {new_status}."),
                })
        return result

    def mark_as_returned(self):
        """change the status to reserved.
        param: None
        return: True"""
        print(self.write({'status': 'reserved'}))
        self.write({'status': 'reserved'})
