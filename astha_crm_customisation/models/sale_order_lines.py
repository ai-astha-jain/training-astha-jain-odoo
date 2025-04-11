# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrderLine(models.Model):
    """inherit sale.order.line to add functionality."""
    _inherit = 'sale.order.line'

    def _timesheet_create_project_prepare_values(self):
        res = super()._timesheet_create_project_prepare_values()
        res["job_name"] = self.order_id.job_name

    def _timesheet_create_project_prepare_values(self):
        res = super()._timesheet_create_project_prepare_values()
        res["job_name"] = self.order_id.job_name
        res['name'] = '%s - %s' % (self.order_id.name,self.order_id.job_name) if self.order_id.job_name else self.order_id.name
        return res
