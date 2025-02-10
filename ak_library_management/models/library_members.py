# -*- coding: utf-8 -*-

from odoo import models,fields


class LibraryMembers(models.Model):
    """This class is storing fields of library member for the record."""
    _name = 'library.members'
    _description = 'Library Members'

    name = fields.Char(string='Member Name', required=True)
    email = fields.Char(string='Email ID')
    phone = fields.Char(string='Contact Number')
    membership_date = fields.Date(string='Membership Start Date')
