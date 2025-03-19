# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class LibraryMembers(models.Model):
    """This class is storing fields of library member for the record."""
    _name = 'library.members'
    _description = 'Library Members'
    _rec_name = 'lib_member_id'

    lib_member_id = fields.Many2one(comodel_name='res.partner', required=True, string="Library Member Id")
    email = fields.Char(string='Email ID',related="lib_member_id.email")
    phone = fields.Char(string='Contact Number')
    membership_date = fields.Date(string='Membership Start Date')
    member_id = fields.Char(string='Member ID',copy=False, default=lambda s: s.env._('New'))

    @api.model_create_multi
    def create(self, vals_list):
        """to generate the unique sequence for the members of library.
        param: vals_list
        return: True"""
        for vals in vals_list:
            if not vals.get('member_id') or vals['member_id'] == _('New'):
                vals['member_id'] = (self.env['ir.sequence']
                                     .next_by_code('library.membership') or _('New'))
        return super().create(vals_list)

    def send_renewal_mail(self):
        """return the mail compose wizard for the renewal of membership.
        Only manager or librarian can send the mail.
        param: None
        return: True"""
        template = self.env.ref('ak_library_management.send_email_renewal_membership')
        ctx = {'default_template_id':template.id}
        if self.env.user.is_manager:
            return {
                'name': _('Renewal Membership'),
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'mail.compose.message',
                'target': 'new',
                'context': ctx,
            }
        raise ValidationError(_('You are not allowed to send email as you are not a manager.'))

