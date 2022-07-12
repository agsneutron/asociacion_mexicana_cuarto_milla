# coding=utf-8
import io
import json

from PIL._imaging import font
from django.db.models import Sum

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from requests import RequestException
from django.views.decorators.cache import never_cache
from django.db.models.functions import Trim


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.utils import timezone
import six as StringIO
from apps.amcm.models import *
from apps.lib.utilities import Utilities
from django.db.models import Sum
from django.db.models import Count
import datetime
import os
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')



def html_to_pdf(content, output):
    """
    Generate a pdf using a string content

    Parameters
    ----------
    content : str
        content to write in the pdf file
    output  : str
        name of the file to create
    """
    # Open file to write
    result_file = open(output, "w+b")  # w+b to write in binary mode.

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
        content,  # the HTML to convert
        dest=result_file  # file handle to recieve result
    )

    # close output file
    result_file.close()

    result = pisa_status.err

    if not result:
        print("Successfully created PDF")
    else:
        print("Error: unable to create the PDF")

        # return False on success and True on errors
    return result

class Render():
    @staticmethod
    @never_cache
    def render(path, params):
        if path == 'amcm/listado_elegibles_pdf.html':
            filename = 'listado.pdf'
        elif path == 'amcm/evento_cuotas_pdf_original.html':
            filename = 'evento_listado.pdf'
        elif path == 'amcm/evento_cuotas_pdf.html':
            filename = 'listado_cuotas_' + str(params['evento'].__self__) + '.pdf'
        elif path == 'amcm/estado_cuenta.html':
            filename = 'estado_cuenta.pdf'
        elif path == 'amcm/estado_cuenta_pagos.html':
            filename = 'estado_cuenta_pagos.pdf'
        elif path == 'amcm/recibo_impresora.html':
            filename = 'Recibo-' + str(params['no_recibo']) + '.pdf'
        else:
            filename = 'listado_evento' + str(params['no_recibo']) + '.pdf'

        template = get_template(path)
        html = template.render(params)
        stream = io.buffer = BytesIO()

        #response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        #pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), response, path=path)
        #https://www.it-swarm-es.com/es/django/django-pisa-agregar-imagenes-pdf-salida/968337910/

        pdf = pisa.CreatePDF(io.BytesIO(html.encode("UTF-8")), stream,link_callback=path)


        if not pdf.err:
            stream.flush()
            response = HttpResponse(stream.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
            stream.flush()
            return response
        else:
            return HttpResponse("Error al generar el documento PDF", status=400)

    @staticmethod
    def renderCuota(path, params):
        filename = 'reporte.pdf'
        template = get_template(path)
        html = template.render(params)
        response = io.buffer = BytesIO()

        # pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), response, path=path)
        # https://www.it-swarm-es.com/es/django/django-pisa-agregar-imagenes-pdf-salida/968337910/

        pdf = pisa.CreatePDF(io.BytesIO(html.encode("UTF-8")), response, link_callback=path)
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
            return response
        else:
            return HttpResponse("Error al generar el documento PDF", status=400)

    def get_full_path_x(request):
        full_path = ('http', ('', 's')[request.is_secure()], '://',
                     request.META['HTTP_Host'], request.path)
        return ''.join(full_path)

    @staticmethod
    def write_pdf(template_src, context_dict, filename):
        template = get_template(template_src)
        # context = Context(context_dict)
        html = template.render(context_dict)
        result = open(filename, 'wb')  # Changed from file to filename
        pdf = pisa.pisaDocument(StringIO.StringIO(
            html.encode("UTF-8")), result)
        result.close()



    @staticmethod
    def from_template(template, output):
        """
        Generate a pdf from a html file

        Parameters
        ----------
        source : str
            content to write in the pdf file
        output  : str
            name of the file to create
        """
        # Reading our template
        source_html = open(template, "r")
        content = source_html.read()  # the HTML to convert
        source_html.close()  # close template file

        html_to_pdf(content, output)


# ******************************************** renderear PDF ***********************************************
class GenerarReciboPDF(ListView):
    @never_cache
    def get(self, request, *args, **kwargs):
        anterior=False;
        recibo_id = request.GET.get('recibo_id')
        recibo = Recibo.objects.get(id=recibo_id)
        ejemplares=recibo.pago.ejemplar.all()
        total_ejemplares=0
        monto_pagado=0
        for ejemplar in ejemplares:
            total_ejemplares +=1
        pagos = Pago.objects.filter(evento=recibo.pago.evento,cuota=recibo.pago.cuota,cuadra=recibo.pago.cuadra,id__lt=recibo.pago.id)
        for pago in pagos:
            if set(list(ejemplares)) == set(list(pago.ejemplar.all())) and pago.recibo_set is not None:
                monto_pagado += pago.cuotaPagada

        arrCuentas=[]
        cuentas = recibo.pago.cuentaspago_set.all()
        for cuenta in cuentas:
            cuenta_json={
                'nombre': cuenta.cuenta.cuenta.nombre,
                'importe': '{:,.2f}'.format(cuenta.importe),
                'codigo': cuenta.cuenta.cuenta.codigo
            }
            arrCuentas.append(cuenta_json)

        arrReferenciaFormaPago = []
        referennciaformapago = recibo.pago.referenciaformapago_set.all()
        for referencia in referennciaformapago:
            referencia_json={
                'nombre': referencia.formapago.nombre,
                'importe':'{:,.2f}'.format(referencia.importe),
                'referencia':referencia.referencia,
                'fecha': str(referencia.fecha_registro.strftime("%d/%m/%Y")).upper()
            }
            arrReferenciaFormaPago.append(referencia_json)

        renglones=[1,2,3]
        ancho_evento=26
        ancho_caballos=91
        if recibo.pago.cuota:

            conceptoCuotas = recibo.pago.cuota.tipoCuota.nombre
            if recibo.pago.estatus_credito == 'ANTICIPO':
                conceptoCuotas = 'ANTICIPO DE ' + conceptoCuotas
            if recibo.pago.estatus_credito == 'PAGO TOTAL':
                conceptoCuotas = 'PAGO TOTAL DE ' + conceptoCuotas

            if recibo.pago.cuota.tipoCuota.tipo == 'EVENTO':
                if recibo.pago.cuota.tipoCuota.id == 2:
                    descuento = recibo.pago.cuota.monto*recibo.pago.evento.descuento.porcentaje
                    descuento = descuento*total_ejemplares
                    # el descuento ya está aplicado en el monto de la cuota del evento
                    descuento = 0
                    monto_a_pagar = recibo.pago.cuota.monto*total_ejemplares

                    saldo=(monto_a_pagar - descuento) - (recibo.pago.cuotaPagada+monto_pagado)
                else:
                    saldo=(recibo.pago.cuota.monto*total_ejemplares) - (recibo.pago.cuotaPagada+monto_pagado)
            else:
                saldo = 0.00
            concepto=recibo.pago.evento.nombre
            if concepto == 'GENERAL':
                concepto = recibo.pago.conceptoPago if recibo.pago.conceptoPago else ""
        else:
            ancho_evento=91
            ancho_caballos=25
            conceptoCuotas = recibo.pago.paquete.get_paquete_display()
            if recibo.pago.estatus_credito == 'ANTICIPO':
                conceptoCuotas = 'ANTICIPO DE ' + conceptoCuotas
            if recibo.pago.estatus_credito == 'PAGO TOTAL':
                conceptoCuotas = 'PAGO TOTAL DE ' + conceptoCuotas

            saldo=(recibo.pago.paquete.importe*total_ejemplares) - (recibo.pago.cuotaPagada+monto_pagado)
            renglones=[]
            concepto = ""
            if recibo.pago.paquete.evento_uno:
                concepto = concepto + ' ' + recibo.pago.paquete.evento_uno.nombre
            if recibo.pago.paquete.evento_dos:
                concepto = concepto + ', ' + recibo.pago.paquete.evento_dos.nombre
            if recibo.pago.paquete.evento_tres:
                concepto = concepto + ', ' + recibo.pago.paquete.evento_tres.nombre
            if recibo.pago.paquete.evento_cuatro:
                concepto = concepto + ', ' + recibo.pago.paquete.evento_cuatro.nombre
            if recibo.pago.paquete.evento_cinco:
                concepto = concepto + ', ' + recibo.pago.paquete.evento_cinco.nombre

        recibido_en = ''
        for obj in arrReferenciaFormaPago:
            recibido_en += obj['nombre'] + ' ' + obj['importe'] + ' ' + obj['referencia'] + ' ' +obj['fecha'] + ', '

        if len(recibido_en) <=50:
            font_size_recibido = 18
        else:
            font_size_recibido =16

        total_recibido = 0
        cuotas_pagadas = 0
        for pago_ref in recibo.pago.referenciaformapago_set.all():
            texto=Trim(pago_ref.referencia)
            ref_anteriores = ReferenciaFormaPago.objects.filter(referencia=pago_ref.referencia, id__lt=pago_ref.id)
            for ref_ant in ref_anteriores:
                cuotas_pagadas += ref_ant.importe_pago
            total_recibido += pago_ref.importe
        saldo_favor = total_recibido - (recibo.pago.cuotaPagada + cuotas_pagadas)

        if saldo_favor>0:
            referencia_json = {
                'nombre': 'Saldo a favor',
                'importe': '{:,.2f}'.format(saldo_favor),
                'referencia': '',
                'fecha': ''
            }
            arrReferenciaFormaPago.append(referencia_json)

        cantidad_letra = '{:,.2f}'.format(recibo.pago.cuotaPagada) + '(' + Utilities.numero_to_letras(recibo.pago.cuotaPagada) + ' PESOS 00/100 M.N.)'
        len_cantidad_letra = len(cantidad_letra)
        if len(cantidad_letra) <=50:
            font_size_letra = 18
        else:
            if len(cantidad_letra)>50 and len(cantidad_letra)<59:
                font_size_letra = 18
            else:
                if len(cantidad_letra) > 58 and len(cantidad_letra) < 67:
                    font_size_letra = 18
                else:
                    if len(cantidad_letra) > 66 and len(cantidad_letra) < 80:
                        font_size_letra = 18


        if len(conceptoCuotas + ', ' +concepto) <=52:
            font_size_concepto = 18
        else:
            if len(conceptoCuotas + ', ' +concepto) > 52 and len(conceptoCuotas + ', ' +concepto) < 60:
                font_size_concepto = 17
            else:
                font_size_concepto = 16

        caballos=''
        for obj in ejemplares:
            caballos += obj.nombre + ','

        if len(caballos) <=160:  #50
            font_size_caballos = 18
        else:
            font_size_caballos = 16
            renglones = [1, 2]

        if recibo.pago.estatus_credito == 'PAGO TOTAL':
            saldo=0

        params = {
            'no_recibo': recibo.numero_recibo,
            'dia':recibo.fecha_registro.day,
            'mes': recibo.fecha_registro.month,
            'anio': recibo.fecha_registro.year,
            'usuario': recibo.pago.cuadra.nombre , #+' '+ recibo.pago.cuadra.representante,
            'importe':'{:,.2f}'.format(recibo.pago.cuotaPagada),
            'importe_letra': '(' + Utilities.numero_to_letras(recibo.pago.cuotaPagada) + ' PESOS 00/100 M.N.)',
            'concepto': conceptoCuotas,
            'recibido_en': arrReferenciaFormaPago,
            'saldo': 'SALDO POR PAGAR: ' + '{:,.2f}'.format(saldo),
            'cuentas': arrCuentas,
            'evento': concepto,
            'ejemplares': ejemplares,
            'font_size_letra':font_size_letra,
            'font_size_evento':font_size_concepto,
            'font_size_caballos':font_size_caballos,
            'font_size_recibido':font_size_recibido,
            'ancho_evento':ancho_evento,
            'ancho_caballos':ancho_caballos,
            'renglones':renglones,
            }

        return Render.render('amcm/recibo_impresora.html', params)

class GenerarReciboImpresora(ListView):
    def get(self, request, *args, **kwargs):
        recibo_id = request.GET.get('recibo_id')
        recibo = Recibo.objects.get(id=recibo_id)
        ejemplares = recibo.pago.ejemplar.all()
        total_ejemplares = 0
        monto_pagado = 0
        for ejemplar in ejemplares:
            total_ejemplares += 1
        pagos = Pago.objects.filter(evento=recibo.pago.evento, cuota=recibo.pago.cuota, cuadra=recibo.pago.cuadra,
                                    id__lt=recibo.pago.id)
        for pago in pagos:
            if set(list(ejemplares)) == set(list(pago.ejemplar.all())):
                monto_pagado += pago.cuotaPagada

        arrCuentas = []
        cuentas = recibo.pago.cuentaspago_set.all()
        for cuenta in cuentas:
            cuenta_json = {
                'nombre': cuenta.cuenta.cuenta.nombre,
                'importe': '{:,.2f}'.format(cuenta.importe),
                'codigo': cuenta.cuenta.cuenta.codigo
            }
            arrCuentas.append(cuenta_json)

        arrReferenciaFormaPago = []
        referennciaformapago = recibo.pago.referenciaformapago_set.all()
        for referencia in referennciaformapago:
            referencia_json = {
                'nombre': referencia.formapago.nombre,
                'importe': '{:,.2f}'.format(referencia.importe),
                'referencia': referencia.referencia
            }
            arrReferenciaFormaPago.append(referencia_json)

        if recibo.pago.cuota:
            saldo = (recibo.pago.cuota.monto * total_ejemplares) - (recibo.pago.cuotaPagada + monto_pagado)
            concepto = recibo.pago.evento.nombre
        else:
            saldo = (recibo.pago.paquete.importe * total_ejemplares) - (recibo.pago.cuotaPagada + monto_pagado)
            concepto = recibo.pago.paquete.get_paquete_display()

        no_recibo = recibo.numero_recibo
        dia = recibo.fecha_registro.day
        mes =  recibo.fecha_registro.month
        anio = recibo.fecha_registro.year
        usuario = recibo.pago.cuadra.nombre + ' ' + recibo.pago.cuadra.representante
        importe = '{:,.2f}'.format(recibo.pago.cuotaPagada)
        importe_letra = '(' + Utilities.numero_to_letras(recibo.pago.cuotaPagada) + ' PESOS 00/100 M.N.)'
        concepto_pago = recibo.pago.cuota.tipoCuota.nombre + ' ' + recibo.pago.evento.nombre
        concepto_pago_observaciones = recibo.pago.conceptoPago
        recibido_en = arrReferenciaFormaPago
        saldo = 'SALDO POR PAGAR: ' + '{:,.2f}'.format(saldo)
        cuentas = arrCuentas
        evento = concepto
        ejemplares = ejemplares

        impresion = open('imprime.txt', 'w')
        impresion.write("\n\n\n\n")
        impresion.write("                                                                  " + str(no_recibo) + "\n")
        impresion.write("\n\n\n\n\n")
        impresion.write("                                                                " + str(dia) + "    " + str(mes) + "   " + str(anio) + "\n")
        impresion.write("\n\n")
        impresion.write("              " + str(usuario) + "\n\n")
        impresion.write("              "+ importe + "   " + importe_letra + "\n\n")
        impresion.write("\n")
        impresion.write("              " + concepto_pago + "\n",font('Arial,h1,normal'))
        impresion.write("   EVENTO: " + evento+ "\n")
        i=0
        for caballo in ejemplares:
            if i==0:
                impresion.write("   EJEMPLARES: " + caballo.nombre + ",")
                i+=1
            else:
                impresion.write(caballo.nombre + ",")
        impresion.write("\n\n\n\n\n\n")
        for recibido in recibido_en:
            impresion.write("               " + str(recibido['nombre']) + " "  + str(recibido['referencia']) + " " + recibido['importe'] +  "\n")

        impresion.write("     " + concepto_pago_observaciones + "\n")
        impresion.write("  " + str(saldo) + "                                ")
        i=0
        for cuenta in cuentas:
            if i==0:
                impresion.write(str(cuenta['codigo']) + " " + str(cuenta['importe']) + "\n")
                i += 1
            else:
                impresion.write("                                                                     " + str(cuenta) + "\n")
        impresion.close()
        os.popen("lp imprime.txt")
        return HttpResponse(Utilities.json_to_dumps({"mensaje": "se imprimió correctamente"}), 'application/json; charset=utf-8')

class getListadoElegibles(ListView):

    @staticmethod
    def get_datosReporte(evento_id):
        cuotas_set = []
        descuento = 0
        try:
            all_evento = Evento.objects.get(id=evento_id)

            if all_evento.elegibles_evento != None:
                elegibles = EventoElegibles.objects.filter(
                    Q(elegible_id=all_evento.elegibles_evento) & Q(evento_id=evento_id)).order_by('cuadra__nombre')
            else:
                elegibles = EventoElegibles.objects.filter(
                    Q(elegible_id=all_evento.elegibles_subasta) & Q(evento_id=evento_id)).values('cuadra').annotate(
                    dcount=Count('ejemplar')).order_by('cuadra__nombre')

                cuotas_evento = CuotaEvento.objects.filter(evento_id=evento_id).order_by('fechaVencimiento')
                for cuota in cuotas_evento:
                    if cuota.tipoCuota.id == 2:
                        descuento = cuota.monto - (cuota.monto * all_evento.descuento.porcentaje)
                        print(descuento)
                    if cuota.tipoCuota.id != 2 and cuota.tipoCuota.id != 6:
                        cuotas_set.append(cuota.to_serializable_dict())

                cuadras = []
                i = 0

                for obj in elegibles:
                    # datos de la cuadra
                    cuadra = Cuadras.objects.get(id=obj['cuadra'])
                    if cuadra.nombre=='CUADRA BASTIDA':
                        print('hola')

                    # datos del ejemplar
                    evento_ejemplares = EventoElegibles.objects.filter(
                        Q(elegible_id=all_evento.elegibles_subasta) & Q(evento_id=evento_id) & Q(
                            cuadra_id=obj['cuadra'])).order_by('ejemplar__lote')
                    cuadra_ejemplares = []
                    for evento_ejemplar in evento_ejemplares:
                        i = i + 1

                        # buscar si hay recibo de PU (2) o NOM EXT  (6)
                        pagos_cuota = Recibo.objects.filter(
                            Q(pago__cuota__tipoCuota_id__in=(2, 6))  # & Q(pago__estatus_cuota="PAGADO")
                            & Q(pago__cuadra=cuadra)
                            & Q(pago__ejemplar=evento_ejemplar.ejemplar))

                        registro_unico = {}
                        recibo_unico = False
                        if pagos_cuota:
                            print(pagos_cuota)
                            recibos = []
                            recibo_unico = True
                            for pago_cuota in pagos_cuota:
                                registro_unico = {}
                                recibos.append(pago_cuota.to_serializable_dict_rpt())

                            registro_unico = {
                                'cuota': pago_cuota.pago.cuota,
                                'recibo': recibos
                            }

                        # buscar recibos del ejemplar para este evento
                        ejemplar_recibos = []
                        for obj_cuota in cuotas_evento:
                            if obj_cuota.tipoCuota.id != 2 and obj_cuota.tipoCuota.id != 6:
                                # cuando es recibo de cuota
                                # pagos_cuota = Pago.objects.filter(Q(cuota = obj_cuota) & Q(estatus_cuota="PAGADO") & Q(cuadra = obj_cuadra) & Q(ejemplar = ejemplar_object)) #
                                pagos_cuota = Recibo.objects.filter(
                                    Q(pago__cuota=obj_cuota) & Q(pago__estatus_cuota="PAGADO") & Q(
                                        pago__cuadra=cuadra) & Q(
                                        pago__ejemplar=evento_ejemplar.ejemplar))

                                if pagos_cuota:
                                    recibos = []
                                    for pago_cuota in pagos_cuota:
                                        registro = {}
                                        recibos.append(pago_cuota.to_serializable_dict_rpt())

                                    registro = {
                                        'cuota': pago_cuota.pago.cuota,
                                        'recibo': recibos
                                    }
                                    ejemplar_recibos.append(registro)
                                else:
                                    if recibo_unico:
                                        registro = registro_unico
                                    else:
                                        registro = {
                                            # 'cuadra' : cuadra,
                                            'cuota': obj_cuota.to_serializable_dict(),
                                            'recibo': []
                                        }

                                    ejemplar_recibos.append(registro)

                        data_ejemplar = {
                            'consecutivo': i,
                            'lote': evento_ejemplar.ejemplar.lote,
                            'nombre': evento_ejemplar.ejemplar.nombre,
                            'eventoelegible': evento_ejemplar.id,
                            'estatus': evento_ejemplar.estaus,
                            'recibos': ejemplar_recibos
                        }
                        cuadra_ejemplares.append(data_ejemplar)

                    registro = {
                        'cuadra': cuadra.to_serializable_dict,
                        'ejemplar': cuadra_ejemplares,
                    }

                    cuadras.append(registro)

        except Evento.DoesNotExist:
            return HttpResponse(
                Utilities.json_to_dumps({"error": "No existe lista de elegibles"}),
                'application/json; charset=utf-8')

        params = {
            "cuadras": cuadras,
            "evento": all_evento.to_serializable_dict,
            'cycle': range(0, i),
            "cuotas": cuotas_set,
            'descuento': descuento,
        }

        return params


    @staticmethod
    def setRetirarEjemplar(ejemplar_evento_id):

        EventoElegibles.objects.filter(id=ejemplar_evento_id).update(estaus=1)
        message = True
        return message

    def get(self, request, *args, **kwargs):
        evento_id = request.GET.get('evento_id')
        ejemplar_evento_id = request.GET.get('ejemplar_evento_id')

        if ejemplar_evento_id:
            self.setRetirarEjemplar(ejemplar_evento_id)

        params = self.get_datosReporte(evento_id)

        # from django.template import loader
        # template = loader.get_template('ficha.html')
        # return HttpResponse(template.render(params, request))

        return render(request, 'amcm/listado_elegibles.html', params)

class getListadoElegiblesPDF(ListView):

    def get(self, request, *args, **kwargs):
        evento_id = request.GET.get('evento_id')

        params = getListadoElegibles.get_datosReporte(evento_id)

        return Render.render('amcm/listado_elegibles_pdf.html', params)

class getEventoCuotas(ListView):

    @staticmethod
    def get_datosReporte(evento_id, cuota_id):
        #obtener el set de datos para
        cuotas_set = []
        reporte_cuotas = []
        reporte = []
        aportacion_fondo = []
        total = 0
        descuento = 0
        cuotas_all = []
        cuotas_all.append(cuota_id)
        cuota_obj = CuotaEvento.objects.filter(Q(evento_id=evento_id) & Q(id=cuota_id))
        i = 0
        total_cuota = 0
        fondo_aportacion = 0
        try:
            all_evento = Evento.objects.get(id=evento_id)
            fondo_aportacion = all_evento.fondo
            if all_evento.bolsa > 0:
                response = {
                    'monto_cuota': '{:,.2f}'.format(all_evento.bolsa),
                    'total_cuota': all_evento.bolsa,
                    'cuota': 'AMCM APORTARÁ PARA ESTA CARRERA',
                    'cuadra_ejemplar': ''
                }
                total = total + all_evento.bolsa
                aportacion_fondo.append(response)

            if all_evento.fondo > 0:
                response = {
                    'monto_cuota': '{:,.2f}'.format(all_evento.fondo),
                    'total_cuota': all_evento.fondo,
                    'cuota': 'FONDO: ' + all_evento.descripcion_fondo,
                    'cuadra_ejemplar': ''
                }
                total = total + all_evento.fondo
                aportacion_fondo.append(response)

            cuota_obj = CuotaEvento.objects.filter(Q(evento_id=evento_id) & Q(id=cuota_id))
            for cuota in cuota_obj:
                cuota_obj = cuota

            # obtener las cuotas anteriores a la cuota seleccionada
            cuotas_evento = CuotaEvento.objects.filter(evento_id=evento_id).order_by('fechaVencimiento')
            for cuota in cuotas_evento:
                if cuota.tipoCuota.id == 2:
                    cuotas_all.append(cuota.id)
                    descuento = cuota.monto - (cuota.monto * all_evento.descuento.porcentaje)
                    print(descuento)
                if cuota.tipoCuota.id != 2 and cuota.tipoCuota.id != 6:
                    cuotas_set.append(cuota.to_serializable_dict())

                if cuota_obj:
                    if cuota.fechaVencimiento <= cuota_obj.fechaVencimiento:
                        reporte_cuotas.append(cuota)

            # obtener los montos totales de las cuotas anteriores a la seleccionada y la seleccionada
            if reporte_cuotas:

                for reporte_cuota in reporte_cuotas:
                    total_cuota = 0
                    ejemplares_pago = []
                    cuadra_ejemplares = []
                    # pago__estatus_cuota="PAGADO"
                    #pagos = Recibo.objects.filter(pago__evento=reporte_cuota.evento_id, pago__cuota_id=reporte_cuota.id
                    #                             ).order_by('pago__cuadra').distinct()
                    pagos = Pago.objects.filter(evento=reporte_cuota.evento_id, cuota_id=reporte_cuota.id).order_by('cuadra').distinct()
                    if pagos:


                        for x in pagos:
                            ejemplar_pago_set = x.ejemplar.all()
                            for ejemplar_obj in ejemplar_pago_set:
                                ejemplares_pago.append(ejemplar_obj)

                                i = i + 1
                                total_cuota = total_cuota + 1
                                data = {
                                    'cuadra': ejemplar_obj.cuadra,  # x.pago.cuadra,
                                    'contador': i,
                                    "ejemplar_lote": ejemplar_obj.lote,
                                    "ejemplar_nombre": ejemplar_obj.nombre
                                }

                                cuadra_ejemplares.append(data)

                        # if ejemplares_pago:
                        #     for ejemplar_object in ejemplares_pago:
                        #         i = i+1
                        #         total_cuota = total_cuota+1
                        #         data = {
                        #             'cuadra': ejemplar_object.cuadra, #x.pago.cuadra,
                        #             'contador': i,
                        #             "ejemplar_lote": ejemplar_object.lote,
                        #             "ejemplar_nombre": ejemplar_object.nombre
                        #         }
                        #
                        #         cuadra_ejemplares.append(data)

                        if cuadra_ejemplares:
                            response = {
                                'monto_cuota': '{:,.2f}'.format(reporte_cuota.monto * total_cuota),
                                'total_cuota': total_cuota,
                                'cuota': reporte_cuota,
                                'cuadra_ejemplar': cuadra_ejemplares
                            }
                            total = total + (reporte_cuota.monto * total_cuota)
                            reporte.append(response)

                            # aqui meter lo del fondo fondo_aportacion
                    else:
                        response = {
                            'monto_cuota': '{:,.2f}'.format(0),
                            'total_cuota': 0,
                            'cuota': reporte_cuota,
                            'cuadra_ejemplar': []
                        }
                        total = total + (reporte_cuota.monto * total_cuota)
                        reporte.append(response)

            # reporte lista de ejemplares de la cuota seleccionada
            i = 0
            # ejemplares = Ejemplares.objects.all()
            # ejemplares.query('SELECT `amcm_ejemplares`.`id`, `amcm_ejemplares`.`lote`, `amcm_ejemplares`.`nombre`, `amcm_ejemplares`.`edad`, `amcm_ejemplares`.`peso`, `amcm_ejemplares`.`sexo_id`, `amcm_ejemplares`.`nacionalidad_id`, `amcm_ejemplares`.`color`, `amcm_ejemplares`.`padre`, `amcm_ejemplares`.`madre`, `amcm_ejemplares`.`estatus_id`, `amcm_ejemplares`.`observaciones`, `amcm_ejemplares`.`cuadra_id`,`amcm_pago`.`id`, `amcm_pago`.`evento_id` FROM `amcm_ejemplares` INNER JOIN `amcm_cuadras` ON (`amcm_ejemplares`.`cuadra_id` = `amcm_cuadras`.`id`) INNER JOIN `amcm_pago` ON (`amcm_cuadras`.`id` = `amcm_pago`.`cuadra_id`  ) ORDER BY `amcm_cuadras`.`nombre` ASC, `amcm_ejemplares`.`lote` ASC')
            # for caballo in ejemplares:
            #    print(caballo)
            ejemplares_pago = []
            cuadra_ejemplares_reporte = []
            #pagos = Recibo.objects.filter(pago__evento=evento_id, pago__cuota_id__in=cuotas_all,
            #                              pago__estatus_cuota="PAGADO").order_by('pago__cuadra').distinct()

            pagos = Pago.objects.filter(evento=evento_id, cuota_id__in=cuotas_all).order_by('cuadra').distinct()

            if pagos:
                for ejemplar_obj in pagos:  # ejemplar_pago_set:
                    # ejemplares_pago.append(ejemplar_obj)
                    negritas = 'N'
                    if ejemplar_obj.cuota.id == 172: #todas las cuotas
                        negritas = 'S'
                    ejemplar_pago_set = ejemplar_obj.ejemplar.all()
                    for x in ejemplar_pago_set:
                        i = i + 1
                        data = {
                            'cuadra': x.cuadra,  # x.pago.cuadra,
                            'contador': i,
                            "ejemplar_lote": x.lote,
                            "ejemplar_nombre": x.nombre,
                            'negritas': negritas
                        }
                        cuadra_ejemplares_reporte.append(data)

                # if ejemplares_pago:
                #     for ejemplar_object in ejemplares_pago:
                #
                #         i = i + 1
                #         data = {
                #             'cuadra': ejemplar_object.cuadra,  # x.pago.cuadra,
                #             'contador': i,
                #             "ejemplar_lote": ejemplar_object.lote,
                #             "ejemplar_nombre": ejemplar_object.nombre
                #         }
                #
                #         cuadra_ejemplares_reporte.append(data)
                #

                # if cuotas_evento is not None:
                #     cuota_obj = cuotas_evento.filter()
                #     if cuota_obj:
                #         pagos_cuota = Recibo.objects.filter(
                #             Q(pago__cuota_id=cuota_id) & Q(pago__estatus_cuota="PAGADO") & Q(pago__evento=all_evento)
                #         )
                #
                #
                # i = 0
                #
                #
                #
                #
                #         data_ejemplar = {
                #             'consecutivo': i,
                #             'lote': evento_ejemplar.ejemplar.lote,
                #             'nombre': evento_ejemplar.ejemplar.nombre,
                #             'eventoelegible': evento_ejemplar.id,
                #             'estatus': evento_ejemplar.estaus,
                #             'recibos': ejemplar_recibos
                #         }
                #         cuadra_ejemplares.append(data_ejemplar)
                #
                #     registro = {
                #         'cuadra': cuadra.to_serializable_dict,
                #         'ejemplar': cuadra_ejemplares,
                #     }
                #
                #     cuadras.append(registro)

        except Evento.DoesNotExist:
            return HttpResponse(
                Utilities.json_to_dumps({"error": "No existe lista de elegibles"}),
                'application/json; charset=utf-8')

        dt = datetime.datetime.now()
        dia = dt.strftime("%d")
        mes = dt.strftime("%B").capitalize()
        anio = dt.strftime("%Y")
        fecha = dia + ' de ' + mes + ' del ' + anio
        params = {
            "reporte_cuotas": reporte,
            'aportacion_fondo': aportacion_fondo,
            "evento": all_evento.to_serializable_dict,
            'cycle': range(0, i),
            "cuotas": cuotas_set,
            'descuento': descuento,
            "total": '{:,.2f}'.format(total),
            'titulo': cuota_obj,
            'fecha':fecha,
            "ejemplares_cuota": cuadra_ejemplares_reporte
        }
        print(params)

        return params

    def get(self, request, *args, **kwargs):
        evento_id = request.GET.get('evento_id')
        cuota_id = request.GET.get('cuota_id')

        params = self.get_datosReporte(evento_id, cuota_id)

        return render(request, 'amcm/evento_cuotas.html', params)

class getEventoCuotasPDF(ListView):

    def get(self, request, *args, **kwargs):
        evento_id = request.GET.get('evento_id')
        cuota_id = request.GET.get('cuota_id')

        params = getEventoCuotas.get_datosReporte(evento_id, cuota_id)

        return Render.render('amcm/evento_cuotas_pdf.html', params)


class getReporteEventos(ListView):

    def get(self, request, *args, **kwargs):

        try:
            all_eventos = Evento.objects.filter(tipoEvento=1)
            futurity = []
            for obj in all_eventos:
                futurity.append(obj.to_serializable_dict())

            all_eventos = Evento.objects.filter(tipoEvento=2)
            derby = []
            for obj in all_eventos:
                derby.append(obj.to_serializable_dict())

            all_eventos = Evento.objects.filter(tipoEvento=3)
            clasico = []
            for obj in all_eventos:
                clasico.append(obj.to_serializable_dict())


        except Evento.DoesNotExist:
            return HttpResponse(
                Utilities.json_to_dumps({"error": "No existen Eventos"}),
                'application/json; charset=utf-8')

        params = {
            "futurity": futurity,
            "derby": derby,
            "clasico": clasico
        }

        # from django.template import loader
        # template = loader.get_template('ficha.html')
        # return HttpResponse(template.render(params, request))

        return render(request, 'amcm/reporte.html', params)


class getEventoEjemplares(ListView):

    def get(self, request, *args, **kwargs):

        try:
            all_eventos = Evento.objects.all()

        except Evento.DoesNotExist:
            return HttpResponse(
                Utilities.json_to_dumps({"error": "No existen Eventos"}),
                'application/json; charset=utf-8')

        params = {
            "eventos": all_eventos
        }

        return render(request, 'amcm/ejemplares_eventos.html', params)


class getReporteCuotas(ListView):

    @staticmethod
    def get_datos_reporte(idEvento):

        idEvento = idEvento

        try:
            obj = Evento.objects.get(id=idEvento)

            cuotas_set = []
            cuadras = []
            ejemplar_recibos = []
            cuadras_set = []
            i= 1
            #evento.append(all_evento.to_serializable_dict())
            #obtener las cuotas asociadas al evento
            cuotas_evento = CuotaEvento.objects.filter(evento_id=obj.id).order_by('fechaVencimiento')
            #for cuota in cuotas_evento:
            #    cuotas_set.append(cuota.to_serializable_dict())

            for cuota in cuotas_evento:
                if cuota.tipoCuota.id == 2:
                    descuento = cuota.monto - (cuota.monto * obj.descuento.porcentaje)
                    print(descuento)
                if cuota.tipoCuota.id != 2 and cuota.tipoCuota.id != 6:
                    cuotas_set.append(cuota.to_serializable_dict())


            # los pagos asociados al evento
            i = 0
            all_pagos = Pago.objects.filter(Q(evento=obj.id))
            # obtenener las cuadras distintas encontradas en los pagos
            #cuadras_evento = Pago.objects.filter(Q(evento=obj.id)).values_list('cuadra', flat=True).distinct()
            cuadras_evento = Recibo.objects.filter(Q(pago__evento=obj.id)).values_list('pago__cuadra', flat=True).distinct()
            for obj_cuadra in cuadras_evento:
                cuadra = Cuadras.objects.get(id=obj_cuadra)
                #por cada cuadra  obtengo los ejemplares para obtener los pagos de los ejemplares
                #pagos=Pago.objects.filter(evento=obj,cuadra=cuadra)
                pagos = Recibo.objects.filter(pago__evento=obj, pago__cuadra=cuadra)
                for x in pagos:
                    ejemplar_pago_set=x.pago.ejemplar.all()
                cuadra_ejemplares = []
                cuota_unica=None
                #for pago_ejemplar in pagos:
                #    if cuota_unica!=pago_ejemplar.pago.cuota:
                #        cuota_unica = pago_ejemplar.pago.cuota
                #        ejemplar_pago_set = pago_ejemplar.pago.ejemplar.all()

                #por cada ejemplar obtener los pagos y sus recibos
                for ejemplar_object in ejemplar_pago_set:
                    ejemplar_recibos = []
                    i = i + 1
                    # buscar si hay recibo de PU (2) o NOM EXT  (6)
                    pagos_cuota = Recibo.objects.filter(
                        Q(pago__cuota__tipoCuota_id__in=(2, 4))  # & Q(pago__estatus_cuota="PAGADO")
                        & Q(pago__cuadra=cuadra)
                        & Q(pago__ejemplar=ejemplar_object))

                    registro_unico = {}
                    recibo_unico = False
                    if pagos_cuota:
                        print(pagos_cuota)
                        recibos = []
                        recibo_unico = True
                        for pago_cuota in pagos_cuota:
                            registro_unico = {}
                            recibos.append(pago_cuota.to_serializable_dict())

                        registro_unico = {
                            'cuota': pago_cuota.pago.cuota,
                            'recibo': recibos
                        }


                    for obj_cuota in cuotas_evento:
                        ############
                        pagos_cuota = Recibo.objects.filter(
                            Q(pago__cuota=obj_cuota) & Q(pago__estatus_cuota="PAGADO") & Q(pago__cuadra=obj_cuadra) & Q(
                                pago__ejemplar=ejemplar_object))

                        if obj_cuota.tipoCuota.id != 2 and obj_cuota.tipoCuota.id != 6:
                            # cuando es recibo de cuota
                            # pagos_cuota = Pago.objects.filter(Q(cuota = obj_cuota) & Q(estatus_cuota="PAGADO") & Q(cuadra = obj_cuadra) & Q(ejemplar = ejemplar_object)) #
                            pagos_cuota = Recibo.objects.filter(
                                Q(pago__cuota=obj_cuota) & Q(pago__estatus_cuota="PAGADO") & Q(
                                    pago__cuadra=cuadra) & Q(
                                    pago__ejemplar=ejemplar_object))

                            if pagos_cuota:
                                recibos = []
                                for pago_cuota in pagos_cuota:
                                    registro = {}
                                    recibos.append(pago_cuota.to_serializable_dict())

                                registro = {
                                    'cuota': pago_cuota.pago.cuota,
                                    'recibo': recibos
                                }
                                ejemplar_recibos.append(registro)
                            else:
                                if recibo_unico:
                                    registro = registro_unico
                                else:
                                    registro = {
                                        # 'cuadra' : cuadra,
                                        'cuota': obj_cuota.to_serializable_dict(),
                                        'recibo': []
                                    }

                                ejemplar_recibos.append(registro)

                        ############
                        #pagos_cuota = Pago.objects.filter(Q(cuota = obj_cuota) & Q(estatus_cuota="PAGADO") & Q(cuadra = obj_cuadra) & Q(ejemplar = ejemplar_object)) #

                        # if pagos_cuota:
                        #     recibos = []
                        #     for pago_cuota in pagos_cuota:
                        #         registro = {}
                        #         recibos.append(pago_cuota.to_serializable_dict())
                        #
                        #
                        #     registro = {
                        #         'cuota': pago_cuota.pago.cuota,
                        #         'recibo': recibos
                        #     }
                        #     ejemplar_recibos.append(registro)
                        # else:
                        #     registro = {
                        #         # 'cuadra' : cuadra,
                        #         'cuota': obj_cuota.to_serializable_dict(),
                        #         'recibo': []
                        #     }
                        #     ejemplar_recibos.append(registro)
                    ejemplar = {
                        'contador': i,
                        'ejemplar': ejemplar_object.to_serializable_dict(),
                        'cuotas': ejemplar_recibos
                    }
                    cuadra_ejemplares.append(ejemplar)


                cuadras_data = {
                    'cuadra': cuadra.to_serializable_dict(),
                    'ejemplares': cuadra_ejemplares
                }
                cuadras_set.append(cuadras_data)

        except Evento.DoesNotExist:
            return HttpResponse(
                Utilities.json_to_dumps({"error": "No existen Eventos"}),
                'application/json; charset=utf-8')

        params = {
            "evento": obj.to_serializable_dict(),
            "cuotas": cuotas_set,
            "cuadras": cuadras_set
        }

        return params

    def get(self, request, *args, **kwargs):
        idEvento = 0
        if request.GET.get('id') != '':
            idEvento = request.GET.get('id')

        params = self.get_datos_reporte(idEvento)
        #print(params)
        # from django.template import loader
        # template = loader.get_template('ficha.html')
        # return HttpResponse(template.render(params, request))

        return render(request, 'amcm/reporte_cuota.html', params)


class getReporteCuotasPDF(ListView):

    def get(self, request, *args, **kwargs):
        idEvento = 0
        if request.GET.get('id') != '':
            idEvento = request.GET.get('id')

        params = getReporteCuotas.get_datos_reporte(idEvento)
        # try:
        #     obj = Evento.objects.get(id=idEvento)
        #
        #     cuotas_set = []
        #     cuadras = []
        #     ejemplar_recibos = []
        #     cuadras_set = []
        #     i = 1
        #     # evento.append(all_evento.to_serializable_dict())
        #     # obtener las cuotas asociadas al evento
        #     cuotas_evento = CuotaEvento.objects.filter(evento_id=obj.id).order_by('fechaVencimiento')
        #     for cuota in cuotas_evento:
        #         cuotas_set.append(cuota.to_serializable_dict())
        #
        #     # los pagos asociados al evento
        #     all_pagos = Pago.objects.filter(Q(evento=obj.id))
        #     # obtenener las cuadras distintas encontradas en los pagos
        #     # cuadras_evento = Pago.objects.filter(Q(evento=obj.id)).values_list('cuadra', flat=True).distinct()
        #     cuadras_evento = Recibo.objects.filter(Q(pago__evento=obj.id)).values_list('pago__cuadra',
        #                                                                                flat=True).distinct()
        #     for obj_cuadra in cuadras_evento:
        #         cuadra = Cuadras.objects.get(id=obj_cuadra)
        #         # por cada cuadra  obtengo los ejemplares para obtener los pagos de los ejemplares
        #         # pagos=Pago.objects.filter(evento=obj,cuadra=cuadra)
        #         pagos = Recibo.objects.filter(pago__evento=obj, pago__cuadra=cuadra)
        #         for x in pagos:
        #             ejemplar_pago_set = x.pago.ejemplar.all()
        #         cuadra_ejemplares = []
        #         cuota_unica = None
        #         # for pago_ejemplar in pagos:
        #         #    if cuota_unica!=pago_ejemplar.pago.cuota:
        #         #        cuota_unica = pago_ejemplar.pago.cuota
        #         #        ejemplar_pago_set = pago_ejemplar.pago.ejemplar.all()
        #
        #         # por cada ejemplar obtener los pagos y sus recibos
        #         for ejemplar_object in ejemplar_pago_set:
        #             ejemplar_recibos = []
        #             for obj_cuota in cuotas_evento:
        #                 # pagos_cuota = Pago.objects.filter(Q(cuota = obj_cuota) & Q(estatus_cuota="PAGADO") & Q(cuadra = obj_cuadra) & Q(ejemplar = ejemplar_object)) #
        #                 pagos_cuota = Recibo.objects.filter(
        #                     Q(pago__cuota=obj_cuota) & Q(pago__estatus_cuota="PAGADO") & Q(pago__cuadra=obj_cuadra) & Q(
        #                         pago__ejemplar=ejemplar_object))
        #
        #                 if pagos_cuota:
        #                     recibos = []
        #                     for pago_cuota in pagos_cuota:
        #                         registro = {}
        #                         recibos.append(pago_cuota.to_serializable_dict())
        #
        #                     registro = {
        #                         'cuota': pago_cuota.pago.cuota,
        #                         'recibo': recibos
        #                     }
        #                     ejemplar_recibos.append(registro)
        #                 else:
        #                     registro = {
        #                         # 'cuadra' : cuadra,
        #                         'cuota': obj_cuota.to_serializable_dict(),
        #                         'recibo': []
        #                     }
        #                     ejemplar_recibos.append(registro)
        #             ejemplar = {
        #                 'ejemplar': ejemplar_object.to_serializable_dict(),
        #                 'cuotas': ejemplar_recibos
        #             }
        #             cuadra_ejemplares.append(ejemplar)
        #
        #         cuadras_data = {
        #             'cuadra': cuadra.to_serializable_dict(),
        #             'ejemplares': cuadra_ejemplares
        #         }
        #         cuadras_set.append(cuadras_data)
        #
        #
        # except Evento.DoesNotExist:
        #     params = {
        #         "evento": "",
        #         "cuotas": [],
        #         "cuadras": [],
        #         "mensaje": "No fue posible generar el reporte"
        #     }
        #     return Render.render('amcm/reporte_cuotas_pdf.html', params)
        #
        # params = {
        #     "evento": obj.to_serializable_dict(),
        #     "cuotas": cuotas_set,
        #     "cuadras": cuadras_set,
        #     "mensaje": "success"
        # }

        return Render.renderCuota('amcm/reporte_cuotas_pdf.html', params)


class getReporteCuotasAcumulado(ListView):

    def get(self, request, *args, **kwargs):
        idEvento = 0
        if request.GET.get('id') != '':
            idEvento = request.GET.get('id')

        try:
            obj = Evento.objects.get(id=idEvento)

            cuotas_set = []
            cuadras = []
            ejemplar_recibos = []
            cuadras_set = []
            i= 1
            #evento.append(all_evento.to_serializable_dict())
            #obtener las cuotas asociadas al evento
            cuotas_evento = CuotaEvento.objects.filter(evento_id=obj.id).order_by('fechaVencimiento')
            acumulado_set = []

            for cuota in cuotas_evento:
                cuotas_set.append(cuota.to_serializable_dict())
                #obtener los pagos de la cuota
                total_cuota = 0
                pagos_cuotas = Pago.objects.filter(Q(evento_id=obj.id) & Q(cuota=cuota)).aggregate(total_por_cuota=Sum('cuotaPagada'))
                print(pagos_cuotas)
                pagos_all = Pago.objects.filter(Q(evento_id=obj.id) & Q(cuota=cuota))
                x = 0
                for pago_ejemplar in pagos_all:
                    ejemplares = pago_ejemplar.ejemplar.all()

                    for i in ejemplares:
                        x = x+1

                if pagos_cuotas['total_por_cuota'] == None:
                    total_cuota = 0
                else:
                    total_cuota = '{:,.2f}'.format(pagos_cuotas['total_por_cuota'])

                registro = {
                    'cuota': cuota,
                    'acumulado':  total_cuota,
                    'ejemplares_pago': x
                }
                acumulado_set.append(registro)



        except Evento.DoesNotExist:
            return HttpResponse(
                Utilities.json_to_dumps({"error": "No existen Eventos"}),
                'application/json; charset=utf-8')

        params = {
            "evento": obj.to_serializable_dict(),
            "cuotas": cuotas_set,
            "acumulado": acumulado_set
        }
        #print(params)
        # from django.template import loader
        # template = loader.get_template('ficha.html')
        # return HttpResponse(template.render(params, request))

        return render(request, 'amcm/reporte_cuota_acumulado.html', params)



class getReporteCuotasAcumuladoPDF(ListView):

    def get(self, request, *args, **kwargs):
        idEvento = 0
        if request.GET.get('id') != '':
            idEvento = request.GET.get('id')

        try:
            obj = Evento.objects.get(id=idEvento)

            cuotas_set = []
            cuadras = []
            ejemplar_recibos = []
            cuadras_set = []
            i= 1
            #evento.append(all_evento.to_serializable_dict())
            #obtener las cuotas asociadas al evento
            cuotas_evento = CuotaEvento.objects.filter(evento_id=obj.id).order_by('fechaVencimiento')
            acumulado_set = []

            for cuota in cuotas_evento:
                cuotas_set.append(cuota.to_serializable_dict())
                #obtener los pagos de la cuota
                total_cuota = 0
                pagos_cuotas = Pago.objects.filter(Q(evento_id=obj.id) & Q(cuota=cuota)).aggregate(total_por_cuota=Sum('cuotaPagada'))
                print(pagos_cuotas)
                pagos_all = Pago.objects.filter(Q(evento_id=obj.id) & Q(cuota=cuota))
                x = 0
                for pago_ejemplar in pagos_all:
                    ejemplares = pago_ejemplar.ejemplar.all()

                    for i in ejemplares:
                        x = x+1

                if pagos_cuotas['total_por_cuota'] == None:
                    total_cuota = 0
                else:
                    total_cuota = '{:,.2f}'.format(pagos_cuotas['total_por_cuota'])

                registro = {
                    'cuota': cuota,
                    'acumulado': total_cuota,
                    'ejemplares_pago': x
                }
                acumulado_set.append(registro)

        except Evento.DoesNotExist:
            params = {
                "evento": {},
                "cuotas": [],
                "acumulado": [],
                "message": "success"
            }
            return Render.render('amcm/reporte_cuotas_pdf.html', params)

        params = {
            "evento": obj.to_serializable_dict(),
            "cuotas": cuotas_set,
            "acumulado": acumulado_set,
            "message": "success"
        }

        return Render.renderCuota('amcm/reporte_cuotas_acumulado_pdf.html', params)


class getReporteLista(ListView):

    def get(self, request, *args, **kwargs):
        idEvento = 0
        if request.GET.get('id') != '':
            idEvento = request.GET.get('id')

        try:
            obj = Evento.objects.get(id=idEvento)

            cuotas_set = []
            cuadras = []
            ejemplar_recibos = []
            cuadras_set = []
            i= 1
            #evento.append(all_evento.to_serializable_dict())
            #obtener las cuotas asociadas al evento
            cuotas_evento = CuotaEvento.objects.filter(evento_id=obj.id).order_by('fechaVencimiento')
            acumulado_set = []

            for cuota in cuotas_evento:
                cuotas_set.append(cuota.to_serializable_dict())
                #obtener los pagos de la cuota
                total_cuota = 0
                pagos_cuotas = Pago.objects.filter(Q(evento_id=obj.id) & Q(cuota=cuota)).aggregate(total_por_cuota=Sum('cuotaPagada'))
                print(pagos_cuotas)
                pagos_all = Pago.objects.filter(Q(evento_id=obj.id) & Q(cuota=cuota))
                x = 0
                for pago_ejemplar in pagos_all:
                    ejemplares = pago_ejemplar.ejemplar.all()

                    for i in ejemplares:
                        x = x+1

                if pagos_cuotas['total_por_cuota'] == None:
                    total_cuota = 0
                else:
                    total_cuota = '{:,.2f}'.format(pagos_cuotas['total_por_cuota'])

                registro = {
                    'cuota': cuota,
                    'acumulado': total_cuota,
                    'ejemplares_pago': x
                }
                acumulado_set.append(registro)

        except Evento.DoesNotExist:
            params = {
                "evento": {},
                "cuotas": [],
                "acumulado": [],
                "message": "success"
            }
            return Render.render('amcm/reporte_futurity-garanones-rg2.html', params)

        params = {
            "evento": obj.to_serializable_dict(),
            "cuotas": cuotas_set,
            "acumulado": acumulado_set,
            "message": "success"
        }

        return Render.renderCuota('amcm/reporte_futurity-garanones-rg2.html', params)


class getDashboard(ListView):

    def get(self, request, *args, **kwargs):

        total_cuadras_ejemplares = []
        eventos_temporada = []
        nominados_set = []
        try:
            today = datetime.datetime.now()

            #conteo general de ejemplares, cuadras, eventos
            eventos = Evento.objects.filter(Q(temporada=str(today.year))).count()
            ejemplares = Ejemplares.objects.count()
            cuadras = Cuadras.objects.count()
            pagos = Pago.objects.filter(Q(fechaPago__year=str(today.year))).aggregate(total=Sum('cuotaPagada'))
            eventos_set = Evento.objects.all()

            #recibos vs pagos
            reporte_recibos_pagos = []
            for obj_evento in eventos_set:
                recibos_obj = Recibo.objects.filter(Q(pago__evento = obj_evento)).values('pago__evento__nombre',) \
                    .annotate(
                    total=Count('pago__evento__nombre'), monto=Sum('pago__cuotaPagada')).order_by()

                pagos_obj = Pago.objects.filter(Q(evento = obj_evento)).values('evento__nombre',).annotate(
                    total=Count('evento__nombre'), monto=Sum('cuotaPagada')).order_by()

                numero_recibos = 0
                numero_pagos = 0
                monto_recibo = 0
                monto_pago = 0
                for total_recibo in recibos_obj:
                    numero_recibos = total_recibo['total']
                    monto_recibo = total_recibo['monto']

                for total_pagos in pagos_obj:
                    numero_pagos = total_pagos['total']
                    monto_pago = total_pagos['monto']

                data = {
                    'evento': obj_evento.nombre,
                    'numero_recibos': numero_recibos,
                    'monto_recibo': monto_recibo,
                    'numero_pagos': numero_pagos,
                    'monto_pago': monto_pago,
                }

                reporte_recibos_pagos.append(data)

            #relacion de cuadras y ejemplares
            cuadras_ejemplares = Ejemplares.objects.values('cuadra__nombre').annotate(total=Count('cuadra__nombre')).order_by()
            for obj in cuadras_ejemplares:
                data = {
                    'cuadra': obj['cuadra__nombre'],
                    'ejemplares': obj['total']
                }
                total_cuadras_ejemplares.append(data)

            #eventos de la temporada
            #eventos_obj = Evento.objects.filter(Q(temporada=str(today.year)))

            eventos_obj = CuotaEvento.objects.filter(Q(evento__temporada=str(today.year)) & Q(tipoCuota_id__in=(1,11,15))).order_by('fechaVencimiento')
            for obj in eventos_obj:
                cuotas_set = []
                fechas_set = []
                condicion_set = []
                cuotas_obj = CuotaEvento.objects.filter(Q(evento_id=obj.evento_id) & Q(tipoCuota_id__in=(1,3,11,12,13,15))).order_by('fechaVencimiento')
                for cuota in cuotas_obj:
                    cuota_data = {
                    "cuotaFecha": str(cuota.fechaVencimiento.strftime("%d-%m-%Y")),
                    "cuotaMonto": cuota.monto
                    }
                    cuotas_set.append(cuota_data)

                fechas_obj = FechasEvento.objects.filter(Q(evento_id=obj.evento_id) & Q(tipoFecha_id__in=(1,3))).order_by('tipoFecha_id')
                for fecha in fechas_obj:
                    fecha_data = {
                    "tipoFecha": fecha.tipoFecha.nombre,
                    "fecha": str(fecha.fecha.strftime("%d-%m-%Y"))
                    }
                    fechas_set.append(fecha_data)

                condicion_obj = CondicionesEvento.objects.filter(Q(evento_id=obj.evento_id))
                for condicion in condicion_obj:
                    condicion_data = {
                        'condicion': condicion.especificacion
                    }
                    condicion_set.append(condicion_data)

                data = {
                    'nombre': obj.evento.nombre,
                    'cuotas': cuotas_set,
                    'fechas': fechas_set,
                    'condicion': condicion_set,
                    'distancia': obj.evento.yardas,
                    'tipo': obj.evento.tipoEvento.nombre,
                }
                eventos_temporada.append(data)

            #nominados vs inscritos
            nominados_obj = EventoElegibles.objects.values('evento__nombre', 'elegible__nombre').annotate(total=Count('evento__nombre')).order_by()
            for nominados in nominados_obj:
                nominados_data = {
                    'evento': nominados['evento__nombre'],
                    'ejemplares': nominados['total'],
                    'elegible': nominados['elegible__nombre'],
                }
                nominados_set.append(nominados_data)

                # recibos
                recibos_set = []                                                   #'pago__cuotaPagada'
                recibos_obj = Recibo.objects.values('pago__evento__nombre', 'pago__cuota__tipoCuota__nombre')\
                    .annotate(total=Count('pago__evento__nombre')).order_by() #.aggregate(total_monto=Sum('pago__cuotaPagada'))\

                for recibo in recibos_obj:
                    recibos_data = {
                        'evento': recibo['pago__evento__nombre'],
                        'total': recibo['total'],
                        #'monto': recibo['total_monto'],
                        'cuota': recibo['pago__cuota__tipoCuota__nombre'],
                    }
                    recibos_set.append(recibos_data)

        except Evento.DoesNotExist:
            params = {
                "eventos": 0,
                "ejemplares": 0,
                "cuadras": 0,
                "pagos": 0,
                "cuadras_ejemplares": [],
                "eventos_temporada": [],
                'nominados': [],
                'recibos_pagos': [],
                "message": "error"
            }
            return HttpResponse(Utilities.json_to_dumps(params), 'application/json; charset=utf-8')

        params = {
            "eventos": eventos,
            "ejemplares": ejemplares,
            "cuadras": cuadras,
            "pagos": pagos['total'],
            "cuadras_ejemplares": total_cuadras_ejemplares,
            "eventos_temporada": eventos_temporada,
            'nominados': nominados_set,
            'recibos':recibos_set,
            'recibos_pagos': reporte_recibos_pagos,
            "message": "success",
        }

        return HttpResponse(Utilities.json_to_dumps(params), 'application/json; charset=utf-8')

@method_decorator(csrf_exempt, name='dispatch')
class getParentesis(ListView):
    def json_to_dumps(self,json_object):
        return json.dumps(json_object, indent=4, separators=(',', ': '), sort_keys=False, ensure_ascii=False)

    def post(self, request, *args, **kwargs):
        datos = json.loads(request.body)
        cadena = datos["cadena"]
        contador=0
        for i in cadena:
            if i=='(':
                contador+=1
            else:
                contador-=1

        if contador==0:
            message='True'
        else:
            message ='False'

        params = {

            "message": message
        }

        return HttpResponse(self.json_to_dumps(params), 'application/json; charset=utf-8')

@method_decorator(csrf_exempt, name='dispatch')
class wordsReversed(ListView):
    def json_to_dumps(self,json_object):
        return json.dumps(json_object, indent=4, separators=(',', ': '), sort_keys=False, ensure_ascii=False)

    def post(self, request, *args, **kwargs):
        datos = json.loads(request.body)
        cadena = datos["cadena"].split(' ')
        reverseWord=''
        for word in cadena:
            if len(word)>=5:
                reverseWord += word[::-1] + ' '
            else:
                reverseWord+=word + ' '

        params = {

            "message": reverseWord.rstrip()
        }

        return HttpResponse(self.json_to_dumps(params), 'application/json; charset=utf-8')


#reporte de recibos realizados
class getReporteRecibos(ListView):

    @staticmethod
    def get_datos_reporte(idEvento, fecha_de, fecha_a):
        filtros = "Recibos  "
        recibos_set = []
        evento_set = []
        recibos = Recibo.objects.all()
        try:
            evento_set = Evento.objects.all()

            if idEvento is None and fecha_de is None :
                recibos = Recibo.objects.all()
            elif idEvento is not None:
                recibos = recibos.filter(Q(pago__evento=idEvento))
                evento_filtro = Evento.objects.get(id=idEvento)
                filtros = filtros + "  del:  " + evento_filtro.nombre
                if fecha_de is not None:
                    recibos = recibos.filter(Q(fecha_registro__range=(fecha_de,fecha_a)))
                    filtros = filtros + "  del periodo:  " + str(fecha_de.date()) + "  al:  " + str(fecha_a.date())
            elif fecha_de is not None:
                recibos = recibos.filter(Q(fecha_registro__range=(fecha_de,fecha_a)))
                filtros = filtros + " del periodo: " + str(fecha_de.date()) + " al: " + str(fecha_a.date())

            for object_recibo in recibos:
                recibos_data = {
                    'numero': object_recibo.numero_recibo,
                    'pago': object_recibo.pago.to_serializable_dict(),

                }
                recibos_set.append(recibos_data)

        except Evento.DoesNotExist:
            return HttpResponse(
                Utilities.json_to_dumps({"error": "No existen Recibos"}),
                'application/json; charset=utf-8')

        params = {
            "recibos": recibos_set,
            "eventos": evento_set,
            'filtros': filtros,
        }

        return params

    def get(self, request, *args, **kwargs):

        idEvento = None
        fecha_de = None
        fecha_a = None
        if request.GET.get('evento_id') is not None and request.GET.get('evento_id') != '':
            idEvento = request.GET.get('evento_id')

        if request.GET.get('fecha_de') is not None and request.GET.get('fecha_de') != '':
            getFecha = request.GET.get('fecha_de')
            fecha_de = datetime.datetime.strptime(getFecha, '%m/%d/%Y')

        if request.GET.get('fecha_a') is not None and request.GET.get('fecha_a') != '':
            getFecha = request.GET.get('fecha_a')
            fecha_a = datetime.datetime.strptime(getFecha, '%m/%d/%Y')

        params = self.get_datos_reporte(idEvento, fecha_de, fecha_a)

        return render(request, 'amcm/reporte_recibos.html', params)

from django.contrib.admin.views.decorators import staff_member_required

class AdminRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(AdminRequiredMixin, cls).as_view(**initkwargs)
        return staff_member_required(view)

#reporte de deudores
from notion.client import NotionClient
from notion.block import FramerBlock, VideoBlock,PageBlock,EmbedBlock
class getViewDeudores(ListView):

    @staticmethod
    def get_cuadras():

        cuadras_set = Cuadras.objects.all()

        params = {
            "cuadras": cuadras_set
        }

        return params

    def get(self, request, *args, **kwargs):
        # Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
        ##client = NotionClient(token_v2="d7ee991a7879908ccbf32a3287122176b925a2cf67944af0516338a6b8226e1dc60b41d51c385c1dabf134fdf464fb45de5dc9c21f2ed701c8a2a4eb516c5e6c60356b8cda14f2978a461fc0fda9")

        # Replace this URL with the URL of the page you want to edit
        ##page = client.get_block("https://www.notion.so/HI-97da578e14a24347b14aa9d8f5434126")
        ##video = page.children.add_new(VideoBlock, width=200)
        # sets "property.source" to the URL, and "format.display_source" to the embedly-converted URL
        ##video.set_source_url("https://www.youtube.com/watch?v=yKUM45-LuHk")

        params = self.get_cuadras()

        return render(request, 'amcm/vista_reporte_deudores.html', params)

#reporte de pagos generales
class getViewPagos(ListView):

    @staticmethod
    def get_cuadras():

        cuadras_set = Cuadras.objects.all()

        params = {
            "cuadras": cuadras_set
        }

        return params

    def get(self, request, *args, **kwargs):
        params = self.get_cuadras()

        return render(request, 'amcm/vista_reporte_pagos.html', params)

class getReporteRecibosPDF(ListView):
    def get(self, request, *args, **kwargs):

        idEvento = None
        fecha_de = None
        fecha_a = None
        if request.GET.get('evento_id') is not None and request.GET.get('evento_id') != '':
            idEvento = request.GET.get('evento_id')

        if request.GET.get('fecha_de') is not None and request.GET.get('fecha_de') != '':
            getFecha = request.GET.get('fecha_de')
            fecha_de = datetime.datetime.strptime(getFecha, '%m/%d/%Y')

        if request.GET.get('fecha_a') is not None and request.GET.get('fecha_a') != '':
            getFecha = request.GET.get('fecha_a')
            fecha_a = datetime.datetime.strptime(getFecha, '%m/%d/%Y')

        params = getReporteRecibos.get_datos_reporte(idEvento, fecha_de, fecha_a)

        return Render.renderCuota('amcm/reporte_recibos_pdf.html', params)


@method_decorator(csrf_exempt, name='dispatch')
class setRetirarEjemplar(ListView):

    def get(self, request, *args, **kwargs):
        evento_ejemplar_id = request.GET.get('evento_ejemplar_id')

        EventoElegibles.objects.filter(id=evento_ejemplar_id).update(estaus=1)
        message = "retirado"
        params = {
            "message": "success",
            "estatus": message
        }

        return HttpResponse(Utilities.json_to_dumps(params), 'application/json; charset=utf-8')

@method_decorator(csrf_exempt, name='dispatch')
class getEstadoCuentaXCuadraXls(ListView):
    def get(self, request, *args, **kwargs):
        cuadra_id = request.GET.get('cuadra_id')
        pagos = Pago.objects.filter(cuadra__id=cuadra_id, tuvo_credito=True)
        if pagos.count()>0:
            cuadra = {'id':pagos[0].cuadra.id,'nombre':pagos[0].cuadra.nombre}
            arrPagos=[]
            saldo=0
            for pago in pagos:
                saldo+=pago.cuota.monto
                ejemplares=''
                for ejemplar in pago.ejemplar.all():
                    if ejemplares=='':
                        ejemplares += ejemplar.nombre
                    else:
                        ejemplares += ',' + ejemplar.nombre
                arrPagos.append({'fecha':str(pago.cuota.fechaVencimiento.strftime("%d/%m/%Y")).upper(),
                                 'concepto': pago.cuota.tipoCuota.nombre + ' ' + pago.evento.nombre ,
                                 'ejemplares':'(' + ejemplares + ')',
                                 'debe':'{:,.2f}'.format(pago.cuota.monto),'haber':'{:,.2f}'.format(0),'saldo':'{:,.2f}'.format(saldo)})

            pagos = ReferenciaFormaPago.objects.filter(pago__cuadra__id=cuadra_id, pago__tuvo_credito=True).\
                values('formapago__nombre','referencia','importe','fecha_registro').distinct()
            saldo_referencia=0
            saldo_final=0
            for pago in pagos:
                saldo_referencia+=pago['importe']
                saldo_final = saldo - saldo_referencia
                arrPagos.append({'fecha': str(pago['fecha_registro'].strftime("%d/%m/%Y")).upper(),
                                 'concepto': pago['formapago__nombre'] + ' ' + pago['referencia'],
                                 'ejemplares': '',
                                 'debe': '{:,.2f}'.format(0), 'haber': '{:,.2f}'.format(pago['importe']), 'saldo': '{:,.2f}'.format(saldo_final)})
                print (pago)

            params = {'cuadra': cuadra,'estado_cuenta': arrPagos, 'fecha_reporte':now()}
        else:
            params = {'cuadra': '','estado_cuenta': []}

        return Render.render('amcm/estado_cuenta.html', params)

        #return HttpResponse(Utilities.json_to_dumps(params), 'application/json; charset=utf-8')

@method_decorator(csrf_exempt, name='dispatch')
class setEstadoCuentaXCuadra(ListView):
    def get(self, request, *args, **kwargs):
        cuadra_id = request.GET.get('cuadra_id')
        pagos = Pago.objects.filter(cuadra__id=cuadra_id, tuvo_credito=True)
        if pagos.count()>0:
            obj_cuadra = pagos[0].cuadra
            arrPagos=[]
            saldo=0
            for pago in pagos:
                saldo+=pago.cuota.monto
                ejemplares = ''
                for ejemplar in pago.ejemplar.all():
                    if ejemplares == '':
                        ejemplares += ejemplar.nombre
                    else:
                        ejemplares += ',' + ejemplar.nombre
                arrPagos.append({'fecha':pago.cuota.fechaVencimiento,
                                 'concepto':pago.cuota.tipoCuota.nombre + ' ' + pago.evento.nombre,
                                 'ejemplares':'(' + ejemplares + ')',
                                 'debe':pago.cuota.monto,'haber':0,'saldo':saldo})

            pagos = ReferenciaFormaPago.objects.filter(pago__cuadra__id=cuadra_id, pago__tuvo_credito=True).\
                values('formapago__nombre','referencia','importe','fecha_registro').distinct()
            saldo_referencia=0
            saldo_final=0
            for pago in pagos:
                saldo_referencia+=pago['importe']
                saldo_final = saldo - saldo_referencia
                arrPagos.append({'fecha': pago['fecha_registro'],
                                 'concepto': pago['formapago__nombre'] + ' ' + pago['referencia'],
                                 'ejemplares': '',
                                 'debe': 0, 'haber': pago['importe'], 'saldo': saldo_final})

            estado_cuenta = EstadoCuenta()
            estado_cuenta.cuadra=obj_cuadra
            estado_cuenta.nombre_cuadra = obj_cuadra.nombre
            estado_cuenta.saldo = saldo_final
            estado_cuenta.save()

            for pago in arrPagos:
                detalle_estado_cuenta = EstadoCuentaDetalle()
                detalle_estado_cuenta.estado_cuenta = estado_cuenta
                detalle_estado_cuenta.fecha = pago['fecha']
                detalle_estado_cuenta.concepto = pago['concepto']
                detalle_estado_cuenta.ejemplares = pago['ejemplares']
                detalle_estado_cuenta.debe = pago['debe']
                detalle_estado_cuenta.haber = pago['haber']
                detalle_estado_cuenta.saldo = pago['saldo']
                detalle_estado_cuenta.save()



            params = {
                "message": "Se generó correctamente el registro del estado de cuenta",
                "estatus": 'ok',
            }
        else:
            params = {
                "message": "No Existe Información para registrar",
                "estatus": 'error'
            }

        return HttpResponse(Utilities.json_to_dumps(params), 'application/json; charset=utf-8')

# pagos totales por cuadra
@method_decorator(csrf_exempt, name='dispatch')
class getEstadoCuentaXCuadraGeneral(ListView):
    def get(self, request, *args, **kwargs):
        cuadra_id = request.GET.get('cuadra_id')
        pagos = Pago.objects.filter(cuadra__id=cuadra_id)
        if pagos.count()>0:
            cuadra = {'id':pagos[0].cuadra.id,'nombre':pagos[0].cuadra.nombre}
            arrPagos=[]
            saldo=0
            for pago in pagos:

                ejemplares=''
                ejemplares_count=0
                for ejemplar in pago.ejemplar.all():
                    if ejemplares=='':
                        ejemplares += ejemplar.nombre
                    else:
                        ejemplares += ',' + ejemplar.nombre
                    ejemplares_count +=1
                saldo += (pago.cuota.monto*ejemplares_count)
                recibos = ''
                for recibo in pago.recibo_set.all():
                    if recibos=='':
                        recibos += str(recibo.numero_recibo)
                        if recibo.letra is not None:
                            recibos += '-' + recibo.letra
                    else:
                        recibos += ',' + str(recibo.numero_recibo)
                        if recibo.letra is not None:
                            recibos += '-' + recibo.letra

                arrPagos.append({'fecha':str(pago.cuota.fechaVencimiento.strftime("%d/%m/%Y")).upper(),
                                 'concepto': pago.cuota.tipoCuota.nombre + ' ' + pago.evento.nombre ,
                                 'ejemplares':'(' + ejemplares + ')',
                                 'recibos':recibos,
                                 'debe':'{:,.2f}'.format(pago.cuota.monto*ejemplares_count),'haber':'{:,.2f}'.format(0),'saldo':'{:,.2f}'.format(saldo)})

            pagos = ReferenciaFormaPago.objects.filter(pago__cuadra__id=cuadra_id).\
                values('pago__recibo__numero_recibo','formapago__nombre','referencia','importe','importe_pago','fecha_registro')
            saldo_referencia=0
            saldo_final=0

            for pago in pagos:

                saldo_referencia+=pago['importe_pago']
                saldo_final = saldo - saldo_referencia
                arrPagos.append({'fecha': str(pago['fecha_registro'].strftime("%d/%m/%Y")).upper(),
                                 'concepto': pago['formapago__nombre'] + ' ' + pago['referencia'] + ' (' + '{:,.2f}'.format(pago['importe']) + ')',
                                 'ejemplares': '',
                                 'recibos':pago['pago__recibo__numero_recibo'] ,
                                 'debe': '{:,.2f}'.format(0), 'haber': '{:,.2f}'.format(pago['importe_pago']), 'saldo': '{:,.2f}'.format(saldo_final)})
                print (pago)

            params = {'cuadra': cuadra,'estado_cuenta': arrPagos, 'fecha_reporte':now()}
        else:
            params = {'cuadra': '','estado_cuenta': []}

        return Render.render('amcm/estado_cuenta_pagos.html', params)