# -*- coding: utf-8 -*-

from odoo import models,fields,api


class Partner(models.Model):
    """Inherit res.partner"""
    _inherit = "res.partner"

    contacts_slug = fields.Char(string='Contact Slug', compute="_compute_contact_slug", store=True)

    @api.depends('name')
    def _compute_contact_slug(self):
        for contact in self:
            slug = self.env['ir.http']._slugify(str(contact))
            contact.contacts_slug = slug
