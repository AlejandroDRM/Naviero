# -*- coding: utf-8 -*-
#################################################################
# Ms2 Consulting Group                                          #
#################################################################

from openerp import models, fields, api
from openerp.tools.translate import _


class material(models.Model):

    _name = 'material'
    _description = u'Clase Material'
    _rec_name = 'descripcion'

    @api.one
    def eliminar_material(self):
        self.write({'eliminado': True, })
        return True

    codigo = fields.Char(_(u'Código'), required=True)
    descripcion = fields.Char(_(u'Descripción'), required=True)
    hoja_seguridad = fields.Char(_(u'Hoja De Seguridad'), required=True)
    eliminado = fields.Boolean('Eliminado', default=False)
