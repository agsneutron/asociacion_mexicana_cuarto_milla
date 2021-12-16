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


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request', None)
        super(PagoForm, self).__init__(*args, **kwargs)


    def save(self, commit=True):
        # instance = super(PagoForm, self).save(commit=False)
        # if instance.id is not None:  # Revisa si existe ese objeto
        #     a = Pago.objects.filter(id=instance.id).first()
        ejemplares = self.cleaned_data['ejemplar']
        ejemplares_total = 0
        for ejemplar in ejemplares:
            ejemplares_total +=1
            print(ejemplar)

        pagos = Pago.objects.filter(evento=self.cleaned_data['evento'], cuota=self.cleaned_data['cuota'], cuadra=self.cleaned_data['cuadra'])
        total_pago=0
        for pago in pagos:
            ejemplares_pago=pago.ejemplar.all()
            if set(list(ejemplares)) == set(list(ejemplares_pago)):
                total_pago += pago.cuotaPagada
                print(ejemplar)

        monto_cuota = (self.instance.cuota.monto * ejemplares_total)
        monto_recibido = self.instance.cuotaPagada + total_pago
        if (monto_cuota - monto_recibido > 0):
            self.instance.estatus_cuota = 'PENDIENTE'
        else:
            self.instance.estatus_cuota = 'PAGADO'
        return super(PagoForm, self).save(commit)

