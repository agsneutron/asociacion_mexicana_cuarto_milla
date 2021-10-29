# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.amcm import api


urlpatterns = [
    path('get_recibo_pdf/', api.GenerarReciboPDF.as_view(), name="recibo"),
]