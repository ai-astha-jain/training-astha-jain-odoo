# -*- coding: utf-8 -*-

from odoo import models,fields

class LibraryMember(models.Model):
    """Models name is library.member. It stores the information about the members of
    library."""
    _name = 'library.member'
    _description = 'Library Members'


    name = fields.Char(string='Member Name', required=True)
    email = fields.Char(string='Email ID')
    phone = fields.Char(string='Contact Number')
    membership_date = fields.Date(string='Membership Start Date')
