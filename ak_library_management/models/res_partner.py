# -*- coding: utf-8 -*-

from odoo import models,fields,api


class Partner(models.Model):
    """Inherit res.partner"""
    _inherit = "res.partner"

    not_trust_worthy = fields.Boolean(string='Not Trust worthy')
    is_member = fields.Boolean(string='Is Member')
    contacts_slug = fields.Char(string='Contact Slug', compute="_compute_contact_slug", store=True)

    @api.depends('name')
    def _compute_contact_slug(self):
        for contact in self:
            slug = self.env['ir.http']._slugify(str(contact))
            contact.contacts_slug = slug
