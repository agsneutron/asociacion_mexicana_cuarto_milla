# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from apps.amcm import api
from django.conf.urls import url
from apps.amcm import views


urlpatterns = [
    path('get_recibo_pdf/', api.GenerarReciboPDF.as_view(), name="recibo"),
    url(r'^get_reporte/', login_required(api.getReporteEventos.as_view())),
    url(r'^get_reporte_cuota/', login_required(api.getReporteCuotas.as_view())),
    url(r'^get_reporte_cuota_pdf/', login_required(api.getReporteCuotasPDF.as_view())),
    url(r'^get_reporte_cuota_acumulado/', login_required(api.getReporteCuotasAcumulado.as_view())),
    url(r'^get_reporte_cuota_acumulado_pdf/', login_required(api.getReporteCuotasAcumuladoPDF.as_view())),
    url(r'^get_reporte_lista_pdf/', login_required(api.getReporteLista.as_view())),
    url(r'^get_listado_elegibles/', login_required(api.getListadoElegibles.as_view())),
    url(r'^get_listado_elegibles_pdf/', login_required(api.getListadoElegiblesPDF.as_view())),
    url(r'^get_evento_cuotas/', login_required(api.getEventoCuotas.as_view())),
    url(r'^get_evento_cuotas_pdf/', login_required(api.getEventoCuotasPDF.as_view())),
    url(r'^get_dashboard/', login_required(api.getDashboard.as_view())),
    url(r'^get_reporte_recibos/', login_required(api.getReporteRecibos.as_view())),
    url(r'^get_reporte_recibos_pdf/', login_required(api.getReporteRecibosPDF.as_view())),
    #url(r'^register_by_token', views.register_by_access_token),
]