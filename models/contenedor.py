# -*- coding: utf-8 -*-
#################################################################
# Ms2 Consulting Group                                          #
#################################################################


from datetime import timedelta, datetime
from openerp import models, fields, api
from openerp.exceptions import ValidationError
from openerp.tools.translate import _


class contenedor_movimiento(models.Model):

    _name = 'contenedor.movimiento'
    _description = u'Clase Movimientos De Contenedor'
    _rec_name = 'movimiento'

    MOVIMIENTOS = [('descargado', 'Descargado'),
                   ('despacho_full_consignatario', 'Despacho Full al Consignatario'),
                   ('recibido_vacio_consignatario', 'Recibido vacio del consignatario'),
                   ('embarcado_vacio', 'Embarcado Vacío'),
                   ('asignado_vacio_exportador', 'Asignado vacío al exportador'),
                   ('retorno_full_exportacion', 'Retorno full para exportación'),
                   ('embarque_full_exportacion', 'Embarcado full exportación'),
                   ('entrega_shiperon', 'Despacho Shiperon'),
                   ('embarque_shiperon', 'Embarque Shiperon'), ]

    @api.one
    @api.constrains('fecha')
    def _check_fecha_movimiento(self):
        ctrl_equipos = False
        usuario_actual = self.env.user
        for id_grupo in usuario_actual.groups_id:
            if id_grupo.name == "Control De Equipos":
                ctrl_equipos = True
        fecha_movimiento = datetime.strptime(self.fecha, "%Y-%m-%d")
        fecha_auxiliar = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
        if fecha_movimiento < fecha_auxiliar and self.movimiento != "descargado" and \
           self.movimiento != "embarcado_vacio" and self.movimiento != "embarcado_full" and ctrl_equipos is False:
            raise ValidationError("No se puede asignar fecha de movimiento menor al día de ayer")
        elif fecha_movimiento > datetime.today():
            raise ValidationError("Fecha de movimiento no puede ser superior a la fecha de hoy")

    @api.one
    @api.constrains('movimiento', 'eir', 'puerto', 'patio', 'fecha', 'hora', 'buque', 'viaje', 'operativo', 'booking', )
    def _check_movimiento(self):
        ctrl_equipos = False
        usuario_actual = self.env.user
        contenedor_encontrado = False
        for id_grupo in usuario_actual.groups_id:
            if id_grupo.name == "Control De Equipos":
                ctrl_equipos = True

        for rec in self:
            model = self.env['contenedor']
            contenedores = model.search([('numero', '=', self.contenedor_id_aux), ('fecha_salida', '=', False)])
            for contenedor_aux in contenedores:
                self.bl_id_aux = contenedor_aux.no_bl.no_bl
                contenedor = contenedor_aux
                estado = contenedor.state
                self.contenedor_id = contenedor_aux
                contenedor_encontrado = True
        if not contenedor_encontrado:
            raise ValidationError("No existe en inventario el contenedor: {}".format(self.contenedor_id_aux))

        if self.movimiento == "descargado":
            if estado != "en_camino" and not ctrl_equipos:
                raise ValidationError("Movimiento inválido, el contenedor no se encuentra en estado: En Camino")
            if not self.puerto.id or not self.patio.id:
                raise ValidationError("Debe introducir un puerto y patio")
            else:
                contenedor.fecha_inicio_operaciones = self.fecha
                contenedor.puerto_actual = self.puerto
                contenedor.patio = self.patio
                contenedor.operativo = self.operativo
                if contenedor.observaciones:
                    contenedor.observaciones = '{0} {1}'.format(contenedor.observaciones, self.observaciones)
                else:
                    contenedor.observaciones = self.observaciones
                contenedor.state = "en_puerto"

        elif self.movimiento == "entrega_shiperon":
            if estado != "en_puerto" and not ctrl_equipos:
                raise ValidationError("Movimiento inválido, el contenedor no se encuentra en estado: Full En Puerto")
            if not self.puerto.id:
                self.puerto = contenedor.puerto_actual
            contenedor.puerto_actual = self.puerto
            contenedor.fecha_entrega = self.fecha
            contenedor.fecha_devolucion = self.fecha
            contenedor.fecha_salida = self.fecha
            contenedor.eir = self.eir
            contenedor.operativo = self.operativo
            if contenedor.observaciones:
                contenedor.observaciones = '{0} {1}'.format(contenedor.observaciones, self.observaciones)
            else:
                contenedor.observaciones = self.observaciones
            contenedor.state = "entregado_shiperon"

        elif self.movimiento == "embarque_shiperon":
            if not self.viaje.id:
                raise ValidationError("Debe introducir un viaje")
            if not self.booking:
                raise ValidationError("Debe introducir un número de booking")
            else:
                booking_valido = False
                booking1 = self.env['booking']
                bookings = booking1.search([('no_booking', '=', self.booking), ])
                for booking_aux in bookings:
                    contenedor.no_booking = booking_aux
                    booking_valido = True
                if not booking_valido:
                    raise ValidationError("No existe número de booking")
            contenedor.puerto_actual = self.puerto
            contenedor.fecha_llegada = self.fecha
            contenedor.fecha_entrega = self.fecha
            contenedor.fecha_devolucion = self.fecha
            contenedor.fecha_salida = self.fecha
            contenedor.operativo = self.operativo
            contenedor.buque_salida = self.buque
            contenedor.viaje_salida = self.viaje
            if contenedor.observaciones:
                contenedor.observaciones = '{0} {1}'.format(contenedor.observaciones, self.observaciones)
            else:
                contenedor.observaciones = self.observaciones
            contenedor.state = "embarcado_shiperon"

        elif self.movimiento == "despacho_full_consignatario":
            if estado != "en_puerto" and not ctrl_equipos:
                raise ValidationError("Movimiento inválido, el contenedor no se encuentra en estado: Full En Puerto")
            if not self.eir:
                raise ValidationError("Debe introducir un número de EIR")
            else:
                if not self.puerto.id:
                    self.puerto = contenedor.puerto_actual
                contenedor.puerto_actual = self.puerto
                contenedor.fecha_entrega = self.fecha
                contenedor.eir = self.eir
                contenedor.operativo = self.operativo
                if contenedor.observaciones:
                    contenedor.observaciones = '{0} {1}'.format(contenedor.observaciones, self.observaciones)
                else:
                    contenedor.observaciones = self.observaciones
                contenedor.state = "despachado"
        elif self.movimiento == "recibido_vacio_consignatario":
            if estado != "despachado" and not ctrl_equipos:
                raise ValidationError("Movimiento inválido, el contenedor no se encuentra en estado:"
                                      "En Poder Del Consignatario")
            if not self.eir:
                raise ValidationError("Debe introducir un número de EIR")
            if not self.patio.id:
                raise ValidationError("Debe introducir un patio")
            else:
                if not self.puerto.id:
                    self.puerto = contenedor.puerto_actual
                contenedor.fecha_devolucion = self.fecha
                contenedor.puerto_actual = self.puerto
                contenedor.patio = self.patio
                contenedor.operativo = self.operativo
                contenedor.eir = self.eir
                if contenedor.observaciones:
                    contenedor.observaciones = '{0} {1}'.format(contenedor.observaciones, self.observaciones)
                else:
                    contenedor.observaciones = self.observaciones
                contenedor.state = "devuelto"
        elif self.movimiento == "embarcado_vacio":
            if estado != "devuelto" and not ctrl_equipos:
                raise ValidationError("Movimiento inválido, el contenedor no se encuentra en estado: Vacío Recibido")
            if not self.viaje.id:
                raise ValidationError("Debe introducir un viaje")
            if not self.booking:
                raise ValidationError("Debe introducir un número de booking")
            else:
                booking_valido = False
                booking1 = self.env['booking']
                bookings = booking1.search([('no_booking', '=', self.booking)])
                for booking_aux in bookings:
                    contenedor.no_booking = booking_aux
                    booking_valido = True
                if not booking_valido:
                    raise ValidationError("No existe número de booking")
                contenedor.fecha_salida = self.fecha
                contenedor.operativo = self.operativo
                contenedor.buque_salida = self.buque
                contenedor.viaje_salida = self.viaje
                if contenedor.observaciones:
                    contenedor.observaciones = '{0} {1}'.format(contenedor.observaciones, self.observaciones)
                else:
                    contenedor.observaciones = self.observaciones
                if not self.puerto.id:
                    self.puerto = contenedor.puerto_actual
                contenedor.puerto_actual = self.puerto
                contenedor.state = "embarcado_vacio"
        elif self.movimiento == "asignado_vacio_exportador":
            if estado != "devuelto" and not ctrl_equipos:
                raise ValidationError("Movimiento inválido, el contenedor no se encuentra en estado: Vacío Recibido")
            if not self.eir:
                raise ValidationError("Debe introducir un número de EIR")
            if not self.patio.id:
                raise ValidationError("Debe introducir un patio")
            else:
                if not self.puerto.id:
                    self.puerto = contenedor.puerto_actual
                contenedor.puerto_actual = self.puerto
                contenedor.patio = self.patio
                contenedor.eir = self.eir
                contenedor.operativo = self.operativo
                if contenedor.observaciones:
                    contenedor.observaciones = '{0} {1}'.format(contenedor.observaciones, self.observaciones)
                else:
                    contenedor.observaciones = self.observaciones
                contenedor.state = "vacio_exportacion"

        elif self.movimiento == "retorno_full_exportacion":
            if estado != "vacio_exportacion" and not ctrl_equipos:
                raise ValidationError("Movimiento inválido, el contenedor no se encuentra en estado: "
                                      " Vacío Para Exportación")
            if not self.eir:
                raise ValidationError("Debe introducir un número de EIR")
            if not self.patio.id:
                raise ValidationError("Debe introducir un patio")
            else:
                if not self.puerto.id:
                    self.puerto = contenedor.puerto_actual
                contenedor.puerto_actual = self.puerto
                contenedor.patio = self.patio
                contenedor.eir = self.eir
                contenedor.operativo = self.operativo
                if contenedor.observaciones:
                    contenedor.observaciones = '{0} {1}'.format(contenedor.observaciones, self.observaciones)
                else:
                    contenedor.observaciones = self.observaciones
                contenedor.state = "full_exportacion"
        elif self.movimiento == "embarque_full_exportacion":
            if estado != "full_exportacion" and not ctrl_equipos:
                raise ValidationError("Movimiento inválido, el contenedor no se encuentra en estado: "
                                      "Full Para Exportación")
            if not self.viaje.id:
                raise ValidationError("Debe introducir un viaje")
            if not self.booking:
                raise ValidationError("Debe introducir un número de booking")
            else:
                booking_valido = False
                booking1 = self.env['booking']
                bookings = booking1.search([('no_booking', '=', self.booking)])
                for booking_aux in bookings:
                    contenedor.no_booking = booking_aux
                    booking_valido = True
                if not booking_valido:
                    raise ValidationError("No existe número de booking")
                contenedor.fecha_salida = self.fecha
                contenedor.operativo = self.operativo
                contenedor.buque_salida = self.buque
                contenedor.viaje_salida = self.viaje
                if contenedor.observaciones:
                    contenedor.observaciones = '{0} {1}'.format(contenedor.observaciones, self.observaciones)
                else:
                    contenedor.observaciones = self.observaciones
                if not self.puerto.id:
                    self.puerto = contenedor.puerto_actual
                contenedor.puerto_actual = self.puerto
                contenedor.state = "embarcado_full"

    @api.one
    @api.depends('contenedor_id', 'movimiento')
    def _obtener_usuario(self):
        user_id = self.env.user
        self.usuario = user_id.name

    @api.one
    @api.depends('viaje')
    def _obtener_buque(self):
        for rec in self:
            model = self.env['viaje']
            viaje = model.browse([rec.viaje.id])
            rec.buque = viaje.buque_id

    @api.one
    @api.depends('bl_id_aux')
    def _obtener_datos_llegada(self):
        for rec in self:
            model = self.env['bl']
            bls = model.search([('no_bl', '=', self.bl_id_aux)])
            for bl in bls:
                self.viaje_llegada = bl.viaje_id
                self.buque_llegada = bl.buque

    @api.one
    @api.depends('fecha')
    def _asignar_fechas_aux(self):
        self.fecha_desde = self.fecha

    @api.one
    @api.depends('fecha')
    def _asignar_fechas_aux2(self):
        self.fecha_hasta = self.fecha

    @api.one
    def _asignar_registros_sidunea(self):
        for rec in self:
            model = self.env['viaje']
            viaje = model.browse([rec.viaje_id.id])
            rec.registro_sidunea = viaje.registro_sidunea

    contenedor_id = fields.Many2one('contenedor', _(u'Contenedor Aux'), required=False)
    contenedor_id_aux = fields.Char(_(u'Contenedor'), required=True)

    bl_id = fields.Many2one('bl', _(u'BL Aux'), required=False)
    bl_id_aux = fields.Char(_(u'BL'), readonly=True, required=False)

    movimiento = fields.Selection(MOVIMIENTOS, 'Movimiento', required=True)
    fecha = fields.Date(_(u'Fecha'), required=True, default=datetime.today().strftime('%Y-%m-%d'))
    hora = fields.Char(_(u'Hora'), required=True)
    puerto = fields.Many2one('puerto', _(u'Puerto'), required=False)
    patio = fields.Many2one('patio', _(u'Patio'), required=False, default="_obtener_puerto")
    eir = fields.Char(_(u'EIR'), required=False)
    booking = fields.Char(_(u'Booking'), required=False)
    operativo = fields.Boolean('Op', default=True)
    usuario = fields.Char(_(u'Usuario'), store=True, compute='_obtener_usuario', readonly=True)
    buque = fields.Many2one('buque', _(u'Buque'), compute="_obtener_buque", readonly=True, required=False)
    viaje = fields.Many2one('viaje', _(u'Viaje'), domain=[('fecha_regreso', '=', False)], required=False)
    observaciones = fields.Text(_(u'Obs.'), required=False)
    buque_llegada = fields.Many2one('buque', _(u'Buque Llegada'), store=True, compute='_obtener_datos_llegada')
    viaje_llegada = fields.Many2one('viaje', _(u'Viaje Llegada'), required=False,
                                    compute='_obtener_datos_llegada', domain=[('eliminado', '=', False)])
    fecha_desde = fields.Date(_(u'Fecha desde'), required=False, store=True, compute='_asignar_fechas_aux')
    fecha_hasta = fields.Date(_(u'Fecha hasta'), required=False, store=True, compute='_asignar_fechas_aux2')


class contenedor_tipo(models.Model):

    _name = 'contenedor.tipo'
    _description = u'Clase Tipo De Contenedor'
    _rec_name = 'descripcion'

    @api.one
    def eliminar_tipo_contenedor(self):
        self.write({'eliminado': True, })
        return True

    codigo = fields.Char(_(u'Código'), required=True)
    descripcion = fields.Char(_(u'Descripción'), required=True)
    tarifa_demora = fields.Float(_(u'Tarifa Demora'), required = False);
    eliminado = fields.Boolean('Eliminado', default=False)

    _sql_constraints = [
        ('tipo_contenedor_uniq', 'unique(codigo)', 'Error. No puede insertar dos Tipos de Contenedor con mismo código'),
    ]


class contenedor(models.Model):

    _name = 'contenedor'
    _description = u'Clase Contenedor'
    _rec_name = 'numero'
    _order = "fecha_llegada desc"
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    ESTADOS = [('en_camino', 'En Camino'),
               ('en_puerto', 'Full En Puerto'),
               ('despachado', 'En Poder Del Consignatario'),
               ('devuelto', 'Vacío Recibido'),
               ('vacio_exportacion', 'Vacío para exportación'),
               ('full_exportacion', 'Full para exportación'),
               ('embarcado_full', 'Embarcado full'),
               ('embarcado_vacio', 'Embarcado vacio'),
               ('entregado_shiperon', 'En Poder Del Dueño'),
               ('embarcado_shiperon', 'Embarcado Shiperon'), ]

    @api.one
    def get_tipo_material(self):
        materiales = []
        material_tipo = self.pool.get('material')
        material_tipo_ids = material_tipo.search([])
        for material_tipo_id in material_tipo_ids:
            material = material_tipo.browse(material_tipo_id)
            materiales.append((material.descripcion, material.descripcion))
        return materiales

    @api.multi
    def equipo_en_puerto(self):
        self.write({'state': 'en_puerto', })
        return True

    @api.multi
    def equipo_despachado(self):
        self.write({'state': 'despachado', })
        return True

    @api.multi
    def equipo_devuelto(self):
        self.write({'state': 'devuelto', })
        return True

    @api.multi
    def eliminar_contenedor(self):
        self.write({'eliminado': True, })
        return True

    @api.multi
    def equipo_en_camino(self):
        self.write({'state': 'en_camino', })
        return True

    @api.multi
    def equipo_en_demora(self):
        self.write({'state': 'demora', })
        return True

    @api.one
    @api.constrains('fecha_entrega', 'fecha_devolucion', 'fecha_llegada')
    def _check_fechas(self):
        if(self.fecha_entrega and self.fecha_llegada):
            if self.fecha_entrega < self.fecha_llegada:
                raise ValidationError("Fecha De Entrega debe ser mayor o igual a la Fecha De Llegada")
        if(self.fecha_entrega and self.fecha_devolucion):
            if self.fecha_devolucion < self.fecha_entrega:
                raise ValidationError("Fecha De Devolución debe ser mayor o igual a la Fecha De Entrega")

    @api.one
    @api.depends('numero')
    def _obtener_buque(self):
        for rec in self:
            model = self.env['viaje']
            viaje = model.browse([rec.viaje_id.id])
            rec.buque = viaje.buque_id

    @api.one
    @api.depends('fecha_inicio_operaciones', 'dias_libres')
    def _calcular_dias_libres(self):
        # print "Calcular dias libres"
        if self.fecha_inicio_operaciones and self.dias_libres > 0:
            fecha = datetime.strptime(self.fecha_inicio_operaciones, "%Y-%m-%d")
            dias = timedelta(days=self.dias_libres - 1)
            self.fecha_vencen_dias_libres = fecha + dias
        else:
            self.fecha_vencen_dias_libres = ""

    @api.one
    @api.constrains('fecha_entrega', 'fecha_devolucion', 'fecha_llegada')
    def _check_fechas(self):
        if(self.fecha_entrega and self.fecha_llegada):
            if self.fecha_entrega < self.fecha_llegada:
                raise ValidationError("Fecha De Entrega debe ser mayor o igual a la Fecha De Llegada")
        if(self.fecha_entrega and self.fecha_devolucion):
            if self.fecha_devolucion < self.fecha_entrega:
                raise ValidationError("Fecha De Devolución debe ser mayor o igual a la Fecha De Entrega")

    @api.one
    @api.depends('numero')
    def _obtener_buque(self):
        for rec in self:
            model = self.env['viaje']
            viaje = model.browse([rec.viaje_id.id])
            rec.buque = viaje.buque_id

    @api.one
    @api.depends('fecha_llegada', 'fecha_entrega', 'fecha_salida', 'fecha_devolucion')
    def _asignar_fechas_aux(self):
        self.llegada_desde = self.fecha_llegada
        self.llegada_hasta = self.fecha_llegada
        self.entrega_desde = self.fecha_entrega
        self.entrega_hasta = self.fecha_entrega
        self.salida_desde = self.fecha_salida
        self.salida_hasta = self.fecha_salida
        self.devolucion_desde = self.fecha_devolucion
        self.devolucion_hasta = self.fecha_devolucion

    def equipo_demora(self, cr, uid, context=None):
        contenedores = self.pool.get('contenedor')
        contenedores_ids = contenedores.search(cr, uid, [('state', '!=', 'embarcado_vacio'), ('state', '!=', 'embarcado_full'),
                                                ('state', '!=', 'embarcado_shiperon')])
        for contenedor_id in contenedores_ids:
            contenedor = contenedores.browse(cr, uid, contenedor_id, context=context)
            if contenedor.fecha_inicio_operaciones != False:
                if contenedor.fecha_salida != False:
                    fecha_inicio = datetime.strptime(contenedor.fecha_inicio_operaciones, "%Y-%m-%d")
                    fecha_salida_aux = datetime.strptime(contenedor.fecha_salida, "%Y-%m-%d")
                    dias_pais = fecha_salida_aux - fecha_inicio
                    contenedor.dias_en_pais = dias_pais.days
                elif not contenedor.fecha_salida != False:
                    hoy = datetime.today()
                    hoy = hoy.replace(hour=0, minute=0, second=0, microsecond=0)
                    fecha_inicio = datetime.strptime(contenedor.fecha_inicio_operaciones, "%Y-%m-%d")
                    dias_pais = hoy - fecha_inicio
                    contenedor.dias_en_pais = dias_pais.days

                if contenedor.fecha_devolucion == False and contenedor.fecha_vencen_dias_libres != False:
                    hoy = datetime.today()
                    hoy = hoy.replace(hour=0, minute=0, second=0, microsecond=0)
                    vencimiento = datetime.strptime(contenedor.fecha_vencen_dias_libres, "%Y-%m-%d")
                    if hoy > vencimiento:
                        dem = hoy - vencimiento
                        contenedor.demora = True
                        contenedor.dias_demora = dem.days
                if contenedor.fecha_devolucion != False and contenedor.fecha_vencen_dias_libres != False:
                    contenedor.demora = False
                    vencimiento = datetime.strptime(contenedor.fecha_vencen_dias_libres, "%Y-%m-%d")
                    devolucion = datetime.strptime(contenedor.fecha_devolucion, "%Y-%m-%d")
                    if devolucion > vencimiento:
                        dem = devolucion - vencimiento
                        contenedor.dias_demora = dem.days
        return True

    @api.one
    @api.depends('numero', 'no_bl')
    def _set_clave(self):
        self.clave = '{0}{1}'.format(self.numero, self.no_bl.no_bl)

    @api.one
    @api.depends('numero')
    def _obtener_cliente(self):
        for rec in self:
            model = self.env['bl']
            bl = model.browse([rec.no_bl.id])
            rec.customers = bl.customers

    @api.one
    @api.depends('numero')
    def _obtener_partner(self):
        for rec in self:
            model = self.env['bl']
            bl = model.browse([rec.no_bl.id])
            rec.cliente = bl.cliente

    @api.one
    @api.depends('numero')
    def _obtener_exoneracion(self):
        for rec in self:
            model = self.env['bl']
            bl = model.browse([rec.no_bl.id])
            rec.exonerado = bl.exonerado

    @api.one
    @api.depends('numero')
    def _obtener_puerto_llegada(self):
        for rec in self:
            model = self.env['viaje']
            viaje = model.browse([rec.viaje_id.id])
            rec.puerto_llegada = viaje.puerto_arribo

    no_bl = fields.Many2one('bl', _(u'BL'), required=True,
                            domain=[('eliminado', '=', False)])
    no_booking = fields.Many2one('booking', _(u'Booking'), required=False, readonly=True,
                                 domain=[('eliminado', '=', False)])
    numero = fields.Char(_(u'Número'), required=True)
    no_precinto = fields.Char(_(u'Precinto'), required=False)
    no_precinto2 = fields.Char(_(u'Precinto 2'), required=False)
    no_precinto3 = fields.Char(_(u'Precinto 3'), required=False)
    tipo = fields.Many2one('contenedor.tipo', _(u'Tipo'), required=False,
                           domain=[('eliminado', '=', False)])
    peso = fields.Char(_(u'Peso'), required=False)
    observaciones = fields.Text(_(u'Obs.'), required=False)
    viaje_id = fields.Many2one('viaje', _(u'Viaje Llegada'), required=False,
                               domain=[('eliminado', '=', False)])
    image = fields.Binary("Image")
    customers = fields.Many2one('beneficiario', _(u'Beneficiario'), store=True, compute='_obtener_cliente')
    cliente = fields.Many2one('res.partner', _(u'Cliente'), store=True, compute='_obtener_partner')
    state = fields.Selection(ESTADOS, 'Status', store=True, readonly=True, default="en_camino")
    eliminado = fields.Boolean('Eliminado', default=False)
    operativo = fields.Boolean('Op.', default=True)
    demora = fields.Boolean('Demora', default=False, readonly=True)
    dias_libres = fields.Integer(_(u'Días Libres'), required=False, default=10)
    fecha_llegada = fields.Date(_(u'Llegada'), required=False, store=True, readonly=True)
    fecha_inicio_operaciones = fields.Date(_(u'Inicio Operaciones'), required=False, store=True, readonly=True)
    fecha_entrega = fields.Date(_(u'Despacho'), required=False, store=True, readonly=True)
    fecha_salida = fields.Date(_(u'Salida'), required=False, store=True, readonly=True)
    fecha_vencen_dias_libres = fields.Date(_(u'Vencimiento'), required=False,
                                           store=True, compute='_calcular_dias_libres')
    fecha_devolucion = fields.Date(_(u'Devolución'), required=False, store=True, readonly=True)
    puerto_actual = fields.Many2one('puerto', _(u'Puerto'), required=False, store=True, readonly=True)
    patio = fields.Many2one('patio', _(u'Patio'), required=False, store=True, readonly=True)
    eir = fields.Char(_(u'EIR'), required=False, store=True, readonly=True)
    buque = fields.Many2one('buque', _(u'Buque Llegada'), store=True, compute='_obtener_buque')
    movimiento_contenedor_id = fields.One2many('contenedor.movimiento', 'contenedor_id',
                                               string=_(u'Movimientos'), readonly=False)
    llegada_desde = fields.Date(_(u'Llegada desde'), required=False, store=True, compute='_asignar_fechas_aux')
    llegada_hasta = fields.Date(_(u'Llegada hasta'), required=False, store=True, compute='_asignar_fechas_aux')
    entrega_desde = fields.Date(_(u'Entrega desde'), required=False, store=True, compute='_asignar_fechas_aux')
    entrega_hasta = fields.Date(_(u'Entrega hasta'), required=False, store=True, compute='_asignar_fechas_aux')
    salida_desde = fields.Date(_(u'Embarque desde'), required=False, store=True, compute='_asignar_fechas_aux')
    salida_hasta = fields.Date(_(u'Embarque hasta'), required=False, store=True, compute='_asignar_fechas_aux')
    devolucion_desde = fields.Date(_(u'Devolución desde'), required=False, store=True, compute='_asignar_fechas_aux')
    devolucion_hasta = fields.Date(_(u'Devolución hasta'), required=False, store=True, compute='_asignar_fechas_aux')
    clave = fields.Char(_(u'Clave'), required=False, store=True, compute='_set_clave')
    buque_salida = fields.Many2one('buque', _(u'Buque Salida'), readonly=True)
    viaje_salida = fields.Many2one('viaje', _(u'Viaje Salida'), required=False,
                                   domain=[('eliminado', '=', False)], readonly=True)
    dias_demora = fields.Integer(_(u'Días Demora'), required=False, default=0, readonly=True)
    dias_en_pais = fields.Integer(_(u'Días En El País'), required=False, default=0, readonly=True)
    puerto_llegada = fields.Many2one('puerto', _(u'Puerto Arribo'), compute='_obtener_puerto_llegada', store=True)
    exonerado = fields.Boolean('Exonerado', default=False, compute='_obtener_exoneracion', store=True)

    _sql_constraints = [
        ('contenedor_uniq', 'unique(clave)',
         'Error. No puede insertar dos contenedores con misma combinación de Número y BL'),
    ]
