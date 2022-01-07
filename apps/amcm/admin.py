# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - AriSan - FusionTI
"""

from django.contrib import admin
from apps.amcm.models import *
from apps.amcm import views
from apps.amcm.forms import *
from django.conf.urls import url
from django.utils.html import format_html


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
class EstatusEjemplarAdmin(admin.ModelAdmin):
    model = EstatusEjemplar
    #fields = ('nombre', 'descripcion',)
    actions = None
    list_per_page = 20
    list_display = ('nombre', 'descripcion',)
    fieldsets = (
        (('Estatus del Ejemplar'),
         {'fields': ('nombre', 'descripcion',)}),)

# Administrador para el catálogo Paquetes de Descuento.
class PaquetesDescuentoAdmin(admin.ModelAdmin):
    model = PaquetesDescuento
    #fields = ('nombre', 'descripcion',)
    actions = None
    list_per_page = 20
    list_display = ('paquete',)
    fieldsets = (
        (('Paquetes de Descuento'),
         {'fields': ('paquete', 'evento_uno','porcentaje_uno','evento_dos','porcentaje_dos','evento_tres',
                     'porcentaje_tres','evento_cuatro','porcentaje_cuatro','evento_cinco','porcentaje_cinco','anio',)}),)


# Administrador para el catálogo Cuotas.
class TipoCuotaAdmin(admin.ModelAdmin):
    model = TipoCuota
    #fields = ('nombre', 'descripcion',)
    actions = None
    list_per_page = 20
    list_display = ('nombre', 'descripcion', 'moneda')
    fieldsets = (
        (('Tipo de Cuota'),
         {'fields': ('nombre', 'descripcion', 'moneda')}),)


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


# Administrador para el catálogo Cuentas Contables.
class CuentasContablesAdmin(admin.ModelAdmin):
    model = CuentasContables
    actions = None
    list_per_page = 20
    list_display = ('codigo', 'nombre', 'estatus',)
    fieldsets = (
        (('Cuentas Contables'),
         {'fields': ('codigo', 'nombre', 'estatus',)}),)


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
    list_display = ('cuadra', 'lote', 'nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'estatus')
    fieldsets = (
        (('Ejemplares'),
         {'fields': ('cuadra', 'lote',  'nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre', 'estatus',)}),)

    def get_form(self, request, obj=None, **kwargs):
        form = super(EjemplarAdmin, self).get_form(request, obj, **kwargs)
        field = form.base_fields['cuadra']
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = form.base_fields['sexo']
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = form.base_fields['nacionalidad']
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = form.base_fields['estatus']
        field.widget.can_add_related = False
        field.widget.can_change_related = False

        return form

#inlines para asignar datos de contacto a Cuadras
class ContactoInlineAdmin(admin.TabularInline):
    model= Contacto
    fields = ('nombre', 'telefono')
    actions = None
    extra = 0
    list_per_page = 20


#inlines para asignar ejemplares a cuadras
class EjemplarInlineAdmin(admin.StackedInline):
    model = Ejemplares
    fields = ('lote', 'nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre','estatus', )
    actions = None
    extra = 1
    list_per_page = 20

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        field = formset.form.base_fields["sexo"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = formset.form.base_fields["nacionalidad"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = formset.form.base_fields["estatus"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        return formset

    # fieldsets = (
    #     (('Ejemplares'),
    #      {'fields': ('nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre',)}),)


class CuadraAdmin(admin.ModelAdmin):
    model = Cuadras
    #fields = ('nombre', 'representante', 'telefono', 'celular', 'correoElectronico', 'observaciones')
    actions = None
    list_per_page = 20
    inlines = [ContactoInlineAdmin, EjemplarInlineAdmin, ]
    list_display = ('nombre', 'representante', 'telefono', 'celular', 'correoElectronico',)
    fieldsets = (
        (('Cuadras'), {'fields': ('nombre', 'representante', 'telefono', 'celular', 'correoElectronico', 'observaciones',)}),)


class CuotasEventoInlineAdmin(admin.TabularInline):
    model = CuotaEvento
    fields = ( 'tipoCuota', 'monto', 'fechaVencimiento', 'observacion', )
    actions = None
    extra = 0
    list_per_page = 20

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        field = formset.form.base_fields["tipoCuota"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        return formset
    # fieldsets = (
    #     (('Ejemplares'),
    #      {'fields': ('nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre',)}),)


class CondicionesEventoInlineAdmin(admin.TabularInline):
    model = CondicionesEvento
    fields = ('limite', 'tipoCondicion', 'valor', 'especificacion', )
    actions = None
    extra = 0
    list_per_page = 20

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        field = formset.form.base_fields["limite"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = formset.form.base_fields["tipoCondicion"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        return formset
    # fieldsets = (
    #     (('Ejemplares'),
    #      {'fields': ('nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre',)}),)


class FechasEventoInlineAdmin(admin.TabularInline):
    model = FechasEvento
    fields = ('tipoFecha', 'fecha', 'evento' )
    actions = None
    extra = 0
    list_per_page = 20

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        field = formset.form.base_fields["tipoFecha"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        return formset

    # fieldsets = (
    #     (('Ejemplares'),
    #      {'fields': ('nombre', 'edad', 'peso', 'sexo', 'nacionalidad', 'color', 'padre', 'madre',)}),)


class CuentasEventoInlineAdmin(admin.TabularInline):
    model = CuentasEvento
    fields = ('cuenta', )
    actions = None
    extra = 0
    list_per_page = 20

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        field = formset.form.base_fields["cuenta"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        return formset


class EventoAdmin(admin.ModelAdmin):
    model = Evento
    # fields = ('nombre', 'representante', 'telefono', 'celular', 'correoElectronico', 'observaciones')
    actions = None
    list_per_page = 20
    inlines = [FechasEventoInlineAdmin, CondicionesEventoInlineAdmin, CuotasEventoInlineAdmin, CuentasEventoInlineAdmin]
    list_display = ('nombre', 'yardas', 'bolsa', 'fondo', 'tipoEvento', 'edit_link','pago_link',)
    fieldsets = (
        (('Evento'),
         {'fields': ('nombre', 'temporada', 'tipoEvento',  'yardas', 'elegibles_evento', 'elegibles_subasta', 'descuento', 'bolsa', 'fondo', 'descripcion_evento', 'observaciones', )}),)



    def get_form(self, request, obj=None, **kwargs):
        form = super(EventoAdmin, self).get_form(request, obj, **kwargs)
        field = form.base_fields['tipoEvento']
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = form.base_fields['descuento']
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = form.base_fields['elegibles_evento']
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = form.base_fields['elegibles_subasta']
        field.widget.can_add_related = False
        field.widget.can_change_related = False

        return form


    def changelist_view(self, request, extra_context=None):

        self.list_display = ('nombre', 'yardas', 'bolsa', 'fondo', 'tipoEvento', 'edit_link', 'listado_link', 'pago_link',)

        return super(EventoAdmin, self).changelist_view(request, extra_context)

    def ficha_link(self, obj):
        return format_html(
            '<a href="/indicadores/view/accion/{}/">{}. {}</a>',
            obj.id,
            obj.numero,
            obj.nombre,

        )
    ficha_link.short_description = 'Acción'
    ficha_link.allow_tags = True

    def edit_link(self, obj):
        return format_html('<a href="/admin/amcm/evento/{}/change/"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="far fa-edit"></i></button></a>',
            obj.id,
        )
    edit_link.short_description = 'Editar'
    edit_link.allow_tags = True

    def listado_link(self, obj):
        return format_html('<a href="/amcm/get_listado_elegibles/?evento_id={}"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fas fa-list"></i></button></a>',
            obj.id,
        )
    listado_link.short_description = 'Listado'
    listado_link.allow_tags = True

    def pago_link(self, obj):
        return format_html('<a href="/admin/amcm/pago/?evento_id={}"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fas fa-list-alt"></i></button></a>',
            obj.id,
        )
    pago_link.short_description = 'Pagos'
    pago_link.allow_tags = True

# @admin.register(Evento)
# class EventoAdmin(admin.ModelAdmin):
#     form = EventoForm
#     list_per_page = 20
#     inlines = [FechasEventoInlineAdmin, CondicionesEventoInlineAdmin, CuotasEventoInlineAdmin]
#
#     list_display = ('nombre', 'yardas', 'bolsa', 'fondo', 'tipoEvento',)
#     fieldsets = ((('Evento'), {'fields': ('nombre', 'yardas', 'descripcion', 'bolsa', 'fondo', 'temporada', 'tipoEvento','descuento', 'observaciones', )}),)
#
#
#     def get_form(self, request, obj=None, **kwargs):
#         ModelForm = super(EventoAdmin, self).get_form(request, obj, **kwargs)
#         # # get the foreign key field I want to restrict
#         # contractlineitem = ModelForm.base_fields['contractlineitem']
#         #
#         # # remove the green + and change icons by setting can_change_related and can_add_related to False on the widget
#         # contractlineitem.widget.can_add_related = False
#         # contractlineitem.widget.can_change_related = False
#
#         class ModelFormMetaClass(ModelForm):
#             def __new__(cls, *args, **kwargs):
#                 kwargs['request'] = request
#                 return ModelForm(*args, **kwargs)
#
#         return ModelFormMetaClass
#
#     def get_urls(self):
#         urls = super(EventoAdmin, self).get_urls()
#         info = self.model._meta.app_label, self.model._meta.model_name
#         my_urls = [
#             url(r'^$',
#                 self.admin_site.admin_view(views.EventoListView.as_view()),
#                 name='Evento-list-view'),
#             # url(r'^(?P<pk>\d+)/unlock$', views.unlock_estimate, name='estimate-detail'),
#             # url(r'^(?P<pk>\d+)/$', views.EstimateDetailView.as_view(), name='estimate-detail'),
#             # url(r'^(?P<pk>\d+)/delete/$', views.EstimateDelete.as_view(), name='estimate-delete'),
#             # url(r'^(?P<pk>\d+)/approve', views.approve_estimate_advance, name='estimate-advance-approve'),
#             # url(r'^apply_deductions_to_estimate', views.apply_deductions_to_estimate),
#             # url(r'^save_deductions_to_estimate', views.save_deductions_to_estimate),
#
#         ]
#
#         return my_urls + urls


class InscripcionAdmin(admin.ModelAdmin):
    model = inscripcion
    actions = None
    list_per_page = 20
    list_display = ('evento', 'cuadra',  'ejemplar',)
    fieldsets = (
        (('Inscripción'),
         {'fields': ('evento', 'cuadra', 'ejemplar',  'status', )}),)
    exclude = ('fechaRegistro',)


class CuentasPagoInlineAdmin(admin.TabularInline):
    model = CuentasPago
    actions = None
    extra = 0
    list_per_page = 5


# Inlines para registro de Forma de PAgo
class ReferenciaFormaPagoInlineAdmin(admin.TabularInline):
    model = ReferenciaFormaPago
    actions = None
    extra = 0
    list_per_page = 20
    list_display = ('formapago', 'referencia',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        field = formset.form.base_fields["formapago"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        return formset


#Admin para modelo de pago, se agregan los inlines de forma de pago y cuentas contables de pago
class PagoAdmin(admin.ModelAdmin):
    form = PagoForm
    inlines = [ReferenciaFormaPagoInlineAdmin, CuentasPagoInlineAdmin, ]
    actions = None
    list_per_page = 20
    list_display = ('evento', 'cuadra', 'cuota','cuotaPagada','estatus_cuota','edit_link','recibo_link')
    fields = ('evento', 'cuota', 'cuadra', 'ejemplar', ('cuotaPagada', 'conceptoPago',), ('fechaPago','estatus_credito', ), )


    def get_form(self, request, obj=None, **kwargs):
        form = super(PagoAdmin, self).get_form(request, obj, **kwargs)
        field = form.base_fields['evento']
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = form.base_fields['cuadra']
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = form.base_fields['cuota']
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = form.base_fields['ejemplar']
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        return form

    def edit_link(self, obj):
        return format_html('<a href="/admin/amcm/pago/{}/change/"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="far fa-edit"></i></button></a>',
            obj.id,
        )
    edit_link.short_description = 'Editar'
    edit_link.allow_tags = True

    def recibo_link(self, obj):
        try:
            recibo = Recibo.objects.get(pago__id=obj.id)
            return format_html(
                '<a href="/amcm/get_recibo_pdf/?recibo_id={}"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fa fa-print"></i></button></a>',
                recibo.id,
                )

        except Recibo.DoesNotExist:
            return format_html(
                '<a href="/admin/amcm/recibo/add/?pago_id={}"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fas fa-list-alt"></i></button></a>',
                obj.id,
                )

    recibo_link.short_description = 'Recibos'
    recibo_link.allow_tags = True

    def save_model(self, request, obj, form, change):
        print("ok")
        return super(PagoAdmin, self).save_model(request, obj, form, change)


class ReciboAdmin(admin.ModelAdmin):
    model = Recibo
    form = ReciboForm
    actions = None
    list_per_page = 20
    list_display = ('pago', 'numero_recibo', 'fecha_registro','observaciones','edit_link','recibo_link',)
    fields = ('pago', 'numero_recibo', 'observaciones', 'fecha_registro',)

    def edit_link(self, obj):
        return format_html('<a href="/admin/amcm/recibo/{}/change/"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="far fa-edit"></i></button></a>',
            obj.id,
        )
    edit_link.short_description = 'Editar'
    edit_link.allow_tags = True

    def recibo_link(self, obj):
        return format_html('<a href="/amcm/get_recibo_pdf/?recibo_id={}"><button type="button" class="btn btn-outline-secondary btn-sm"><i class="fa fa-print"></i></button></a>',
            obj.id,
        )
    recibo_link.short_description = 'Imprime'
    recibo_link.allow_tags = True

    fields = (
    'pago', 'numero_recibo', 'fecha_registro','observaciones')

    def get_form(self, request, obj=None, **kwargs):
        if obj is not None:
            pago_id = obj.pago.id
        else:
            pago_id = request.GET.get('pago_id')

        self.param = pago_id
        form = super(ReciboAdmin, self).get_form(request, obj, **kwargs)
        if pago_id:
            pago = Pago.objects.filter(pk=pago_id)
        else:
            pago = Pago.objects.all().order_by('id')
        # self.fields['pago'].attrs['value'] = str(pago.id)
        field = form.base_fields['pago']
        field.queryset = pago
        field.widget.can_add_related = False
        field.widget.can_change_related = False


        return form


class ReasignaEjemplarAdmin(admin.ModelAdmin):
    model = ReasignaEjemplar
    actions = None
    list_per_page = 20
    list_display = ('ejemplar', 'cuadra',)


#Admin para catalogo forma de pago
class FormaPagoAdmin(admin.ModelAdmin):
    model = FormaPago
    actions = None
    list_per_page = 20
    list_display = ('nombre', 'descripcion',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(FormaPagoAdmin, self).get_form(request, obj, **kwargs)
        field = form.base_fields['nombre']
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        return form

# Inlines para registro de Listado Elegibles
class ListadoElegiblesInlineAdmin(admin.TabularInline):
    model = ListadoElegibles
    actions = None
    extra = 0
    list_per_page = 20
    list_display = ('cuadra', 'ejemplar',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        field = formset.form.base_fields["cuadra"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field = formset.form.base_fields["ejemplar"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        return formset


#Admin para catalogo elegible
class ElegibleAdmin(admin.ModelAdmin):
    model = Elegible
    inlines = [ListadoElegiblesInlineAdmin, ]
    actions = None
    list_per_page = 20
    list_display = ('nombre', 'fecha_registro',)


# Admin para catalogo elegible
class ListadoElegiblesAdmin(admin.ModelAdmin):
    model = ListadoElegibles
    actions = None
    list_per_page = 20
    list_display = ('elegible', 'cuadra',  )


#Admin para catalogo elegible
class EventoElegiblesAdmin(admin.ModelAdmin):
    model = EventoElegibles
    actions = None
    list_per_page = 20
    list_display = ('evento', 'elegible', 'cuadra', 'ejemplar', 'estaus')



admin.site.register(Cuotas, CuotaAdmin)
admin.site.register(TipoCuota, TipoCuotaAdmin)
admin.site.register(Descuentos, DescuentoAdmin)
admin.site.register(Sexo, SexoAdmin)
admin.site.register(Nacionalidad, NacionalidadAdmin)
admin.site.register(PaquetesDescuento,PaquetesDescuentoAdmin)
admin.site.register(Cuadras, CuadraAdmin)
admin.site.register(Ejemplares, EjemplarAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(TipoFecha)
admin.site.register(TipoMoneda)
admin.site.register(CuotaEvento)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Recibo, ReciboAdmin)
admin.site.register(Limite)
admin.site.register(TipoCondicion)
admin.site.register(TipoEvento, TipoEventoAdmin)
admin.site.register(inscripcion, InscripcionAdmin)
admin.site.register(EstatusEjemplar, EstatusEjemplarAdmin)
admin.site.register(ReasignaEjemplar, ReasignaEjemplarAdmin)
admin.site.register(CuentasContables, CuentasContablesAdmin)
admin.site.register(FormaPago, FormaPagoAdmin)
admin.site.register(Elegible, ElegibleAdmin)
admin.site.register(EventoElegibles, EventoElegiblesAdmin)
admin.site.register(ListadoElegibles, ListadoElegiblesAdmin)