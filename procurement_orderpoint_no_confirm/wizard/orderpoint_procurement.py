# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api


class ProcurementCompute(models.TransientModel):
    _inherit = 'procurement.orderpoint.compute'

    @api.multi
    def procure_calculation(self):
        config_param_obj = self.env['ir.config_parameter']
        for record in self:
            config_param_obj.create({'key': 'procurement.order',
                                     'value': 'no_confirm'})
        return super(ProcurementCompute, self).procure_calculation()
