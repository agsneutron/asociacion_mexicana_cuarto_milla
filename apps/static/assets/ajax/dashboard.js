/**
 * Created by ariaocho on 11/08/17.
 */
var $j = jQuery.noConflict();

$j(document).on('ready', main_consulta);
var dataJson;
var tableResultEvento = $('#result_list_et').DataTable();

$j.ajax({
    error: function (xhr, type, errorThrown) {
        if (!xhr.getAllResponseHeaders()) {
            xhr.abort();
            if (isPageBeingRefreshed) {
                return;
            }
        }
    }
});


function main_consulta() {

    $j.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (settings.type == "POST") {
                xhr.setRequestHeader("X-CSRFToken", $j('[name="csrfmiddlewaretoken"]').val());
                //xhr.overrideMimeType( "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; charset=utf-8" );
            }
            if (settings.type == "GET") {
                xhr.setRequestHeader("X-CSRFToken", $j('[name="csrfmiddlewaretoken"]').val());
                //xhr.overrideMimeType( "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; charset=utf-8" );
            }
        }
    });

    getDataDashboard();

    $("#clasico").click(function () {
        eventosTemporadaFiltro("Clásico");
    });

    $("#derby").click(function () {
        eventosTemporadaFiltro("Derby");
    });

    $("#futurity").click(function () {
        eventosTemporadaFiltro("Futurity");
    });


}


function getDataDashboard() {

    var api = "/amcm/get_dashboard/";
    $.ajax({
        url: api,
        type: 'get',
        success: function (data) {
            //console.log(data);
            if (data.message = "success") {
                dataJson = data;
                iniciaDashboard(dataJson);
            } else {
                var message = 'Ocurrió un error al realizar la consulta de los datos:\n' + data.estatus;
                $('#alertModal').find('.modal-body p').text(message);
                $('#alertModal').modal('show');
            }
        },
        error: function (data) {
            var message = 'Ocurrió un error al realizar la consulta de los datos:\n' + data.estatus;
            $('#alertModal').find('.modal-body p').text(message);
            $('#alertModal').modal('show')                //$j("#ajaxProgress").hide();
        }
    });

}

function iniciaDashboard(data) {

    document.getElementById('total_eventos').innerText = data.eventos;
    document.getElementById('total_cuadras').innerText = data.cuadras;
    document.getElementById('total_ejemplares').innerText = data.ejemplares;
    document.getElementById('total_pagos').innerText = "$ " + data.pagos;

    //eventos temporada
    tabla_eventosTemporada(dataJson, "");

    //cuadra ejemplares
    tabla_cuadraEjemplares(dataJson);

    //ejemplares nominados por eventp
    tabla_nominadosEvento(dataJson);

    //total recibospor cuota
    table_recibos(data);

    //tabla recibos pagos
    table_recibos_pagos(data);
}


//carga tabla eventos por temporada
function tabla_eventosTemporada(data, filtro) {

    var filtered = [];
    var data_Set;
    if (filtro !== "") {
        for (var i = 0; i < data.eventos_temporada.length; i++) {
            if (data.eventos_temporada[i].tipo === filtro) {
                filtered.push(data.eventos_temporada[i]);
            }
        }
        data_Set = filtered;

    } else {
        data_Set = data.eventos_temporada;
    }

    tableResultEvento = $('#result_list_et').DataTable({
        bInfo: false,
        "bPaginate": true,
         responsive: true,
        pageLength: 5,
        "language": {
            paginate: {
                previous: "<i class='fas fa-angle-left'>",
                next: "<i class='fas fa-angle-right'>"
            },
            searchPlaceholder: 'Filtrar resultados ...',
            emptyTable: "Realiza una búsqueda para visualizar datos.",
            infoEmpty: "Sin datos disponibles.",
            processing: "Espere un momento, buscando coincidencias.",
            lengthMenu: "Mostrar _MENU_ registros",
            select: {
                rows: {
                    _: "Registros %d seleccionados",
                    0: "De click en un registro psra seleccionarlo",
                    1: "1 Registro seleccionado "
                }
            }
        },
        select: true,
        processing: true,
    });

    //armar el array para formar el dataset de la tabla
    var data_for_table = [];
    for (var i = 0; i < data_Set.length; i++) {

        let cell1 = "";
        let cell2 = "";
        let cell3 = "";
        let cell4 = "";
        let cell5 = "";
        let cell6 = "";

        cell1 = data_Set[i].nombre;
        if (data_Set[i].cuotas.length > 1) {
            cell2 = "$ " + data_Set[i].cuotas[0].cuotaMonto + "<br/>" + data_Set[i].cuotas[0].cuotaFecha;
            cell3 = "$ " + data_Set[i].cuotas[1].cuotaMonto + "<br/>" + data_Set[i].cuotas[1].cuotaFecha;
        } else if (data_Set[i].cuotas.length == 1) {
            cell2 = data_Set[i].cuotas[0].cuotaMonto + "<br/>" + data_Set[i].cuotas[0].cuotaFecha;
            cell3 = "&nbsp;";
        } else {
            cell2 = "&nbsp;";
            cell3 = "&nbsp;";
        }


        if (data_Set[i].fechas.length > 2) {
            //data_Set[i].fechas[0].tipoFecha + "<br/>" + data_Set[i].fechas[0].fecha;
            cell4 = data_Set[i].fechas[0].fecha + "<br/>" + data_Set[i].fechas[1].fecha;
            cell5 = data_Set[i].fechas[2].fecha;
        } else if (data_Set[i].fechas.length === 2) {
            cell4 = data_Set[i].fechas[0].fecha;
            cell5 = data_Set[i].fechas[1].fecha;
        } else if (data_Set[i].fechas.length < 2) {
            cell4 = "&nbsp;";
            cell5 = data_Set[i].fechas[0].fecha;
        }
        condicion = ""
        for (var j = 0; j < data_Set[i].condicion.length; j++) {
            condicion = data_Set[i].condicion[j].condicion + "<br/>";
        }

        cell6 = data_Set[i].distancia;

        var arrResults = [cell1, cell2, cell3, cell4, cell5, cell6];
        //console.log(arrResults);
        data_for_table.push(arrResults);
    }

    //console.log(data_for_table.length);
    if (data_for_table.length > 0) {
        tableResultEvento.rows.add(data_for_table).draw();
    }

}

//filtrar por tipo de evento la tabla de eventos
function eventosTemporadaFiltro(filtro) {
    tableResultEvento.search(filtro).draw();
}

function tabla_cuadraEjemplares(data) {

    tableResult = $('#result_list_ce').DataTable({
        responsive: true,
        bInfo: false,
        bLengthChange: false,

        "language": {
             paginate: {
            previous: "<i class='fas fa-angle-left'>",
            next: "<i class='fas fa-angle-right'>"
        },
            searchPlaceholder: 'Filtrar resultados ...',
            emptyTable: "Realiza una búsqueda para visualizar datos.",
            infoEmpty: "Sin datos disponibles.",
            processing: "Espere un momento, buscando coincidencias.",
            lengthMenu: "Mostrar _MENU_ registros",
            select: {
                rows: {
                    _: "Registros %d seleccionados",
                    0: "De click en un registro psra seleccionarlo",
                    1: "1 Registro seleccionado "
                }
            },

        },
        select: true,
        processing: true,
        drawCallback: function () {
        $('#result_list_ce_paginate ul').addClass('pagination-sm');
      }
    });

    var data_for_table = [];
    for (var i = 0; i < data.cuadras_ejemplares.length; i++) {
        var arrResults = [data.cuadras_ejemplares[i].cuadra, data.cuadras_ejemplares[i].ejemplares];
        //console.log(arrResults);
        data_for_table.push(arrResults);
    }

    //console.log(data_for_table.length);
    if (data_for_table.length > 0) {
        tableResult.rows.add(data_for_table).draw();
    }
}

function tabla_nominadosEvento(data) {
    //nominados eventos
    tableResult = $('#result_list_en').DataTable({
        responsive: true,
        bInfo: false,

        "language": {
             paginate: {
            previous: "<i class='fas fa-angle-left'>",
            next: "<i class='fas fa-angle-right'>"
        },
            searchPlaceholder: 'Filtrar resultados ...',
            emptyTable: "Realiza una búsqueda para visualizar datos.",
            infoEmpty: "Sin datos disponibles.",
            processing: "Espere un momento, buscando coincidencias.",
            lengthMenu: "Mostrar _MENU_ registros",
            select: {
                rows: {
                    _: "Registros %d seleccionados",
                    0: "De click en un registro psra seleccionarlo",
                    1: "1 Registro seleccionado "
                }
            }
        },
        select: true,
        processing: true,
    });


    var data_for_table = [];
    for (var i = 0; i < data.nominados.length; i++) {
        var arrResults = [data.nominados[i].evento, data.nominados[i].ejemplares, data.nominados[i].elegible];
        //console.log(arrResults);
        data_for_table.push(arrResults);
    }

    //console.log(data_for_table.length);
    if (data_for_table.length > 0) {
        tableResult.rows.add(data_for_table).draw();
    }
}

function table_recibos(data) {
    tableResult = $('#result_list_rr').DataTable({
        responsive: true,
        bInfo: false,

        "language": {
             paginate: {
            previous: "<i class='fas fa-angle-left'>",
            next: "<i class='fas fa-angle-right'>"
        },
            searchPlaceholder: 'Filtrar resultados ...',
            emptyTable: "Realiza una búsqueda para visualizar datos.",
            infoEmpty: "Sin datos disponibles.",
            processing: "Espere un momento, buscando coincidencias.",
            lengthMenu: "Mostrar _MENU_ registros",
            select: {
                rows: {
                    _: "Registros %d seleccionados",
                    0: "De click en un registro psra seleccionarlo",
                    1: "1 Registro seleccionado "
                }
            }
        },
        select: true,
        processing: true,
    });


    var data_for_table = [];
    for (var i = 0; i < data.recibos.length; i++) {
        var arrResults = [data.recibos[i].evento, data.recibos[i].cuota, data.recibos[i].total];
        //console.log(arrResults);
        data_for_table.push(arrResults);
    }

    //console.log(data_for_table.length);
    if (data_for_table.length > 0) {
        tableResult.rows.add(data_for_table).draw();
    }


}

function table_recibos_pagos(data) {
    tableResult = $('#result_list_rp').DataTable({
        responsive: true,
        bInfo: false,

        pageLength: 6,
        "language": {
             paginate: {
            previous: "<i class='fas fa-angle-left'>",
            next: "<i class='fas fa-angle-right'>"
        },
            searchPlaceholder: 'Filtrar resultados ...',
            emptyTable: "Realiza una búsqueda para visualizar datos.",
            infoEmpty: "Sin datos disponibles.",
            processing: "Espere un momento, buscando coincidencias.",
            lengthMenu: "Mostrar _MENU_ registros",
            select: {
                rows: {
                    _: "Registros %d seleccionados",
                    0: "De click en un registro psra seleccionarlo",
                    1: "1 Registro seleccionado "
                }
            }
        },
        select: true,
        processing: true,
    });


    var data_for_table = [];
    for (var i = 0; i < data.recibos_pagos.length; i++) {
        var arrResults = [data.recibos_pagos[i].evento, data.recibos_pagos[i].numero_pagos, "$ " + data.recibos_pagos[i].monto_pago, data.recibos_pagos[i].numero_recibos, "$ " + data.recibos_pagos[i].monto_recibo,];
        //console.log(arrResults);
        data_for_table.push(arrResults);
    }

    //console.log(data_for_table.length);
    if (data_for_table.length > 0) {
        tableResult.rows.add(data_for_table).draw();
    }


}