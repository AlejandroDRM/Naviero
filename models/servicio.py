# -*- coding: utf-8 -*-
#################################################################
# Ms2 Consulting Group                                          #
#################################################################

from openerp import models, fields, api
from openerp.tools.translate import _


class servicio(models.Model):

    _name = 'servicio'
    _description = u'Clase Servicio'
    _rec_name = 'descripcion'

    @api.one
    def eliminar_servicio(self):
        self.write({'eliminado': True, })
        return True

    codigo = fields.Char(_(u'Código'), required=True)
    descripcion = fields.Char(_(u'Descripción'), required=True)
    monto = fields.Float(_(u'Monto'), required=True)
    beneficiario = fields.Many2one('res.partner', _(u'Beneficiario'), domain=[('customer', '=', True)])
    viaje_id = fields.Many2one('viaje', _(u'Viaje'), required=False)
    eliminado = fields.Boolean('Eliminado', default=False)
