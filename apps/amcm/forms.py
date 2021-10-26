# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - AriSan FusionTI
"""

from django import forms
from apps.amcm.models import *

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'