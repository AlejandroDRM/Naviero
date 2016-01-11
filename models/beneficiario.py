# -*- coding: utf-8 -*-
#################################################################
# Ms2 Consulting Group                                          #
#################################################################

from openerp import models, fields, api
from openerp.tools.translate import _


class beneficiario(models.Model):

    _name = 'beneficiario'
    _description = u'Clase Beneficiario'
    _rec_name='nombre'
	
    @api.one
    def eliminar_beneficiario(self):
        self.write({'eliminado': True, })
        return True
		
    codigo = fields.Char(_(u'RIF'),required=False)
    nombre = fields.Char(_(u'Nombre'), required=False)
    correo = fields.Char(_(u'Correo'),required=False)
    telefono = fields.Char(_(u'Teléfono'), required=False)
    direccion = fields.Char(_(u'Dirección'), required=False)
    banco = fields.Char(_(u'Banco'), required=False)
    direccion_banco = fields.Char(_(u'Dirección Del Banco'), required=False)
    swift = fields.Char(_(u'Swift Del Beneficiario'), required=False)
    cuenta = fields.Char(_(u'Cuenta Del Beneficiario'), required=False)
    intermediario = fields.Char(_(u'Intermediario'), required=False)
    direccion_intermediario = fields.Char(_(u'Dirección Del Intermediario'), required=False)
    banco_intermediario = fields.Char(_(u'Banco Del Intermediario'), required=False)
    direccion_banco_intermediario = fields.Char(_(u'Dirección Banco Del Intermediario'), required=False)
    cuenta_intermediario = fields.Char(_(u'Cuenta Del Intermediario'), required=False)
    swift_intermediario = fields.Char(_(u'Swift Del Intermediario'), required=False)
    eliminado = fields.Boolean('Eliminado', default=False)
	
    _sql_constraints = [
    ('cliente_uniq', 'unique(codigo)', 'Error. No puede insertar dos clientes con mismo RIF'),
    ]