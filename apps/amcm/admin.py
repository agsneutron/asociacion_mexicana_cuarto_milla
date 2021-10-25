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
    list_display = ('nombre', 'descripcion', 'monto', 'tipoCuota',)
    fieldsets = (
        (('Cuotas'),
         {'fields': ('nombre', 'descripcion', 'monto', 'tipoCuota',)}),)


# Administrador para el catálogo Cuotas.

class TipoCuotaAdmin(admin.ModelAdmin):
    model = TipoCuota
    #fields = ('nombre', 'descripcion',)
    actions = None
    list_per_page = 20
    list_display = ('nombre', 'descripcion',)
    fieldsets = (
        (('Tipo de Cuota'),
         {'fields': ('nombre', 'descripcion',)}),)

# administrador tipo evento

class TipoEventoAdmin(admin.ModelAdmin):
    model = TipoEvento
    #fields = ('nombre', 'descripcion',)
    actions = None
    list_per_page = 20
    list_display = ('nombre', 'descripcion',)
    fieldsets = (
        (('Tipo de Evento'),
         {'fields': ('nombre', 'descripcion',)}),)

# Administrador para el catálogo Cuotas.

class DescuentoAdmin(admin.ModelAdmin):
    model = Descuentos
    #fields = ('nombre', 'descripcion', 'porcentaje')
    actions = None
    list_per_page = 20
    list_display = ('nombre', 'descripcion', 'porcentaje',)
    fieldsets = (
        (('Descuentos'),
         {'fields': ('nombre', 'descripcion', 'porcentaje', )}),)


# Administrador para el catálogo Cuotas.

class SexoAdmin(admin.ModelAdmin):
    model = Sexo
    #fields = ('nombre',)
    actions = None
    list_per_page = 20
    list_display = ('nombre',)
    fieldsets = (
        (('Sexo'),
         {'fields': ('nombre', )}),)


# Administrador para el catálogo Cuotas.

class NacionalidadAdmin(admin.ModelAdmin):
    model = Nacionalidad
    # fields = ('nombre', 'abreviatura')
    actions = None
    list_per_page = 20
    list_display = ('nombre', 'abreviatura',)
    fieldsets = (
        (('Nacionalidad'),
         {'fields': ('nombre','abreviatura',)}),)


# Administrador para el catálogo Ejemplares.
class EjemplarAdmin(admin.ModelAdmin):
    model = Ejemplares
    #fields = ('nombre',)
    actions = None
    list_per_page = 20
    list_display = ('cuadra', 'nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color',)
    fieldsets = (
        (('Ejemplares'),
         {'fields': ('cuadra', 'nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre',)}),)


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
    list_per_page = 20
    inlines = [EjemplarInlineAdmin, ]
    list_display = ('nombre', 'representante', 'telefono', 'celular', 'correoElectronico',)
    fieldsets = (
        (('Cuadras'), {'fields': ('nombre', 'representante', 'telefono', 'celular', 'correoElectronico', 'observaciones',)}),)


class CuotasEventoInlineAdmin(admin.TabularInline):
    model = CuotaEvento
    fields = ( 'tipoCuota', 'monto', 'fechaVencimiento', )
    actions = None
    extra = 0
    list_per_page = 20

    # fieldsets = (
    #     (('Ejemplares'),
    #      {'fields': ('nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre',)}),)



class CondicionesEventoInlineAdmin(admin.TabularInline):
    model = CondicionesEvento
    fields = ('limite', 'tipoCondicion', 'valor', 'especificacion', )
    actions = None
    extra = 0
    list_per_page = 20

    # fieldsets = (
    #     (('Ejemplares'),
    #      {'fields': ('nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre',)}),)



class FechasEventoInlineAdmin(admin.TabularInline):
    model = FechasEvento
    fields = ('tipoFecha', 'fecha', 'evento' )
    actions = None
    extra = 0
    list_per_page = 20

    # fieldsets = (
    #     (('Ejemplares'),
    #      {'fields': ('nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre',)}),)



class EventoAdmin(admin.ModelAdmin):
    model = Evento
    # fields = ('nombre', 'representante', 'telefono', 'celular', 'correoElectronico', 'observaciones')
    actions = None
    list_per_page = 20
    inlines = [FechasEventoInlineAdmin, CondicionesEventoInlineAdmin, CuotasEventoInlineAdmin]
    list_display = ('nombre', 'tipoEvento', 'yardas', 'bolsa', 'fondo', )
    fieldsets = (
        (('Evento'),
         {'fields': ('nombre', 'yardas', 'descripcion', 'bolsa', 'fondo', 'temporada', 'tipoEvento','descuento', 'observaciones', )}),)


class InscripcionAdmin(admin.ModelAdmin):
    model = inscripcion
    actions = None
    list_per_page = 20
    list_display = ('evento', 'cuadra',  'ejemplar',)
    fieldsets = (
        (('Inscripción'),
         {'fields': ('evento', 'cuadra', 'ejemplar',  'status', )}),)
    exclude = ('fechaRegistro',)


admin.site.register(Cuotas, CuotaAdmin)
admin.site.register(TipoCuota, TipoCuotaAdmin)
admin.site.register(Descuentos, DescuentoAdmin)
admin.site.register(Sexo, SexoAdmin)
admin.site.register(Nacionalidad, NacionalidadAdmin)
admin.site.register(Cuadras, CuadraAdmin)
admin.site.register(Ejemplares, EjemplarAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(TipoFecha)
admin.site.register(CuotaEvento)
admin.site.register(RegistroCuotaEvento)
admin.site.register(Limite)
admin.site.register(TipoCondicion)
admin.site.register(TipoEvento, TipoEventoAdmin)
admin.site.register(inscripcion, InscripcionAdmin)