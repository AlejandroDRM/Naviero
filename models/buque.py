# -*- coding: utf-8 -*-
#################################################################
# Ms2 Consulting Group                                          #
#################################################################

from openerp import models, fields, api
from openerp.tools.translate import _


class buque(models.Model):

    _name = 'buque'
    _description = u'Clase Buque'
    _rec_name = 'nombre'

    @api.one
    def eliminar_buque(self):
        self.write({'eliminado': True, })
        return True

    nombre = fields.Char(_(u'Nombre'), required=True)
    siglas = fields.Char(_(u'Código IRIS'), required=True)
    bandera = fields.Char(_(u'Bandera'), required=False)
    omi = fields.Char(_(u'OMI'), required=False)
    buque_viaje_id = fields.One2many('viaje', 'buque_id', string=_(u'Viajes'), readonly=True)
    image = fields.Binary("Image")
    eliminado = fields.Boolean('Eliminado', default=False)

    _sql_constraints = [
        ('buque_uniq', 'unique(siglas)', 'Error. No puede insertar dos Buques con mismas siglas'), ]
