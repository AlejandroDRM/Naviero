# -*- coding: utf-8 -*-
#################################################################
# Ms2 Consulting Group                                          #
#################################################################

from openerp import models, fields, api
from openerp.tools.translate import _


class ruta(models.Model):

    _name = 'ruta'
    _description = u'Clase Ruta'
    _rec_name = 'descripcion'

    @api.one
    def eliminar_ruta(self):
        self.write({'eliminado': True, })
        return True

    codigo = fields.Char(_(u'Código'), required=True)
    descripcion = fields.Char(_(u'Descripción'), required=True)
    eliminado = fields.Boolean('Eliminado', default=False)
    _sql_constraints = [
        ('ruta_uniq', 'unique(codigo)', 'Error. No puede insertar dos Rutas con mismo código'),
    ]
