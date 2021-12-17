# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from apps.amcm import api
from django.conf.urls import url


urlpatterns = [
    path('get_recibo_pdf/', api.GenerarReciboPDF.as_view(), name="recibo"),
    url(r'^get_reporte/', login_required(api.getReporteEventos.as_view())),
    url(r'^get_reporte_cuota/', login_required(api.getReporteCuotas.as_view())),
    url(r'^get_reporte_cuota_pdf/', login_required(api.getReporteCuotasPDF.as_view())),
    url(r'^get_reporte_cuota_acumulado/', login_required(api.getReporteCuotasAcumulado.as_view())),
    url(r'^get_reporte_cuota_acumulado_pdf/', login_required(api.getReporteCuotasAcumuladoPDF.as_view())),
]