# -*- coding: utf-8 -*-
#################################################################
# Ms2 Consulting Group                                          #
#################################################################

from openerp import models, fields, api
from openerp.tools.translate import _


class gasto(models.Model):

    _name = 'gasto'
    _description = u'Clase Gasto'
    _rec_name = 'descripcion'

    @api.one
    def eliminar_gasto(self):
        self.write({'eliminado': True, })
        return True

    GASTOS = [('Adicional', 'Adicional'), ('Local', 'Local')]
    codigo = fields.Char(_(u'Código'), required=True)
    descripcion = fields.Char(_(u'Descripción'), required=True)
    valor = fields.Float(_(u'Valor'), required=True)
    tipo = fields.Selection(GASTOS, string=_(u'Tipo'), required=True)
    cuenta_contable = fields.Char(_(u'Cuenta Contable'), required=True)
    eliminado = fields.Boolean('Eliminado', default=False)
