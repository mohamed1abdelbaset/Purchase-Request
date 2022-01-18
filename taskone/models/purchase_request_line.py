from odoo import api, fields, models


class PurchaseRequestLine(models.Model):
    _name = "purchase.request.line"
    _description = "Purchase Request Line"
    # _rec_name = "description"

    product_id = fields.Many2one('product.product', required=True)
    description = fields.Char()
    quantity = fields.Float(default=1)
    cost_price = fields.Float(readonly=True, related='product_id.standard_price')
    purchase_request_id = fields.Many2one('purchase.request')
    total = fields.Float(compute='_compute_total', readonly=True)

    @api.depends('quantity')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.quantity * rec.cost_price

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id.name:
            self.description = self.product_id.name
        else:
            self.description = ''

