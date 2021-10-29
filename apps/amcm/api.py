# coding=utf-8
import io
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from requests import RequestException

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.utils import timezone
import io as StringIO

class Render():
    @staticmethod
    def render(path, params):
        filename = 'dictamenFactibilidad.pdf'
        template = get_template(path)
        html = template.render(params)
        response = StringIO.StringIO()

        pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), response, path=path)
        #https://www.it-swarm-es.com/es/django/django-pisa-agregar-imagenes-pdf-salida/968337910/

        #pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response,link_callback=path)
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
            return response
        else:
            return HttpResponse("Error al generar el Dictamen PDF", status=400)

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

# ******************************************** renderear PDF ***********************************************

class GenerarReciboPDF(ListView):
    def get(self, request, *args, **kwargs):
        anterior=False;
        # factibilidad_id = request.GET.get('factibilidad_id')
        # parametros = AutorizadorDictamen.objects.get(id=1)
        #
        # presupuesto = Presupuesto.objects.get(id=factibilidad_id)
        # presupuesto = presupuesto.to_serializable_dict()
        # subtotal=0
        # total = 0
        # subtotal_iva = 0
        # total_iva = 0
        # iva=0
        # iva_resumen=0
        # descripcion_pago_extra=''
        # importe_pago_extra=0
        #
        # Arrfecha=presupuesto['fecha_de_registro'].split('/')
        #
        # fecha_base = datetime(2021, 8, 16)
        # fecha_factibilidad = datetime(int(Arrfecha[2]), int(Arrfecha[1]), int(Arrfecha[0]))
        #
        # if fecha_factibilidad < fecha_base:
        #     anterior = True
        # else:
        #     anterior = False
        #
        #
        # for obj in presupuesto['factibilidad']:
        #     if obj['importe_pago_extra']:
        #         importe_pago_extra +=obj['importe_pago_extra']
        #     if obj['descripcion_pago_extra']:
        #         descripcion_pago_extra = obj['descripcion_pago_extra']
        #
        #     if obj['nombre_resumen'] != 'IVA':
        #         subtotal += obj['importe']
        #
        #     if obj['factibilidad']:
        #         subtotal_iva +=obj['importe_sin_pago_extra']
        #         total_iva += obj['cantidad_iva']
        #     else:
        #         if obj['nombre_resumen'] == 'IVA':
        #             iva_resumen = obj['importe']
        # iva = total_iva-subtotal_iva
        # iva = iva + iva_resumen
        # total = subtotal + iva
        # params = {
        #     'presupuesto': presupuesto,
        #     'subtotal':'{:,.2f}'.format(subtotal),
        #     'iva':'{:,.2f}'.format(iva),
        #     'total':'{:,.2f}'.format(total),
        #     'descripcion_pago_extra':descripcion_pago_extra,
        #     'subdirector_planeacion':parametros.tratamiento_subdirector_planeacion + ' ' + parametros.nombre_subdirector_planeacion,
        #     'nombramiento_subdirector_planeacion':parametros.nombramiento_subdirector_planeacion,
        #     'director_general': parametros.tratamiento_director_general + ' ' + parametros.nombre_director_general,
        #     'nombramiento_director_general':parametros.nombramiento_director_general,
        # }

        params = {
            'presupuesto': "presupuesto"
        }


        if anterior == False:
            return Render.render('amcm/recibo.html', params)
        else:
            return Render.render('amcm/recibo.html', {})