# -*- coding: utf-8 -*-

from odoo import models, fields


class ResUsers(models.Model):
    """Inherit res.users"""
    _inherit = 'res.users'

    is_manager = fields.Boolean(string='Is Manager')
