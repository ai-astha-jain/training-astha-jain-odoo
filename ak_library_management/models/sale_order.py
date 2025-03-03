# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrder(models.Model):
    """Here, inherit the sale.order model to
    add more functionality."""
    _inherit = 'sale.order'

    need_confirm = fields.Boolean()
    is_approve = fields.Boolean()

    def action_confirm(self):
        """Checks if on-hand quantity is less than 5. If on-hand
        quantity is less than 5 approval message pop-up else follow
        the odoo base flow."""
        if not self.is_approve:
            low_stock_product = []
            for record in self.order_line:
                if record.product_template_id.qty_available < 5:
                    self.need_confirm = True
                    low_stock_product.append(record.product_template_id.name)
            if low_stock_product:
                message = (f"Approval needed! The following books have low stock: "
                           f"{list(low_stock_product)} ")
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
        """method for approve button."""
        if self.env.user.is_manager:
            self.is_approve = True
            self.need_confirm = False

    def action_need_reject(self):
        """Works as a cancel button."""
        if self.env.user.is_manager:
            self.is_approve = True
        self.action_cancel()
