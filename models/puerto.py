# -*- coding: utf-8 -*-
#################################################################
# Ms2 Consulting Group                                          #
#################################################################

import re
from openerp import models, fields, api
from openerp.exceptions import ValidationError
from openerp.tools.translate import _


class puerto(models.Model):

    @api.one
    def eliminar_puerto(self):
        self.write({'eliminado': True, })
        return True

    @api.one
    @api.constrains('correo')
    def _check_correo(self):
        if self.correo:
            patron = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$')
            if not(patron.match(self.correo)):
                raise ValidationError("Dirección de Correo Electrónico inválida")

    _name = 'puerto'
    _description = u'Clase Puerto'
    _rec_name = 'descripcion'
    codigo = fields.Char(_(u'Código'), required=True)
    descripcion = fields.Char(_(u'Descripción'), required=True)
    direccion = fields.Char(_(u'Dirección'), required=False)
    correo = fields.Char(_(u'Correo electrónico'), required=False)
    eliminado = fields.Boolean('Eliminado', default=False)
    puertos = fields.One2many('patio', 'puerto_id', string=_(u'Puertos'))
    _sql_constraints = [
        ('puerto_uniq', 'unique(codigo)', 'Error. No puede insertar dos Puertos con mismo código'),
    ]
