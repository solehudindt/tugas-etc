from odoo import api, fields, models

class PosMod(models.Model):
    _inherit = "pos.order"
    gratis_antar = fields.Boolean(default=False)

    # @api.model
    # def _order_fields(self, ui_order):
    #     res = super(PosMod, self)._order_fields(ui_order)
    #     res['gratis_antar'] = ui_order['gratis_antar'] or False
    #     return res