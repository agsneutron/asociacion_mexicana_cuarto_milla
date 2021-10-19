# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - AriSan - FusionTI
"""

from django.contrib import admin
from apps.amcm.models import *


# Administrador para el catálogo Cuotas.

class CuotaAdmin(admin.ModelAdmin):
    model = Cuotas
    #fields = ('nombre', 'descripcion', 'monto', 'tipoCuota')
    actions = None
    list_per_page = 20
    fieldsets = (
        (('Cuotas'),
         {'fields': ('nombre', 'descripcion', 'monto', 'tipoCuota',)}),)


# Administrador para el catálogo Cuotas.

class TipoCuotaAdmin(admin.ModelAdmin):
    model = TipoCuota
    #fields = ('nombre', 'descripcion',)
    actions = None
    list_per_page = 20
    fieldsets = (
        (('Tipo de Cuota'),
         {'fields': ('nombre', 'descripcion',)}),)


# Administrador para el catálogo Cuotas.

class DescuentoAdmin(admin.ModelAdmin):
    model = Descuentos
    #fields = ('nombre', 'descripcion', 'porcentaje')
    actions = None
    list_per_page = 20
    fieldsets = (
        (('Descuentos'),
         {'fields': ('nombre', 'descripcion', 'porcentaje', )}),)


# Administrador para el catálogo Cuotas.

class SexoAdmin(admin.ModelAdmin):
    model = Sexo
    #fields = ('nombre',)
    actions = None
    list_per_page = 20
    fieldsets = (
        (('Sexo'),
         {'fields': ('nombre', )}),)


# Administrador para el catálogo Cuotas.

class NacionalidadAdmin(admin.ModelAdmin):
    model = Nacionalidad
    # fields = ('nombre', 'abreviatura')
    actions = None
    list_per_page = 20
    fieldsets = (
        (('Nacionalidad'),
         {'fields': ('nombre','abreviatura',)}),)


# Administrador para el catálogo Ejemplares.
class EjemplarAdmin(admin.ModelAdmin):
    model = Ejemplares
    #fields = ('nombre',)
    actions = None
    extra = 1
    list_per_page = 20
    fieldsets = (
        (('Ejemplares'),
         {'fields': ('nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre',)}),)


class EjemplarInlineAdmin(admin.StackedInline):
    model = Ejemplares
    fields = ('nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre', )
    actions = None
    extra = 1
    list_per_page = 20
    # fieldsets = (
    #     (('Ejemplares'),
    #      {'fields': ('nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre',)}),)


class CuadraAdmin(admin.ModelAdmin):
    model = Cuadras
    #fields = ('nombre', 'representante', 'telefono', 'celular', 'correoElectronico', 'observaciones')
    actions = None
    extra = 1
    list_per_page = 20
    inlines= [EjemplarInlineAdmin, ]
    fieldsets = (
        (('Cuadras'), {'fields': ('nombre', 'representante', 'telefono', 'celular', 'correoElectronico', 'observaciones',)}),)


admin.site.register(Cuotas, CuotaAdmin)
admin.site.register(TipoCuota, TipoCuotaAdmin)
admin.site.register(Descuentos, DescuentoAdmin)
admin.site.register(Sexo, SexoAdmin)
admin.site.register(Nacionalidad, NacionalidadAdmin)
admin.site.register(Cuadras, CuadraAdmin)
admin.site.register(Ejemplares, EjemplarAdmin)
