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
        filename = 'recibo'+ str(datetime.datetime.now()) +'.pdf'
        template = get_template(path)
        html = template.render(params)
        response = io.buffer = BytesIO()
        #response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        #pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), response, path=path)
        #https://www.it-swarm-es.com/es/django/django-pisa-agregar-imagenes-pdf-salida/968337910/


        pdf = pisa.CreatePDF(io.BytesIO(html.encode("UTF-8")), response,link_callback=path)

        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
            response.flush()
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
        ejemplares=recibo.pago.ejemplar.all()
        total_ejemplares=0
        monto_pagado=0
        for ejemplar in ejemplares:
            total_ejemplares +=1
        pagos = Pago.objects.filter(evento=recibo.pago.evento,cuota=recibo.pago.cuota,cuadra=recibo.pago.cuadra,id__lt=recibo.pago.id)
        for pago in pagos:
            if set(list(ejemplares)) == set(list(pago.ejemplar.all())):
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
                'fecha': referencia.fecha_registro
            }
            arrReferenciaFormaPago.append(referencia_json)

        if recibo.pago.cuota:
            conceptoCuotas = recibo.pago.cuota.tipoCuota.nombre
            if recibo.pago.cuota.tipoCuota.tipo == 'EVENTO':
                if recibo.pago.cuota.tipoCuota.id == 2:
                    descuento = recibo.pago.cuota.monto*recibo.pago.evento.descuento.porcentaje
                    descuento = descuento*total_ejemplares
                    monto_a_pagar = recibo.pago.cuota.monto*total_ejemplares

                    saldo=(monto_a_pagar - descuento) - (recibo.pago.cuotaPagada+monto_pagado)
                else:
                    saldo=(recibo.pago.cuota.monto*total_ejemplares) - (recibo.pago.cuotaPagada+monto_pagado)
            else:
                saldo = 0.00
            concepto=recibo.pago.evento.nombre
        else:
            conceptoCuotas = recibo.pago.paquete.get_paquete_display()
            saldo=(recibo.pago.paquete.importe*total_ejemplares) - (recibo.pago.cuotaPagada+monto_pagado)

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

                    # datos del ejemplar
                    evento_ejemplares = EventoElegibles.objects.filter(
                        Q(elegible_id=all_evento.elegibles_subasta) & Q(evento_id=evento_id) & Q(
                            cuadra_id=obj['cuadra'])).order_by('ejemplar__lote')
                    cuadra_ejemplares = []
                    for evento_ejemplar in evento_ejemplares:
                        i = i + 1

                        # buscar si hay recibo de PU (2) o NOM EXT  (6)
                        pagos_cuota = Recibo.objects.filter(
                            Q(pago__cuota__tipoCuota_id__in=(2, 4))  # & Q(pago__estatus_cuota="PAGADO")
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
                                recibos.append(pago_cuota.to_serializable_dict())

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
        total = 0
        descuento = 0
        cuotas_all = []
        cuotas_all.append(cuota_id)
        cuota_obj = CuotaEvento.objects.filter(Q(evento_id=evento_id) & Q(id=cuota_id))
        i = 0
        total_cuota = 0
        try:
            all_evento = Evento.objects.get(id=evento_id)
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
                    pagos = Recibo.objects.filter(pago__evento=reporte_cuota.evento_id, pago__cuota_id=reporte_cuota.id,
                                                  pago__estatus_cuota="PAGADO").order_by('pago__cuadra').distinct()
                    if pagos:
                        for x in pagos:
                            ejemplar_pago_set = x.pago.ejemplar.all()
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
                                'monto_cuota': reporte_cuota.monto * total_cuota,
                                'total_cuota': total_cuota,
                                'cuota': reporte_cuota,
                                'cuadra_ejemplar': cuadra_ejemplares
                            }
                            total = total + (reporte_cuota.monto * total_cuota)
                            reporte.append(response)
                    else:
                        response = {
                            'monto_cuota': 0,
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
            pagos = Recibo.objects.filter(pago__evento=evento_id, pago__cuota_id__in=cuotas_all,
                                          pago__estatus_cuota="PAGADO").order_by('pago__cuadra').distinct()
            if pagos:
                for ejemplar_obj in pagos:  # ejemplar_pago_set:
                    # ejemplares_pago.append(ejemplar_obj)
                    ejemplar_pago_set = ejemplar_obj.pago.ejemplar.all()
                    for x in ejemplar_pago_set:
                        i = i + 1
                        data = {
                            'cuadra': x.cuadra,  # x.pago.cuadra,
                            'contador': i,
                            "ejemplar_lote": x.lote,
                            "ejemplar_nombre": x.nombre
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

        params = {
            "reporte_cuotas": reporte,
            "evento": all_evento.to_serializable_dict,
            'cycle': range(0, i),
            "cuotas": cuotas_set,
            'descuento': descuento,
            "total": total,
            'titulo': cuota_obj,
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

2
@method_decorator(csrf_exempt, name='dispatch')
class setRetirarEjemplar(ListView):

    def get(self, request, *args, **kwargs):
        evento_ejemplar_id = request.GET.get('evento_ejemplar_id')

        EventoElegibles.objects.filter(id=evento_ejemplar_id).update(estatus=1)
        message = "retirado"
        params = {
            "estatus": message
        }

        return HttpResponse(self.json_to_dumps(params), 'application/json; charset=utf-8')