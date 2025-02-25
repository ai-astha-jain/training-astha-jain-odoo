# -*- coding: utf-8 -*-

from odoo import models,fields,api,_


class LibraryMembers(models.Model):
    """This class is storing fields of library member for the record."""
    _name = 'library.members'
    _description = 'Library Members'

    name = fields.Char(string='Member Name', required=True)
    email = fields.Char(string='Email ID')
    phone = fields.Char(string='Contact Number')
    membership_date = fields.Date(string='Membership Start Date')
    member_id = fields.Char(string='Member ID',copy=False)

    @api.model_create_multi
    def create(self, vals_list):
        """to generate the sequence for the members of library"""
        for vals in vals_list:
            if not vals.get('member_id') or vals['member_id'] == _('New'):
                vals['member_id'] = (self.env['ir.sequence']
                                     .next_by_code('library.membership') or _('New'))
        return super().create(vals_list)
