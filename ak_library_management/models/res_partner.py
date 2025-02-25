# -*- coding: utf-8 -*-

from odoo import models,fields


class Partner(models.Model):
    """Inherit res.partner"""
    _inherit = "res.partner"

    not_trust_worthy = fields.Boolean(string='Not Trust worthy')
    is_member = fields.Boolean(string='Is Member')
