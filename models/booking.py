# -*- coding: utf-8 -*-
#################################################################
# Ms2 Consulting Group                                          #
#################################################################

from openerp import models, fields, api
from openerp.tools.translate import _


class booking(models.Model):

    _name = 'booking'
    _description = u'Clase Booking'
    _rec_name = 'no_booking'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    TIPOS = [('full', 'Full'), ('vacio', 'Vacío')]

    @api.one
    def eliminar_booking(self):
        self.write({'eliminado': True, })
        return True

    @api.one
    @api.depends('no_booking')
    def _obtener_buque(self):
        for rec in self:
            model = self.env['viaje']
            viaje = model.browse([rec.viaje_id.id])
            rec.buque = viaje.buque_id

    no_booking = fields.Char(_(u'Número'), required=True)
    customers = fields.Many2one('beneficiario', _(u'Beneficiario'))
    cliente = fields.Many2one('res.partner', _(u'Cliente'),domain=[('customer', '=', True)])
    cantidad_contenedores = fields.Integer(_(u'Cantidad De Contenedores'), required=False)
    unidad_paquetes = fields.Char(_(u'Unidad De Paquetes'), required=False)
    cantidad_paquetes = fields.Integer(_(u'Cantidad De Paquetes'), required=False)
    peso_bruto = fields.Float(_(u'Peso Bruto Total'), required=False)
    tipo = fields.Char(_(u'Tipo'), required=False)
    naturaleza = fields.Char(_(u'Naturaleza'), required=False)
    descripcion_carga = fields.Text(_(u'Descripción De Carga'), required=False)
    viaje_id = fields.Many2one('viaje', _(u'Viaje'), required=False,
                               domain=[('eliminado', '=', False)])
    contenedores_id = fields.One2many('contenedor', 'no_booking', string=_(u'Contenedores'))
    eliminado = fields.Boolean('Eliminado', default=False)
    buque = fields.Many2one('buque', _(u'Buque'), store=True, compute='_obtener_buque')
    tipo_contenedores = fields.Selection(TIPOS, 'Tipos De Contenedor')
    _sql_constraints = [
        ('booking_uniq', 'unique(no_booking)', 'Error. No puede insertar dos Booking con mismo número'), ]
