# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - AriSan - FusionTI
"""

from django.db import models
from django.forms.models import model_to_dict

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
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=False, blank=False)
    representante = models.CharField(verbose_name="Representante", max_length=100, null=False, blank=False)
    telefono = models.CharField(verbose_name="Teléfono", max_length=15, null=False, blank=False)
    celular = models.CharField(verbose_name="Celular", max_length=15, null=False, blank=False)
    correoElectronico = models.CharField(verbose_name="Correo Electrónico", max_length=15, null=False, blank=False)
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
        dict['sexo'] = self.sexo
        dict['nacionalidad'] = self.nacionalidad
        dict['color'] = str(self.color)
        dict['padre'] = str(self.padre)
        dict['madre'] = str(self.madre)
        dict['cuadra'] = str(self.cuadra)

        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre