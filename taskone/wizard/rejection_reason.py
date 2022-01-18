# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class RejectionReasonWizard(models.TransientModel):
    _name = "rejection.reason.wizard"
    _description = "Rejection Reason Wizard"

    rejection_reason = fields.Text(string='Rejection Reason', required=True)

    # def rejection_reason_action(self):
    #     vals = {
    #         'rejection_reason': self.rejection_reason,
    #     }
    #     self.env['purchase.request'].create(vals)

    def rejection_reason_confirm(self):
        # result = self.env['purchase.request'].browse(self._context.get('active_id'))
        # result = super(RejectionReasonWizard, self).rejection_reason()

        rej_obj = self.env['purchase.request'].browse(self._context.get('active_id'))
        rej_obj.rejection_reason = self.rejection_reason
        return rej_obj
        # result = super(AccountInvoiceRefund, self).invoice_refund()
        # invoice_obj = self.env['account.invoice'].browse(self._context.get('active_id'))
        # invoice_obj.is_refund = self.is_refund
        # return result
