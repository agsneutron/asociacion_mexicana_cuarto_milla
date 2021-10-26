# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - AriSan - FusionTI
"""

from django.db import models
from django.forms.models import model_to_dict
from smart_selects.db_fields import ChainedForeignKey

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


#catalogo para tipo de cuotas
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
        verbose_name = "Tipo de Condición"
        verbose_name_plural = "Tipos de Condiciones"

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
        verbose_name = "límite de Condición"
        verbose_name_plural = "límites de Condiciones"

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
    limite = models.ForeignKey('Limite', verbose_name='Limite', null=False, blank=False, on_delete=models.CASCADE,)
    tipoCondicion = models.ForeignKey('TipoCondicion', verbose_name="Tipo de Condición", null=False, blank=False, on_delete=models.CASCADE,)
    valor = models.FloatField(verbose_name="Valor", null=False, blank=False, default=0)
    especificacion = models.CharField(verbose_name="Especificación de la Condición", null=False, blank=True, max_length=500, )
    evento = models.ForeignKey('Evento', verbose_name='Evento', null=False, blank=False, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Condición del Evento"
        verbose_name_plural = "Condiciones del Evento"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['limite'] = self.limite
        dict['tipoCondicion'] = self.tipoCondicion
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
        dict['fechaVencimiento'] = str(self.fechaVencimiento)
        dict['monto'] = str(self.monto)
        dict['tipoCuota'] = self.tipoCuota
        return dict

    def __str__(self):
        return self.tipoCuota.nombre

    def __unicode__(self):
        return self.tipoCuota.nombre


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
        dict['fecha'] = str(self.fecha)
        return dict

    def __str__(self):
        return self.tipoFecha.nombre

    def __unicode__(self):
        return self.tipoFecha.nombre



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


# Modelo de Cuadras
class Cuadras(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=200, null=False, blank=False)
    representante = models.CharField(verbose_name="Representante", max_length=150, null=False, blank=False)
    telefono = models.CharField(verbose_name="Teléfono", max_length=15, null=False, blank=False)
    celular = models.CharField(verbose_name="Celular", max_length=15, null=False, blank=False)
    correoElectronico = models.CharField(verbose_name="Correo Electrónico", max_length=100, null=False, blank=False)
    observaciones = models.TextField(verbose_name="Observaciones", max_length=500, null=False, blank=False)

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
        dict['celular'] = self.celular
        dict['correoElectronico'] = self.correoElectronico
        dict['observaciones'] = str(self.observaciones)


        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


#Catalogo de ejemplares
class Ejemplares(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False, blank=False)
    edad = models.FloatField(verbose_name="Edad", blank=False, null=False, default=0)
    peso = models.FloatField(verbose_name='Peso', blank=False, null=False, default=0)
    sexo = models.ForeignKey(Sexo, verbose_name="Sexo", null=False, blank=False,on_delete=models.CASCADE,)
    nacionalidad = models.ForeignKey(Nacionalidad, verbose_name="Nacionalidad", null=False, blank=False,on_delete=models.CASCADE,)
    color = models.CharField(verbose_name="Color", max_length=100, null=False, blank=False)
    padre = models.CharField(verbose_name="Padre del Caballo", max_length=100, null=False, blank=False)
    madre = models.CharField(verbose_name="Madre del Caballo", max_length=100, null=False, blank=False)
    observaciones = models.TextField(verbose_name="Observaciones", max_length=500, null=False, blank=False)

    cuadra = models.ForeignKey(Cuadras, verbose_name="Cuadra", null=False, blank=False,on_delete=models.CASCADE,)

    class Meta:
        ordering = ['nombre']
        verbose_name = "Ejemplar"
        verbose_name_plural = "Ejemplares"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['nombre'] = str(self.nombre)
        dict['edad'] = str(self.edad)
        dict['peso'] = str(self.peso)
        dict['sexo'] = self.sexo.nombre
        dict['nacionalidad'] = self.nacionalidad.nombre
        dict['color'] = str(self.color)
        dict['padre'] = str(self.padre)
        dict['madre'] = str(self.madre)
        dict['cuadra'] = str(self.cuadra.nombre)

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
    observaciones = models.TextField(verbose_name="Observaciones", max_length=500, null=False, blank=False)

    tipoEvento = models.ForeignKey(TipoEvento, verbose_name="Tipo de Evento", null=False, blank=False, on_delete=models.CASCADE,)
    #fechasEvento = models.ForeignKey(FechasEvento, verbose_name="Fechas del Evento", null=False, blank=False, on_delete=models.CASCADE,)
    descuento = models.ForeignKey(Descuentos, verbose_name="Descuento", null=True, blank=True, on_delete=models.CASCADE,)
    #condicionesEvento = models.ForeignKey(CondicionesEvento, verbose_name="Condiciones del Evento", null=False, blank=False, on_delete=models.CASCADE,)

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
        dict['fechaEvento'] = self.fechasEvento
        dict['descuento'] = self.descuento

        #dics[''] = self.


        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre



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
    inscripcion = models.ForeignKey(inscripcion, verbose_name="Inscripcion", null=False, blank=False, on_delete=models.CASCADE,)

    cuota = ChainedForeignKey(CuotaEvento,
                                 chained_field="inscripcion.evento",
                                 chained_model_field="evento",
                                 show_all=False,
                                 auto_choose=True,
                                 sort=True,
                                 null=True,
                                 blank=True)
    #cuota = models.ForeignKey(CuotaEvento, verbose_name="Cuota", null=False, blank=False, on_delete=models.CASCADE, )
    cuotaPagada = models.FloatField(verbose_name='Cuota Recibida', null=False, blank=False,)
    cuotaLetra = models.CharField(verbose_name="Cuota en Letra", null=False, blank=False, max_length=500,)
    conceptoPago = models.CharField(verbose_name="Concepto de Pago", null=False, blank=False, max_length=250,)
    fechaPago = models.DateField(auto_now=True, verbose_name='Fecha de Pago')
    fechaRegistro = models.DateField(auto_now=True, verbose_name='Fecha de Registro')
    numeroRecibo = models.IntegerField(verbose_name= "Recibo", null=False, blank=False,)
    valorRecibido = models.CharField(verbose_name="Valor Recibido en", null=False, blank=False, max_length=500 )

    class Meta:
        #ordering = ['evento']
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        dict['cuota'] = str(self.cuota)
        dict['inscripcion'] = str(self.inscripcion)
        dict['cuotaPagada'] = str(self.cuotaPagada)
        dict['cuotaLetra'] = str(self.cuotaLetra)
        dict['conceptoPago'] = str(self.conceptoPago)
        dict['fechaPago'] = str(self.fechaPago)
        dict['fechaRegistro'] = str(self.fechaRegistro)
        dict['numeroRecibo'] = str(self.numeroRecibo)
        dict['valorRecibido'] = str(self.valorRecibido)

        return dict

    def __str__(self):
        return str(self.inscripcion) + ' ' + str(self.cuota.tipoCuota.nombre)

    def __unicode__(self):
        return str(self.inscripcion) + ' ' + str(self.cuota.tipoCuota.nombre)
