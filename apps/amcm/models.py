# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - AriSan - FusionTI
"""

from django.db import models
from django.forms.models import model_to_dict
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField, GroupedForeignKey
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.query_utils import Q
# Catalogs Models

#catalogo para descuentos

class Descuentos(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False, blank=False, unique=True)
    descripcion = models.CharField(verbose_name="Descripción", max_length=255, null=False, blank=False)
    porcentaje = models.FloatField(verbose_name='Porcentaje', blank=False, null=False, default=0)

    class Meta:
        ordering = ['nombre']
        verbose_name = "Descuento"
        verbose_name_plural = "Descuentos"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['descripcion'] = str(self.descripcion)
        dict['porcentaje'] = str(self.porcentaje)
        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


#catalogo para tipo de evento
class TipoEvento(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False, blank=False, unique=True)
    descripcion = models.CharField(verbose_name="Descripción", max_length=255, null=False, blank=False)

    class Meta:
        ordering = ['nombre']
        verbose_name = "Tipo de Evento"
        verbose_name_plural = "Tipos de Evento"

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['descripcion'] = str(self.descripcion)
        return dict


#catalogo para estatus de ejemplares
class EstatusEjemplar(models.Model):
    nombre = models.CharField(verbose_name="Estatus", max_length=100, null=False, blank=False, unique=True)
    descripcion = models.CharField(verbose_name="Descripción", max_length=255, null=False, blank=False)

    class Meta:
        ordering = ['nombre']
        verbose_name = "Estatus de Ejemplar"
        verbose_name_plural = "Estatus de Ejemplares"

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['descripcion'] = str(self.descripcion)
        return dict


#catalogo para tipo de cuotas
class TipoCuota(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False, blank=False, unique=True)
    descripcion = models.CharField(verbose_name="Descripción", max_length=255, null=False, blank=False)

    class Meta:
        ordering = ['nombre']
        verbose_name = "Tipo de Cuota"
        verbose_name_plural = "Tipos de Cuotas"

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['descripcion'] = str(self.descripcion)
        return dict


#catalogo para tipo de condiciones
class TipoCondicion(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False, blank=False, unique=True)
    descripcion = models.CharField(verbose_name="Descripción", max_length=255, null=False, blank=False)

    class Meta:
        ordering = ['nombre']
        verbose_name = "Limite "
        verbose_name_plural = "Limite"

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['descripcion'] = str(self.descripcion)
        return dict


#catalogo para tipo de cuotas
class Limite(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False, blank=False, unique=True)
    descripcion = models.CharField(verbose_name="Descripción", max_length=255, null=False, blank=False)

    class Meta:
        ordering = ['nombre']
        verbose_name = "Tipo de Condición"
        verbose_name_plural = "Tipo de Condiciones"

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['descripcion'] = str(self.descripcion)
        return dict


#catalogo para cuotas
class Cuotas(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False, blank=False, unique=True)
    descripcion = models.CharField(verbose_name="Descripción", max_length=255, null=False, blank=False)
    monto = models.FloatField(verbose_name='Monto', blank=False, null=False, default=0)
    tipoCuota = models.ForeignKey('TipoCuota', verbose_name="Tipo de Cuota", null=False, blank=False, on_delete=models.CASCADE,)




    class Meta:
        ordering = ['nombre']
        verbose_name = "Cuota"
        verbose_name_plural = "Cuotas"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['descripcion'] = str(self.descripcion)
        dict['monto'] = str(self.monto)
        dict['tipoCuota'] = self.tipoCuota
        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


#catalogo para cuotas de los eventos

class CondicionesEvento(models.Model):
    limite = models.ForeignKey('Limite', verbose_name='Tipo de Condición', null=False, blank=False, on_delete=models.CASCADE,)
    tipoCondicion = models.ForeignKey('TipoCondicion', verbose_name="Límite", null=False, blank=False, on_delete=models.CASCADE,)
    valor = models.FloatField(verbose_name="Valor", null=False, blank=False, default=0)
    especificacion = models.CharField(verbose_name="Especificación de la Condición", null=False, blank=True, max_length=500, )
    evento = models.ForeignKey('Evento', verbose_name='Evento', null=False, blank=False, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Condición del Evento"
        verbose_name_plural = "Condiciones del Evento"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['limite'] = self.limite.nombre
        dict['tipoCondicion'] = self.tipoCondicion.nombre
        dict['valor'] = self.valor
        dict['especificacion'] = self.especificacion
        return dict

    def __str__(self):
        return self.tipoCondicion.nombre

    def __unicode__(self):
        return self.tipoCondicion.nombre


#catalogo para cuotas de los eventos
class CuotaEvento(models.Model):
    monto = models.FloatField(verbose_name='Monto', blank=False, null=False, default=0)
    tipoCuota = models.ForeignKey('TipoCuota', verbose_name="Tipo de Cuota", null=False, blank=False, on_delete=models.CASCADE,)
    fechaVencimiento = models.DateField(verbose_name="Fecha de Vencimiento", blank=False, null=False,)
    evento = models.ForeignKey('Evento', blank=False, null=False, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Cuota"
        verbose_name_plural = "Cuotas"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['fechaVencimiento'] = self.fechaVencimiento
        dict['monto'] = str(self.monto)
        dict['tipoCuota'] = self.tipoCuota
        return dict

    def __str__(self):
        return self.tipoCuota.nombre + ' - $ ' + str(self.monto)

    def __unicode__(self):
        return self.tipoCuota.nombre + ' - $ ' + str(self.monto)


#catalogo para tipoFechas

class TipoFecha(models.Model):
    nombre = models.CharField(verbose_name='Nombre', blank=False, null=False, max_length=500,)
    descripcion = models.CharField(verbose_name='Descripción', blank=False, null=False, max_length=500,)

    class Meta:
        verbose_name = "Tipo de Fecha del Evento"
        verbose_name_plural = "Tipos de Fechas del Evento"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['descripcion'] = str(self.descripcion)
        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


#modelo para fechas del evento

class FechasEvento(models.Model):
    tipoFecha = models.ForeignKey('TipoFecha', verbose_name='Tipo de Fecha', blank=False, null=False, default=0, on_delete=models.CASCADE,)
    fecha = models.DateField( verbose_name="Fecha de Vencimiento",  blank=False, null=False,)
    evento = models.ForeignKey('Evento', verbose_name='Evento', blank=False, null=False,  on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Fechas del Evento"
        verbose_name_plural = "Fechas del Evento"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['tipoFecha'] = str(self.tipoFecha)
        dict['fecha'] = self.fecha
        return dict

    def __str__(self):
        return self.tipoFecha.nombre

    def __unicode__(self):
        return self.tipoFecha.nombre


#modelo para Cuentas Contables  del evento

class CuentasEvento(models.Model):
    cuenta = models.ForeignKey('CuentasContables', verbose_name='Cuenta Contable', blank=False, null=False, default=0, on_delete=models.CASCADE,)
    evento = models.ForeignKey('Evento', verbose_name='Evento', blank=False, null=False,  on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Cuentas Contables del Evento"
        verbose_name_plural = "Cuentas Contables del Evento"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['cuenta'] = self.cuenta
        dict['evento'] = self.evento
        return dict

    def __str__(self):
        return self.cuenta.nombre

    def __unicode__(self):
        return self.cuenta.nombre



#catalogo para tipo de cuotas
class Sexo(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = "Sexo"
        verbose_name_plural = "Sexos"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


# catalogo para tipo de cuotas
class Nacionalidad(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False, blank=False, unique=True)
    abreviatura = models.CharField(verbose_name="Abreviatura", max_length=100, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = "Nacionalidad"
        verbose_name_plural = "Nacionalidades"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['abreviatura'] = str(self.abreviatura)
        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


# catalogo para cuentas contables
class CuentasContables(models.Model):
    codigo = models.IntegerField(verbose_name="Código", null=False, blank=False)
    nombre = models.CharField(verbose_name="Nombre", max_length=200, null=False, blank=False, unique=True)

    ACTIVA = 'ACTIVA'
    INACTIVA = 'INACTIVA'
    STATUS_CHOICES = (
        (ACTIVA, 'ACTIVA'),
        (INACTIVA, 'INACTIVA'),
    )
    estatus = models.CharField(max_length=15, choices=STATUS_CHOICES, default=ACTIVA,
                              verbose_name="Estatus de Cuenta")

    class Meta:
        ordering = ['nombre']
        verbose_name = "Cuenta Contable"
        verbose_name_plural = "Cuentas Contables"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['estatus'] = str(self.estatus)
        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre



# Modelo de Cuadras
class Cuadras(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=200, null=False, blank=False)
    representante = models.CharField(verbose_name="Representante", max_length=150, null=False, blank=False)
    telefono = models.CharField(verbose_name="Teléfono", max_length=15, null=False, blank=True)
    celular = models.CharField(verbose_name="Celular", max_length=15, null=False, blank=True)
    correoElectronico = models.CharField(verbose_name="Correo Electrónico", max_length=100, null=False, blank=True)
    observaciones = models.TextField(verbose_name="Observaciones", max_length=500, null=False, blank=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = "Cuadra"
        verbose_name_plural = "Cuadras"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['representante'] = str(self.representante)
        dict['telefono'] = str(self.telefono)
        dict['celular'] = str(self.celular).strip()
        dict['correoElectronico'] = self.correoElectronico
        dict['observaciones'] = str(self.observaciones)

        # datos para el modelo de fechas
        contactos = []
        for obj in self.contacto_set.all():
            det = obj.to_serializable_dict()
            contactos.append(det)
        dict['contactos'] = contactos

        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


#Catalogo de ejemplares
class Ejemplares(models.Model):
    lote = models.IntegerField(verbose_name="Lote", unique=True,blank=False,null=False)
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False, blank=False)
    edad = models.FloatField(verbose_name="Edad", blank=False, null=False, default=0)
    peso = models.FloatField(verbose_name='Peso', blank=False, null=False, default=0)
    sexo = models.ForeignKey(Sexo, verbose_name="Sexo", null=False, blank=False,on_delete=models.CASCADE,)
    nacionalidad = models.ForeignKey(Nacionalidad, verbose_name="Nacionalidad", null=False, blank=False,on_delete=models.CASCADE,)
    color = models.CharField(verbose_name="Color", max_length=100, null=False, blank=False)
    padre = models.CharField(verbose_name="Padre del Caballo", max_length=100, null=False, blank=False)
    madre = models.CharField(verbose_name="Madre del Caballo", max_length=100, null=False, blank=False)
    estatus = models.ForeignKey(EstatusEjemplar, verbose_name="Estatus del Ejemplar", null=False, blank=False, on_delete=models.CASCADE,)
    observaciones = models.TextField(verbose_name="Observaciones", max_length=500, null=False, blank=False)

    cuadra = models.ForeignKey(Cuadras, verbose_name="Cuadra", null=False, blank=False,on_delete=models.CASCADE,)

    class Meta:
        #ordering = ['nombre']
        verbose_name = "Ejemplar"
        verbose_name_plural = "Ejemplares"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['lote'] = str(self.lote)
        dict['nombre'] = str(self.nombre)
        dict['edad'] = str(self.edad)
        dict['peso'] = str(self.peso)
        dict['sexo'] = self.sexo.nombre
        dict['nacionalidad'] = self.nacionalidad.nombre
        dict['color'] = str(self.color)
        dict['padre'] = str(self.padre)
        dict['madre'] = str(self.madre)
        dict['cuadra'] = str(self.cuadra.nombre)
        dict['estatus'] = str(self.estatus)

        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


# Modelo de Registro de Evento
class Evento(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False, blank=False)
    yardas = models.IntegerField(verbose_name="Distancia (yardas)", null=False, blank=False)
    descripcion = models.CharField(verbose_name="Descripción", max_length=500, null=False, blank=False)

    bolsa = models.FloatField(verbose_name="Bolsa", null=False, blank=False)
    fondo = models.FloatField(verbose_name="Fondo",  null=False, blank=False)
    temporada = models.IntegerField(verbose_name="Temporada",  null=False, blank=False)
    observaciones = models.TextField(verbose_name="Observaciones", max_length=500, null=False, blank=True)

    tipoEvento = models.ForeignKey(TipoEvento, verbose_name="Tipo de Evento", null=False, blank=False, on_delete=models.CASCADE,)
    #fechasEvento = models.ForeignKey(FechasEvento, verbose_name="Fechas del Evento", null=False, blank=False, on_delete=models.CASCADE,)
    descuento = models.ForeignKey(Descuentos, verbose_name="Descuento", null=True, blank=True, on_delete=models.CASCADE,)
    #condicionesEvento = models.ForeignKey(CondicionesEvento, verbose_name="Condiciones del Evento", null=False, blank=False, on_delete=models.CASCADE,)

    elegibles_evento = models.ForeignKey('self', verbose_name='Elegibles de Evento ', null=True, blank=True,on_delete=models.CASCADE,)
    elegibles_subasta = models.ForeignKey('Elegible', verbose_name='Elegibles de Subasta ', null=True, blank=True,
                                         on_delete=models.CASCADE, )

    class Meta:
        ordering = ['nombre']
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['yardas'] = str(self.yardas)
        dict['bolsa'] = str(self.bolsa)
        dict['fondo'] = str(self.fondo)
        dict['temporada'] = str(self.temporada)
        dict['observaciones'] = self.observaciones
        dict['tipoEvento'] = self.tipoEvento
        #dict['fechaEvento'] = self.fechasEvento
        dict['descuento'] = self.descuento.nombre

        # datos para el modelo de fechas
        fechasevento = []
        for obj in self.fechasevento_set.all():
            det = obj.to_serializable_dict()
            fechasevento.append(det)
        dict['fechas_evento'] = fechasevento

        # datos para el modelo de cuotas
        cuotasevento = []
        for obj in self.cuotaevento_set.all():
            det = obj.to_serializable_dict()
            cuotasevento.append(det)
        dict['cuotas_evento'] = cuotasevento

        # datos para el modelo de condiciones
        condicionesevento = []
        for obj in self.condicionesevento_set.all():
            det = obj.to_serializable_dict()
            condicionesevento.append(det)
        dict['condiciones_evento'] = condicionesevento

        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

    def save(self, *args, **kwargs):


        if self.elegibles_evento != None:
            elegibles = ListadoElegibles.objects.filter(id=self.elegibles_evento)
        else:
            elegibles = ListadoElegibles.objects.filter(elegible_id=self.elegibles_subasta)
            elegible_obj = Elegible.objects.get(id=self.elegibles_subasta.id)

        for obj in elegibles:
            # datos del ejemplar
            ejemplares = obj.ejemplar.all()
            for ejemplar in ejemplares:
                eventoelegible = EventoElegibles()
                eventoelegible.evento = self
                eventoelegible.estaus = False
                eventoelegible.cuadra = obj.cuadra
                eventoelegible.ejemplar = ejemplar
                eventoelegible.elegible = elegible_obj
                eventoelegible.save()

        super(Evento, self).save(*args, **kwargs)


# Modelo de Registro de inscripción
class inscripcion(models.Model):
    evento = models.ForeignKey(Evento, verbose_name="Evento", null=False, blank=False, on_delete=models.CASCADE,)
    cuadra = models.ForeignKey(Cuadras, verbose_name="Cuadra", null=False, blank=False, on_delete=models.CASCADE,)
    ejemplar = ChainedForeignKey(Ejemplares,
                               chained_field="cuadra",
                               chained_model_field="cuadra",
                               show_all=False,
                               auto_choose=True,
                               sort=True,
                               null=True,
                               blank=True)
    #ejemplares = models.ManyToManyField(Ejemplares, verbose_name='Ejemplares', null=False, blank=False,)
    fechaRegistro = models.DateField(auto_now=True, verbose_name='Fecha de Registro')

    ACTIVO = 'ACTIVO'
    RETIRADO = 'RETIRADO'
    STATUS_CHOICES = (
        (ACTIVO, 'ACTIVO'),
        (RETIRADO, 'RETIRADO'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=ACTIVO,
                              verbose_name="Estatus de inscripción")


    class Meta:
        ordering = ['evento']
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['evento'] = self.evento
        dict['cuadra'] = self.cuadra
        dict['ejemplar'] =self.ejemplar
        dict['fecharegistro'] = str(self.fechaRegistro)

        return dict

    def __str__(self):
        return self.evento.nombre + ' ' + self.cuadra.nombre

    def __unicode__(self):
        return self.evento.nombre + ' ' + self.cuadra.nombre


# Modelo de Registro de Cuota de Evento
class Pago(models.Model):
    evento = models.ForeignKey(Evento, verbose_name="Evento", null=False, blank=False, on_delete=models.CASCADE,)

    cuota = ChainedForeignKey(CuotaEvento,
                                 chained_field="evento",
                                 chained_model_field="evento",
                                 show_all=False,
                                 auto_choose=True,
                                 sort=True,
                                 null=True,
                                 blank=True,
                                )

    cuadra = models.ForeignKey(Cuadras, verbose_name="Cuadra", null=False, blank=False, on_delete=models.CASCADE, )
    ejemplar = ChainedManyToManyField(Ejemplares,
                                      chained_field="cuadra",
                                      chained_model_field="cuadra",
                                      related_name='ejemplar_related_fields',
                                      horizontal=False,
                                      null=True,
                                      blank=True,
                                      limit_choices_to={"estatus__nombre": 'ACTIVO'})

    cuotaPagada = models.FloatField(verbose_name='Monto Recibido', null=False, blank=False,)
    #cuotaLetra = models.CharField(verbose_name="Cuota en Letra", null=False, blank=False, max_length=500,)
    conceptoPago = models.CharField(verbose_name="Concepto del Pago", null=False, blank=False, max_length=250,)
    fechaPago = models.DateField(verbose_name='Fecha del Pago' ,null=True, blank=True, editable=True,default=now())
    fechaRegistro = models.DateField(verbose_name='Fecha de Registro',null=False, blank=False, editable=True,default=now())
    #numeroRecibo = models.IntegerField(verbose_name= "Recibo", null=False, blank=False,)
    # valorRecibido = models.CharField(verbose_name="Valor Recibido En ...:", null=False, blank=False, max_length=500 ) se elimina campo por Forma PAgo inlines

    PAGADO = 'PAGADO'
    CREDITO = 'CREDITO'
    PENDIENTE = 'PENDIENTE'
    PAGO_CHOICES = (
        (PAGADO, 'PAGADO'),
        (CREDITO, 'CREDITO'),
    )
    estatus_credito = models.CharField(max_length=15, choices=PAGO_CHOICES, default=PAGADO,
                              verbose_name="Estatus del Pago")

    PAGO_CUOTA_CHOICES = (
        (PAGADO, 'PAGADO'),
        (PENDIENTE, 'PENDIENTE'),
    )
    estatus_cuota = models.CharField(max_length=15, choices=PAGO_CUOTA_CHOICES, default=PAGADO,
                                       verbose_name="Estatus de Pago de Cuota")

    class Meta:
        #ordering = ['evento']
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['cuota'] = str(self.cuota.tipoCuota.nombre)
        dict['evento'] = str(self.evento.nombre)
        dict['cuotaPagada'] = str(self.cuotaPagada)
        dict['cuotaLetra'] = ""
        dict['conceptoPago'] = str(self.conceptoPago)
        dict['fechaPago'] = str(self.fechaPago)
        dict['fechaRegistro'] = str(self.fechaRegistro)
        dict['valorRecibido'] = str(self.valorRecibido)

        return dict

    def __str__(self):
        cadena=''
        for obj in self.ejemplar.all():
            cadena+=obj.nombre + ' '
        return str(self.evento.nombre) + ' ' + str(self.cuota.tipoCuota.nombre) + ' '+ cadena

    def __unicode__(self):
        cadena = ''
        for obj in self.ejemplar.all():
            cadena += obj.nombre + ' '
        return str(self.evento.nombre) + ' ' + str(self.cuota.tipoCuota.nombre) +' ' + cadena

    def save(self, *args, **kwargs):
        canSave = True

        super(Pago, self).save(*args, **kwargs)



@receiver(post_save, sender=Pago, dispatch_uid='save_credito')
def save_credito(sender, instance, **kwargs):
    print(instance)
    try:
        existe = Credito.objects.get(pago=instance)
        if instance.estatus_credito=='PAGADO':
            existe.pagado='SI'
            existe.fecha_pago=now()
            existe.save()
    except Credito.DoesNotExist:
        if instance.estatus_credito=='CREDITO':
            credito = Credito(pago=instance, importe=instance.cuotaPagada, fecha_registro=now(), pagado='NO',fecha_pago=None)
            credito.save()



    #     project_section.save()
    # # Creating the sections for each saved project.
    # saved_section = Pago.objects.filter(Q(project=instance) & Q(section=section))
    #
    # # If no record was found for the specific section.
    # if not saved_section.exists():
    #     project_section = ProjectSections(project=instance, section=section, last_edit_date=now(), status=1)
    #     print "Saving..."
    #     project_section.save()


# Modelo de Registro Tipo de Forma de Pago
class FormaPago(models.Model):
    nombre = models.CharField(verbose_name="Nombre", null=False, blank=False, max_length=50)
    descripcion = models.CharField(verbose_name='Descripción', null=True, blank=True, max_length=250)

    class Meta:
        #ordering = ['evento']
        verbose_name = "Forma de Pago"
        verbose_name_plural = "Formas de Pago"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['descripcion'] = str(self.descripcion)

        return dict

    def __str__(self):
        return str(self.nombre)

    def __unicode__(self):
        return str(self.nombre)


# registro de montos asignados a la cuenta contable de un PAgo
class CuentasPago(models.Model):
    pago = models.ForeignKey(Pago, verbose_name="Pago", null=False, blank=False,on_delete=models.CASCADE,)
    cuenta = models.ForeignKey(CuentasEvento, verbose_name="Cuenta Contable", null=False, blank=False,on_delete=models.CASCADE, )
    importe = models.FloatField(verbose_name='Importe', blank=False, null=False, default=0)
    fecha_registro = models.DateField(verbose_name='Fecha de Registro', null=False, blank=False, editable=True,default=now())


    class Meta:
        verbose_name = "Cuenta - Pago"
        verbose_name_plural = "Cuentas - Pago"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['fecha_registro'] = str(self.fecha_registro)
        return dict

    def __str__(self):
        return self.cuenta.cuenta.nombre

    def __unicode__(self):
        return self.cuenta.cuenta.nombre


# modelo para Nombre de Listado para elegibles
class Elegible(models.Model):
    nombre = models.CharField(verbose_name="Nombre", null= False, blank= False, max_length = 250)
    fecha_registro = models.DateField(verbose_name='Fecha de registro', null=False, blank=False, editable=True,default=now())

    class Meta:
        verbose_name = "Elegible"
        verbose_name_plural = "Elegibles"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = self.nombre
        dict['fecharegistro'] = self.fecha_registro
        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


# modelo para listado de elegibles
class ListadoElegibles(models.Model):
    cuadra = models.ForeignKey(Cuadras, verbose_name="Cuadra", null=False, blank=False, on_delete=models.CASCADE, )
    ejemplar = ChainedManyToManyField(Ejemplares,
                                      chained_field="cuadra",
                                      chained_model_field="cuadra",
                                      related_name='ejemplar_related_elegible',
                                      horizontal=False,
                                      null=True,
                                      blank=True,
                                      limit_choices_to={"estatus__nombre": 'ACTIVO'})
    elegible = models.ForeignKey(Elegible, null=False, blank=False, on_delete= models.CASCADE, )

    class Meta:
        verbose_name = "Listado de Elegibles"
        verbose_name_plural = "Listados de Elegibles"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['cuadra'] = self.cuadra
        dict['ejemplar'] = self.ejemplar
        dict['elegible'] = self.elegible
        return dict

    def __str__(self):
        return self.cuadra.nombre

    def __unicode__(self):
        return self.cuadra.nombre


# modelo para listado de elegibles
class EventoElegibles(models.Model):
    cuadra = models.ForeignKey(Cuadras, verbose_name="Cuadra", null=False, blank=False, on_delete=models.CASCADE, )
    ejemplar = ChainedForeignKey(Ejemplares,
                                      chained_field="cuadra",
                                      chained_model_field="cuadra",
                                      related_name='ejemplar_elegible',
                                      null=True,
                                      blank=True,
                                      limit_choices_to={"estatus__nombre": 'ACTIVO'})
    estaus = models.BooleanField(verbose_name='Retirado',default=False, null=False)
    elegible = models.ForeignKey(Elegible, null=False, blank=False, on_delete= models.CASCADE, )
    evento = models.ForeignKey(Evento, null=False, blank=False, on_delete= models.CASCADE, )

    class Meta:
        verbose_name = "Elegibles para Evento"
        verbose_name_plural = "Elegibles para Evento"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['cuadra'] = self.cuadra
        dict['ejemplar'] = self.ejemplar
        dict['estatus'] = self.estaus
        dict['elegible'] = self.elegible
        return dict

    def __str__(self):
        return self.cuadra.nombre

    def __unicode__(self):
        return self.cuadra.nombre


#modelo registro de contactos
class Contacto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", null= False, blank= False, max_length= 200)
    telefono = models.CharField(verbose_name="Teléfono", max_length=15, null=True, blank=True)
    cuadra = models.ForeignKey(Cuadras, verbose_name="Cuadra", null=False, blank=False, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = self.nombre
        dict['telefono'] = self.telefono
        dict['cuadra'] = self.cuadra

        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


# registro de formas de pago  de un Pago
class ReferenciaFormaPago(models.Model):
    pago = models.ForeignKey(Pago, verbose_name="Pago", null=False, blank=False, on_delete=models.CASCADE, )
    formapago = models.ForeignKey(FormaPago, verbose_name="Forma de Pago", null=False, blank=False,on_delete=models.CASCADE,)
    referencia = models.CharField(verbose_name="Referencia", null= False, blank= False, max_length= 100)
    importe = models.FloatField(verbose_name='Importe', blank=False, null=False, default=0)


    class Meta:
        verbose_name = "Forma - Pago"
        verbose_name_plural = "Formas - Pago"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['formapago'] = self.formapago
        dict['referencia'] = self.referencia
        dict['importe'] = self.importe

        return dict

    def __str__(self):
        return self.referencia

    def __unicode__(self):
        return self.referencia


# Modelo de Registro recibos
class Recibo(models.Model):
    pago = models.ForeignKey(Pago, verbose_name="Pago", null=False, blank=False, on_delete=models.CASCADE,)
    numero_recibo = models.IntegerField(verbose_name= "Número de Recibo", null=False, blank=False, unique=True)
    observaciones = models.CharField(verbose_name="Observaciones", null=True, blank=True, max_length=500 )
    fecha_registro = models.DateField(verbose_name='Fecha de registro', null=False, blank=False, editable=True,default=now())

    class Meta:
        #ordering = ['evento']
        verbose_name = "Recibo"
        verbose_name_plural = "Recibos"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['Pago'] = str(self.pago.evento.nombre) +' - ' +str(self.pago.cuota.tipoCuota.nombre)
        dict['cuadra'] = str(self.pago.cuadra.nombre)

        return dict

    def __str__(self):
        return str(self.pago.evento.nombre) + ' ' + str(self.numero_recibo)

    def __unicode__(self):
        return str(self.pago.evento.nombre) + ' ' + str(self.numero_recibo)


# modelo reasignacion de cuadra
class ReasignaEjemplar(models.Model):
    ejemplar =  models.ForeignKey(Ejemplares, verbose_name="Ejemplar", null=False, blank=False, on_delete=models.CASCADE,)
    cuadra = models.ForeignKey(Cuadras, verbose_name="Cuadra", null=False, blank=False, on_delete=models.CASCADE,)


# Modelo de Registro CRÉDITO
class Credito(models.Model):
    pago = models.ForeignKey(Pago, verbose_name="Pago", null=False, blank=False, on_delete=models.CASCADE,)
    importe = models.FloatField(verbose_name='Importe', null=False, blank=False,)
    fecha_registro = models.DateField(verbose_name='Fecha de registro', null=False, blank=False, editable=True,default=now())
    fecha_pago = models.DateField(verbose_name='Fecha de pago', null=True, blank=True, editable=True,
                                      default=now())
    SI = 'SI'
    NO = 'NO'
    ESTATUS_CHOICES = (
        (SI, 'SI'),
        (NO, 'NO'),
    )
    pagado = models.CharField(max_length=15, choices=ESTATUS_CHOICES, default=NO,
                                       verbose_name="Pagado?")

    class Meta:
        #ordering = ['evento']
        verbose_name = "Crédito"
        verbose_name_plural = "Créditos"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['Pago'] = str(self.pago.evento.nombre) +' - ' +str(self.pago.cuota.tipoCuota.nombre)
        dict['cuadra'] = str(self.pago.cuadra.nombre)

        return dict

    def __str__(self):
        return str(self.pago.evento.nombre) + ' ' + str(self.pago.cuadra.nombre)

    def __unicode__(self):
        return str(self.pago.evento.nombre) + ' ' + str(self.pago.cuadra.nombre)

