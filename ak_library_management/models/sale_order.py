# -*- coding: utf-8 -*-
from email.policy import default
from pyexpat.errors import messages

from odoo import models, fields


class SaleOrder(models.Model):
    """Here, inherit the sale.order model to
    add more functionality."""
    _inherit = 'sale.order'
    need_confirm = fields.Boolean()
    is_approve = fields.Boolean(string='approve')

    def action_confirm(self):
        if self.is_approve:
            return super().action_confirm()
        low_stock_product = []
        for record in self.order_line:
             if record.product_template_id.qty_available < 5:
                 self.need_confirm = True
                 low_stock_product.append(record.product_template_id.name)
        if low_stock_product:
            message = (f"Approval needed! The following books have low stock: {list(low_stock_product)} ")
            return {
                'type': 'ir.actions.act_window',
                'name': 'Message',
                'res_model': 'sale.order.wizard',
                'view_mode': 'form',
                'target': 'new',
                'context':{'default_message' : message}
            }
        return super().action_confirm()

    def action_need_approve(self):
        if self.env.user.is_manager:
            self.is_approve = True
            self.need_confirm = False

    def action_need_reject(self):
        if self.env.user.is_manager:
            self.is_approve = True
        return super().action_cancel()

    def action_cancel(self):
        self.need_confirm = True
