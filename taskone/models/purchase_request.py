import dateutil.utils
from odoo import api, fields, models


class PurchaseRequest(models.Model):
    _name = "purchase.request"
    _description = "Purchase Request"
    _rec_name = "request_name"

    request_name = fields.Char(required=True)
    requested_by = fields.Many2one('res.users', default=lambda self: self.env.uid, required=True)
    start_date = fields.Date(default=dateutil.utils.today())
    end_date = fields.Date()
    rejection_reason = fields.Text(readonly=True)
    orderlines = fields.One2many('purchase.request.line', 'purchase_request_id')
    total_price = fields.Float(compute='_compute_sum_lines', readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit_for_approval', 'SubmitForApproval'),
        ('to_be_approved', 'ToBeApproved'),
        ('approve', 'Approve'),
        ('reject', 'Reject'),
        ('reset', 'Reset'),
        ('cancel', 'Cancel')
    ], default="draft", string="Status")

    @api.depends('orderlines')
    def _compute_sum_lines(self):
        for rec in self:
            rec.total_price = sum(line.total for line in rec.orderlines)

    def action_submit_approval(self):
        for rec in self:
            rec.state = "to_be_approved"

    def action_cancel(self):
        for rec in self:
            rec.state = "to_be_approved"

    def get_email_to(self):
        pass
        # user_group = self.env.ref("res.group_res_user")
        # email_list = [
        #     usr.partner_id.email for usr in user_group.users if usr.partner_id.email]
        # return ",".join(email_list)

    def action_approve(self):
        template_id = self.env.ref('taskone.purchase_approve_email_template').id
        template = self.env['mail.template'].browse(template_id)
        print("template==>", template)
        user_group = self.env("res.groups.group_res_user")
        # template.send_mail(user_group.id, force_send=True)
        # group_purchase_manager

    def action_reject(self):
        pass

    def action_reset(self):
        pass
