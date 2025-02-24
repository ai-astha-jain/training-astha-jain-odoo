# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class ProductTemplate(models.Model):
    """Here, inherit the product.template model to
    extend the ProductTemplate by library books
    information"""
    _inherit = 'product.template'

    is_library_book = fields.Boolean(string='Is Library Book' )
    author = fields.Char(string='Author')
    publisher = fields.Char(string='Publisher')
    edition = fields.Char(string='Edition')
    publish_date = fields.Date(string='Publish Date')
    pages = fields.Integer(string='Pages')
    available = fields.Boolean(string='Available')
    barcode = fields.Char(string='ISBN')
    status = fields.Selection([('available','Available'),
                               ('borrowed','Borrowed'),
                               ('reserved','Reserved'),
                               ('unavailable','Unavailable')],
                               string='Status',tracking=True)
    reference = fields.Char(string='Reference', default=lambda s: s.env._('New'))

    """function for button: is available"""
    def mark_as_available(self):
        self.status = 'available'

    """function for button to borrow a book"""
    def mark_as_borrowed(self):
        self.status = 'borrowed'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == _('New'):
                vals['reference'] = self.env['ir.sequence'].next_by_code('product.reference') or _('New')
        return super().create(vals_list)

    def action_borrow_books(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Borrow Book',
            'res_model': 'borrow.transaction.history',
            'view_mode': 'form',
            'target': 'new'
        }


    def write(self,vals):
        for order in self:
            old_status = order.status

        result = super().write(vals)

        for order in self:
            new_status = order.status
            if old_status != new_status:
                self.env['bus.bus']._sendone(self.env.user.partner_id, 'simple_notification', {
                    'type': 'success',
                    'sticky':True,
                    'message': _(f"Status changes from {old_status} to {new_status}."),
                })
        return result
