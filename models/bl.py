# -*- coding: utf-8 -*-
#################################################################
# Ms2 Consulting Group                                          #
#################################################################

from openerp import models, fields, api
from openerp.tools.translate import _


class bl(models.Model):

    _name = 'bl'
    _description = u'Clase BL'
    _rec_name = 'no_bl'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    @api.one
    def eliminar_bl(self):
        self.write({'eliminado': True, })
        return True

    @api.one
    @api.depends('no_bl')
    def _obtener_puerto_llegada(self):
        for rec in self:
            model = self.env['viaje']
            viaje = model.browse([rec.viaje_id.id])
            rec.puerto_llegada = viaje.puerto_arribo

    @api.one
    @api.depends('no_bl')
    def _obtener_buque(self):
        for rec in self:
            model = self.env['viaje']
            viaje = model.browse([rec.viaje_id.id])
            rec.buque = viaje.buque_id

    no_bl = fields.Char(_(u'Número'), required=True)
    customers = fields.Many2one('beneficiario', _(u'Beneficiario'))
    cliente = fields.Many2one('res.partner', _(u'Cliente'), domain=[('customer', '=', True)])
    cantidad_contenedores = fields.Integer(_(u'Cantidad De Contenedores'), required=False)
    unidad_paquetes = fields.Char(_(u'Unidad De Paquetes'), required=False)
    cantidad_paquetes = fields.Integer(_(u'Cantidad De Paquetes'), required=False)
    peso_bruto = fields.Float(_(u'Peso Bruto Total'), required=False)
    tipo = fields.Char(_(u'Tipo'), required=False)
    naturaleza = fields.Char(_(u'Naturaleza'), required=False)
    descripcion_carga = fields.Text(_(u'Descripción De Carga'), required=False)
    viaje_id = fields.Many2one('viaje', _(u'Viaje'), required=False,
                               domain=[('eliminado', '=', False)])
    contenedores_id = fields.One2many('contenedor', 'no_bl', string=_(u'Contenedores'))
    eliminado = fields.Boolean('Eliminado', default=False)
    buque = fields.Many2one('buque', _(u'Buque'), store=True, compute='_obtener_buque')
    dias_libres = fields.Integer(_(u'Días Libres'), required=False, default=10)
    exonerado = fields.Boolean('Exonerado', default=False)
    origen = fields.Many2one('res.country', _(u'Origen'))
    puerto_embarque = fields.Many2one('puerto', _(u'Puerto De Embarque'))
    puerto_llegada = fields.Many2one('puerto', _(u'Puerto Arribo'), compute='_obtener_puerto_llegada', store=True)
    registro_sidunea = fields.Char(_(u'Registro Sidunea'), required=False, readonly=True)
    carga_peligrosa = fields.Boolean(_(u'Carga Peligrosa'), required=False, default=False)
    impreso_venezuela = fields.Boolean(_(u'Impreso'), required=False, default=False)

    _sql_constraints = [
        ('bl_uniq', 'unique(no_bl)', 'Error. No puede insertar dos BL con mismo número'), ]
