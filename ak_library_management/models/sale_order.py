# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrder(models.Model):
    """Here, inherit the sale.order model to
    add more functionality."""
    _inherit = 'sale.order'

    need_confirm = fields.Boolean(string='need_confirm')
    is_approve = fields.Boolean(string='is_approve')

    def action_confirm(self):
        """
        Override: Open a wizard.
        if product on-hand quantity is less than 5.
        open wizard: product on-hand quantity is less than 5
        else follow the odoo base flow.
        return: True
        """
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
                    'name': 'Warning',
                    'res_model': 'check.low.stock.wizard',
                    'view_mode': 'form',
                    'target': 'new',
                    'context': {'default_message': message}
                }
        return super().action_confirm()

    def action_need_approve(self):
        """
        Define: asking for approval
        if approve button gets clicked confirm button reappear.
        odoo base will be followed.
        return: True
        """
        if self.env.user.is_manager:
            self.is_approve = True
            self.need_confirm = False

    def action_need_reject(self):
        """ Cancel SO after showing the cancel wizard when needed."""
        if self.env.user.is_manager:
            self.is_approve = True
            self.need_confirm = False
        self.action_cancel()
