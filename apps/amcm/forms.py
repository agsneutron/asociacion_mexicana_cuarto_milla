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

def DefCuentasPagoForm(param):
    class CuentasPagoForm(forms.ModelForm):
        class Meta:
            model = CuentasPago
            fields = "__all__"
        def __init__(self, *args, **kwargs):
            self.request = kwargs.pop('request', None)
            super(CuentasPagoForm, self).__init__(*args, **kwargs)
            if param.param:
                cuentasevento = CuentasEvento.objects.filter(evento=param.param)
            else:
                cuentasevento = CuentasEvento.objects.all()

            self.fields['cuenta'].queryset = cuentasevento



    return CuentasPagoForm

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        if kwargs is not None:
            try:
                if kwargs['initial'] != {}:
                    params = kwargs['initial']['_changelist_filters']
                    params = params.split('=')
                    evento_id = params[1]
                    evento = Evento.objects.filter(id=evento_id)
                    kwargs = {'initial': {'evento': evento_id}}
                else:
                    evento_id = 0
                    kwargs = {'initial': {'evento': evento_id}}
            except:
                evento_id = 0

        self.request = kwargs.pop('request', None)
        super(PagoForm, self).__init__(*args, **kwargs)
        #self.fields['evento'].queryset = evento


    def clean(self):
        cleaned_data = super(PagoForm, self).clean()

        estatus_cuota = True
        ejemplares = self.cleaned_data['ejemplar']
        ejemplares_total=0
        for ejemplar in ejemplares:
            ejemplares_total+=1

        pagos = Pago.objects.filter(evento=self.cleaned_data['evento'],
                                    cuadra=self.cleaned_data['cuadra'],estatus_cuota='PENDIENTE').exclude(cuota=self.cleaned_data['cuota'])
        monto_pagado=0
        monto_cuota=0
        nombre_cuota=''
        for pago in pagos:
            ejemplares_pago = pago.ejemplar.all()
            if set(list(ejemplares)) == set(list(ejemplares_pago)):
                monto_cuota = pago.cuota.monto
                nombre_cuota = pago.cuota.tipoCuota.nombre
                monto_pagado+=pago.cuotaPagada
                estatus_cuota=False

        monto_a_pagar = (monto_cuota * ejemplares_total)
        adeudo = monto_a_pagar-monto_pagado
        if estatus_cuota == False:
            self._errors["cuota"] = self.error_class(
                ['no se puede pagar esta cuota, la ' + nombre_cuota + ' tiene un pago pendiente de: $' + '{:,.2f}'.format(adeudo)])
            # self.fields['advance_payment_amount'].
            raise forms.ValidationError("Error")

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

        if self.instance.paquete:
            monto_cuota = self.instance.paquete.importe
        else:
            monto_cuota = (self.instance.cuota.monto * ejemplares_total)

        monto_recibido = self.instance.cuotaPagada + total_pago
        if (monto_cuota - monto_recibido > 0):
            self.instance.estatus_cuota = 'PENDIENTE'
        else:
            self.instance.estatus_cuota = 'PAGADO'
            for pago in pagos:
                pago.estatus_cuota='PAGADO'
                pago.save()
        return super(PagoForm, self).save(commit)

class ReciboForm(forms.ModelForm):
    class Meta:
        model = Recibo
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ReciboForm, self).__init__(*args, **kwargs)


class EventoElegiblesForm(forms.ModelForm):
    class Meta:
        model = EventoElegibles
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        if kwargs is not None:
            try:
                if kwargs['initial'] != {}:
                    params = kwargs['initial']['_changelist_filters']
                    params = params.split('=')
                    evento_id = params[1]
                    evento = Evento.objects.filter(id=evento_id)
                    kwargs = {'initial': {'evento': evento_id}}
                else:
                    evento_id = 0
                    kwargs = {'initial': {'evento': evento_id}}
            except:
                evento_id = 0
        self.request = kwargs.pop('request', None)
        super(EventoElegiblesForm, self).__init__(*args, **kwargs)
