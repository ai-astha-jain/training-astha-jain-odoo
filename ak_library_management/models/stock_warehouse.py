# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class Warehouse(models.Model):
    """Inherit stock.warehouse"""
    _inherit = "stock.warehouse"

    library_assistant_id = fields.Many2one(comodel_name='hr.employee', string="Library Assistant")
    worker_ids = fields.Many2many(comodel_name='hr.employee', string="Library Worker")

    @api.constrains('library_assistant','worker')
    def _unique_assistant(self):
        for record in self.worker_ids:
            if record.name in self.library_assistant_id.name:
                raise ValidationError(_('Assistant and worker can not be the same person.'))
