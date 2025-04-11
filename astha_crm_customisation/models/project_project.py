# -*- coding: utf-8 -*-

from odoo import models, fields


class ProjectProject(models.Model):
    """inherit project.project model to add a new field."""
    _inherit = "project.project"

    job_name = fields.Char(string="Job Name")