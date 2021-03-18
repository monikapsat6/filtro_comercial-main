# -*- coding: utf-8 -*-
from odoo import models, fields, api

class mrprepair(models.Model):
    _inherit = 'mrp.repair'

    @api.multi
    def action_etiqueta_impr(self):
        return self.env.ref('helpdesk_ticket.report_etiqueta_sat').report_action(self)