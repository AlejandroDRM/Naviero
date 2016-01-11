# -*- coding: utf-8 -*-
#################################################################
# Ms2 Consulting Group                                          #
#################################################################

from openerp import models, fields, api
from openerp.tools.translate import _


class patio(models.Model):

    _name = 'patio'
    _description = u'Clase Patio'
    _rec_name = 'descripcion'

    @api.one
    def eliminar_patio(self):
        self.write({'eliminado': True, })
        return True

    codigo = fields.Char(_(u'Código'), required=True)
    descripcion = fields.Char(_(u'Descripción'), required=True)
    puerto_id = fields.Many2one('puerto', _(u'Puerto'), required=False,
                                domain=[('eliminado', '=', False)])
    eliminado = fields.Boolean('Eliminado', default=False)
    _sql_constraints = [
        ('patio_uniq', 'unique(codigo)', 'Error. No puede insertar dos Patios con mismo código'),
    ]
