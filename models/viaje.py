# -*- coding: utf-8 -*-
#################################################################
# Ms2 Consulting Group                                          #
#################################################################

from openerp import models, fields, api
from openerp.exceptions import ValidationError
from openerp.tools.translate import _


class viaje(models.Model):

    _name = 'viaje'
    _description = u'Clase Viaje'
    _rec_name = 'numero'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    @api.one
    @api.depends('numero')
    def _obtener_codigo_buque(self):
        for rec in self:
            model = self.env['buque']
            buque = model.browse([rec.buque_id.id])
            rec.codigo = buque.siglas

    @api.one
    def eliminar_viaje(self):
        self.write({'eliminado': True, })
        return True

    @api.one
    def notificar_consignatarios(self):
        print "Enviando correo"

    @api.one
    @api.constrains('fecha_llegada', 'fecha_inicio_operaciones', 'fecha_salida', 'fecha_fin_operaciones')
    def _check_fechas(self):
        if self.fecha_llegada <= self.fecha_salida:
            raise ValidationError("Fecha De Llegada debe ser mayor a la Fecha De Salida")
        if self.fecha_inicio_operaciones < self.fecha_llegada:
            raise ValidationError("Fecha De Inicio De Operaciones debe ser mayor o igual a la Fecha De Llegada")
        if self.fecha_regreso:
            if self.fecha_regreso <= self.fecha_llegada:
                raise ValidationError("Fecha De Regreso debe ser mayor a la Fecha De Llegada")
        if self.fecha_fin_operaciones:
            if self.fecha_fin_operaciones <= self.fecha_inicio_operaciones:
                raise ValidationError("Fecha De Fin De Operaciones debe ser mayor a la Fecha De Inicio De Operaciones")

    @api.one
    @api.depends('numero', 'buque_id', 'puerto_arribo')
    def _set_clave(self):
        self.clave = '{0}{1}{2}'.format(self.numero, self.buque_id.nombre, self.puerto_arribo.descripcion)

    @api.one
    @api.constrains('registro_sidunea')
    def _asignar_registros_sidunea(self):
        for rec in self:
            model = self.env['bl']
            bls = model.search([('viaje_id', '=', self.numero)])
            for bl_aux in bls:
                bl_aux.registro_sidunea = self.registro_sidunea

    linea = fields.Many2one('linea', _(u'Línea'), required=False, domain=[('eliminado', '=', False)])
    ruta = fields.Many2one('ruta', _(u'Ruta'), required=False, domain=[('eliminado', '=', False)])
    puerto_arribo = fields.Many2one('puerto', _(u'Puerto De Arribo'), required=True,
                                    domain=[('eliminado', '=', False)])
    puerto_origen = fields.Many2one('puerto', _(u'Puerto De Origen'), required=True,
                                    domain=[('eliminado', '=', False)])
    puerto_regreso = fields.Many2one('puerto', _(u'Puerto De Salida'), required=False,
                                     domain=[('eliminado', '=', False)])
    codigo = fields.Char(_(u'Siglas'), compute='_obtener_codigo_buque', required=False)
    fecha_llegada = fields.Date(_(u'Fecha De Llegada'), required=True)
    fecha_inicio_operaciones = fields.Date(_(u'Inicio De Operaciones'), store=True, required=True)
    fecha_salida = fields.Date(_(u'Fecha De Salida'), required=True)
    fecha_regreso = fields.Date(_(u'Fecha De Zarpe'), required=False)
    buque_id = fields.Many2one('buque', _(u'Buque'), required=True, domain=[('eliminado', '=', False)])
    numero = fields.Char(_(u'Viaje'), required=True)
    contenedores_id = fields.One2many('contenedor', 'viaje_id', string=_(u'Contenedores'))
    bls_id = fields.One2many('bl', 'viaje_id', string=_(u'BLS'))
    contenedores_id_salida = fields.One2many('contenedor', 'viaje_salida', string=_(u'Contenedores'))
    servicios_id = fields.One2many('servicio', 'viaje_id', string=_(u'Servicios'))
    beneficiarios_id = fields.Many2many('beneficiario', 'codigo', string=_(u'Beneficiarios'))
    cantidad_bls = fields.Integer(_(u'Cantidad de BLS'), required=False)
    cantidad_bultos = fields.Integer(_(u'Cantidad De Bultos'), required=False)
    cantidad_contenedores = fields.Integer(_(u'Cantidad De Contenedores'), required=False)
    peso_bruto = fields.Integer(_(u'Peso Bruto'), required=False)
    peso_neto = fields.Integer(_(u'Peso Neto'), required=False)
    peso_bruto_total = fields.Float(_(u'Peso Bruto Total'), required=False)
    fecha_fin_operaciones = fields.Date(_(u'Fin De Operaciones'), store=True, required=False)
    eliminado = fields.Boolean('Eliminado', default=False)
    clave = fields.Char(_(u'Clave'), required=False, store=True, compute='_set_clave')
    registro_sidunea = fields.Char(_(u'Registro Sidunea'), required=False)
    _sql_constraints = [
        ('viaje_uniq', 'unique(clave)', 'Error. No puede insertar dos Viajes con mismos número, buque y puerto'),
        ('registro_sidunea_uniq', 'unique(registro_sidunea)', 
         'Error. No puede insertar dos Registro Sidunea con mismos número'),
    ]

