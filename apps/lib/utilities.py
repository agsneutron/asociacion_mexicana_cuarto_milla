# coding=utf-8
import json
import copy

from decimal import Decimal
from datetime import date

class Utilities():
    @staticmethod
    def get_array_or_none(the_string):
        if the_string is None or the_string == "":
            return None
        else:
            return map(int, the_string.split(','))

    @staticmethod
    def get_string_array_or_none(the_string):
        if the_string is None or the_string == "":
            return None
        else:
            return map(str, the_string.split(','))

    # Toma un queryset, lo vuelve serializable y lo serializa para poder devolverlo al cliente.
    @staticmethod
    def query_set_to_dumps(query_set_object):
        return json.dumps(map(lambda model_object: model_object.to_serializable_dict(), query_set_object),
                          indent=4, separators=(',', ': '), sort_keys=False, ensure_ascii=False
                          )

    # Toma un objeto tipo json, y lo serializa para poder mandarlo al cliente.
    @staticmethod
    def json_to_dumps(json_object):
        return json.dumps(json_object, indent=4, separators=(',', ': '), sort_keys=False, ensure_ascii=False)

    @staticmethod
    def json_to_dumps_encode(json_object):
        return json.dumps(json_object, indent=4, separators=(',', ': '), sort_keys=False, ensure_ascii=False, default=Utilities.encode_b)

    # Transforma un queryset a un objeto tipo JSON.
    @staticmethod
    def query_set_to_dictionary(query_set_object):
        return map(lambda model_object: model_object.to_serializable_dict(), query_set_object)

    @staticmethod
    def clean_generic_queryset(query_set_object):
        """
        Cleans a QuerySet object, converting it's decimal properties to strings.
        :param query_set_object: object to clean
        :return: the QuerySet object with the decimal attributes converted to strings
        """
        response = []
        for obj in query_set_object:
            for obj_attr in obj.keys():
                if type(obj[obj_attr]) is Decimal or type(obj[obj_attr]) is date:
                    obj[obj_attr] = str(obj[obj_attr])
            response.append(obj)
        return response

    @staticmethod
    def remove_empty_values_keys_from_object(object):

        object_as_dict = copy.deepcopy(object).__dict__
        keys_to_remove = []
        for key in object_as_dict:
            if object_as_dict[str(key)] is None:
                keys_to_remove.append(key)

        for key in keys_to_remove:
            object_as_dict.pop(key)

        return object_as_dict


    @staticmethod
    def numero_to_letras(numero):
        indicador = [("", ""), ("MIL", "MIL"), ("MILLON", "MILLONES"), ("MIL", "MIL"), ("BILLON", "BILLONES")]
        entero = int(numero)
        decimal = int(round((numero - entero) * 100))
        # print 'decimal : ',decimal
        contador = 0
        numero_letras = ""
        while entero > 0:
            a = entero % 1000
            if contador == 0:
                en_letras = Utilities.convierte_cifra(a, 1).strip()
            else:
                en_letras = Utilities.convierte_cifra(a, 0).strip()
            if a == 0:
                numero_letras = en_letras + " " + numero_letras
            elif a == 1:
                if contador in (1, 3):
                    numero_letras = indicador[contador][0] + " " + numero_letras
                else:
                    numero_letras = en_letras + " " + indicador[contador][0] + " " + numero_letras
            else:
                numero_letras = en_letras + " " + indicador[contador][1] + " " + numero_letras
            numero_letras = numero_letras.strip()
            contador = contador + 1
            entero = int(entero / 1000)
        #numero_letras = numero_letras + " con " + str(decimal) + "/100"

        print
        'numero: ', numero_letras

        return numero_letras

    @staticmethod
    def convierte_cifra(numero, sw):
        lista_centana = ["", ("CIEN", "CIENTO"), "DOCIENTOS", "TRECIENTOS", "CUATROCIENTOS", "QUINIENTOS",
                         "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]
        lista_decena = ["", (
        "DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISEIS", "DIESCISIETE", "DIECIOCHO", "DIECINUEVE"),
                        ("VEINTE", "VEINTI"), ("TREINTA", "TREINTA Y "), ("CUARENTA", "CUARENTA Y "),
                        ("CINCUENTA", "CINCUENTA Y "), ("SESENTA", "SESENTA Y "),
                        ("SETENTA", "SETENTA Y "), ("OCHENTA", "OCHENTA Y "),
                        ("Noventa", "Noventa y ")
                        ]
        lista_unidad = ["", ("UN", "UNO"), "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE"]
        centena = int(numero / 100)
        decena = int((numero - (centena * 100)) / 10)
        unidad = int(numero - (centena * 100 + decena * 10))
        # print "centena: ",centena, "decena: ",decena,'unidad: ',unidad

        texto_centena = ""
        texto_decena = ""
        texto_unidad = ""

        # Validad las centenas
        texto_centena = lista_centana[centena]
        if centena == 1:
            if (decena + unidad) != 0:
                texto_centena = texto_centena[1]
            else:
                texto_centena = texto_centena[0]

        # Valida las decenas
        texto_decena = lista_decena[decena]
        if decena == 1:
            texto_decena = texto_decena[unidad]
        elif decena > 1:
            if unidad != 0:
                texto_decena = texto_decena[1]
            else:
                texto_decena = texto_decena[0]
        # Validar las unidades
        # print "texto_unidad: ",texto_unidad
        if decena != 1:
            texto_unidad = lista_unidad[unidad]
            if unidad == 1:
                texto_unidad = texto_unidad[sw]

        return "%s %s %s" % (texto_centena, texto_decena, texto_unidad)

    @staticmethod
    def mes_to_letra(mes):
        months = ["Unknown",
                  "Enero",
                  "Febrero",
                  "Marzo",
                  "Abril",
                  "Mayo",
                  "Junio",
                  "Julio",
                  "Agosto",
                  "Septiembre",
                  "Octubre",
                  "Noviembre",
                  "Diciembre"]

        return months[mes]






