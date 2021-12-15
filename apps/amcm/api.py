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
