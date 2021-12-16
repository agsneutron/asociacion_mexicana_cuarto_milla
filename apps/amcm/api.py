# coding=utf-8
import io
import json

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from requests import RequestException

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.utils import timezone
import six as StringIO
from apps.amcm.models import *
from apps.lib.utilities import Utilities


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
    def render(path, params):
        filename = 'recibo.pdf'
        template = get_template(path)
        html = template.render(params)
        response = io.buffer = BytesIO()

        #pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), response, path=path)
        #https://www.it-swarm-es.com/es/django/django-pisa-agregar-imagenes-pdf-salida/968337910/

        pdf = pisa.CreatePDF(io.BytesIO(html.encode("UTF-8")), response,link_callback=path)
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
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
    def get(self, request, *args, **kwargs):
        anterior=False;
        recibo_id = request.GET.get('recibo_id')
        recibo = Recibo.objects.get(id=recibo_id)
        saldo=recibo.pago.cuota.monto - recibo.pago.cuotaPagada

        params = {
            'no_recibo': recibo.numero_recibo,
            'dia':recibo.fecha_registro.day,
            'mes': recibo.fecha_registro.month,
            'anio': recibo.fecha_registro.year,
            'usuario': recibo.pago.cuadra.nombre +' '+ recibo.pago.cuadra.representante,
            'importe':'{:,.2f}'.format(recibo.pago.cuotaPagada),
            'importe_letra': '(' + Utilities.numero_to_letras(recibo.pago.cuotaPagada) + ' PESOS 00/100 M.N.)',
            'concepto': recibo.pago.conceptoPago,
            'recibido_en': recibo.pago.valorRecibido,
            'saldo': 'SALDO POR PAGAR: ' + '{:,.2f}'.format(saldo),
            }



        return Render.render('amcm/recibo.html', params)


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


class getReporteCuotas(ListView):

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
            for cuota in cuotas_evento:
                cuotas_set.append(cuota.to_serializable_dict())

            # los pagos asociados al evento
            all_pagos = Pago.objects.filter(Q(evento=obj.id))
            # obtenener las cuadras distintas encontradas en los pagos
            cuadras_evento = Pago.objects.filter(Q(evento=obj.id)).values_list('cuadra', flat=True).distinct()
            for obj_cuadra in cuadras_evento:
                cuadra = Cuadras.objects.get(id=obj_cuadra)
                #por cada cuadra  obtengo los ejemplares para obtener los pagos de los ejemplares
                cuadra_ejemplares = []
                for pago_ejemplar in all_pagos:
                    ejemplar_pago_set = pago_ejemplar.ejemplar.all()
                    #cuadra_ejemplares = []

                    #por cada ejemplar obtener los pagos y sus recibos
                    for ejemplar_object in ejemplar_pago_set:
                        ejemplar_recibos = []
                        for obj_cuota in cuotas_evento:
                            pago_cuota = Pago.objects.filter(Q(cuota = obj_cuota) & Q(estatus_cuota="PAGADO") & Q(cuadra = obj_cuadra) & Q(ejemplar = ejemplar_object)) #
                            if pago_cuota:
                                registro = {}
                                #ejemplar_recibos = []
                                for ejemplar_cuota_pago in pago_cuota:
                                    recibo_pago = Recibo.objects.filter(Q(pago=ejemplar_cuota_pago))
                                    recibos = []
                                    if recibo_pago:
                                        for recibo in recibo_pago:
                                            recibos.append(recibo.to_serializable_dict())
                                    registro = {
                                        #'cuadra' : cuadra,
                                        'cuota': ejemplar_cuota_pago.cuota,
                                        'recibo': recibos
                                    }
                                ejemplar_recibos.append(registro)
                            else:
                                registro = {
                                    # 'cuadra' : cuadra,
                                    'cuota': obj_cuota.to_serializable_dict(),
                                    'recibo': []
                                }
                                ejemplar_recibos.append(registro)
                        ejemplar = {
                            'ejemplar': ejemplar_object.to_serializable_dict(),
                            'cuotas': ejemplar_recibos
                        }
                    cuadra_ejemplares.append(ejemplar)
                cuadras_data = {
                    'cuadra' : cuadra.to_serializable_dict(),
                    'ejemplares' : cuadra_ejemplares
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
        #print(params)
        # from django.template import loader
        # template = loader.get_template('ficha.html')
        # return HttpResponse(template.render(params, request))

        return render(request, 'amcm/reporte-cuota.html', params)


class getReporteCuotasPDF(ListView):

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
            cuotas_evento = CuotaEvento.objects.filter(evento_id=obj.id).order_by('fechaVencimiento')
            for cuota in cuotas_evento:
                cuotas_set.append(cuota.to_serializable_dict())

            all_pagos = Pago.objects.filter(Q(evento=obj.id))
            cuadras_evento = Pago.objects.filter(Q(evento=obj.id)).values_list('cuadra', flat=True).distinct()
            for obj_cuadra in cuadras_evento:
                cuadra = Cuadras.objects.get(id=obj_cuadra)
                cuadra_ejemplares = []
                for pago_ejemplar in all_pagos:
                    ejemplar_pago_set = pago_ejemplar.ejemplar.all()
                    for ejemplar_object in ejemplar_pago_set:
                        for obj_cuota in cuotas_evento:
                            pago_cuota = Pago.objects.filter(Q(cuota = obj_cuota) & Q(estatus_cuota="PAGADO") & Q(cuadra = obj_cuadra) & Q(ejemplar = ejemplar_object)) #
                            if pago_cuota:
                                registro = {}
                                ejemplar_recibos = []
                                for ejemplar_cuota_pago in pago_cuota:
                                    recibo_pago = Recibo.objects.filter(Q(pago=ejemplar_cuota_pago))
                                    recibos = []
                                    if recibo_pago:
                                        for recibo in recibo_pago:
                                            recibos.append(recibo.to_serializable_dict())
                                    registro = {
                                        #'cuadra' : cuadra,
                                        'cuota': ejemplar_cuota_pago.cuota,
                                        'recibo': recibos
                                    }
                                ejemplar_recibos.append(registro)
                            else:
                                registro = {
                                    # 'cuadra' : cuadra,
                                    'cuota': obj_cuota.to_serializable_dict(),
                                    'recibo': []
                                }
                                ejemplar_recibos.append(registro)
                            ejemplar = {
                                'ejemplar': ejemplar_object.to_serializable_dict(),
                                'cuotas': ejemplar_recibos
                            }
                        cuadra_ejemplares.append(ejemplar)
                    cuadras_data = {
                        'cuadra' : cuadra.to_serializable_dict(),
                        'ejemplares' : cuadra_ejemplares
                    }
                    cuadras_set.append(cuadras_data)

        except Evento.DoesNotExist:
            params = {
                "evento": "",
                "cuotas": [],
                "cuadras": [],
                "mensaje": "No fue posible generar el reporte"
            }
            return Render.render('amcm/reporte-cuota-pdf.html', params)

        params = {
            "evento": obj.to_serializable_dict(),
            "cuotas": cuotas_set,
            "cuadras": cuadras_set,
            "mensaje": "success"
        }

        return Render.renderCuota('amcm/reporte-cuota-pdf.html', params)