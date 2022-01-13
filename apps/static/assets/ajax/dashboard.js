/**
 * Created by ariaocho on 11/08/17.
 */
var $j = jQuery.noConflict();

$j(document).on('ready', main_consulta);
var dataJson;
$j.ajax({
    error: function(xhr, type, errorThrown){
        if (!xhr.getAllResponseHeaders()){
            xhr.abort();
            if (isPageBeingRefreshed ){
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

    $( "#clasico" ).click(function() {
          eventosTemporada(dataJson,"Clásico");
    });

    $( "#derby" ).click(function() {
          eventosTemporada(dataJson,"Derby");
    });

    $( "#futurity" ).click(function() {
          eventosTemporada(dataJson,"Futurity");
    });


}



function getDataDashboard() {

     var api = "/amcm/get_dashboard/";
     $.ajax({
        url: api,
        type: 'get',
        success: function(data) {
            console.log(data);
            if (data.message = "success"){
                dataJson = data;
                iniciaDashboard(dataJson);
            }else{
                 var message = 'Ocurrió un error al realizar la consulta de los datos:\n' + data.estatus;
                $('#alertModal').find('.modal-body p').text(message);
                $('#alertModal').modal('show')  ;
            }
        },
        error: function(data) {
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
    eventosTemporada(dataJson,"");

    //cuadra eventos
    myTable = document.getElementById('result_list_ce').getElementsByTagName('tbody')[0];

    for (var i = 0; i < data.cuadras_ejemplares.length; i++) {
        let row = myTable.insertRow();
        let cell1 = row.insertCell(0);
        let cell2 = row.insertCell(1);

        cell1.classList.add("text-wrap");

        cell1.innerHTML = data.cuadras_ejemplares[i].cuadra;
        cell2.innerHTML = data.cuadras_ejemplares[i].ejemplares;

        //.append("<tr><td>data.cuadras_ejemplares[i].cuadra</td><td>data.cuadras_ejemplares[i].ejemplares</td></tr>");
    }


    //nominados eventos
    myTable = document.getElementById('result_list_en').getElementsByTagName('tbody')[0];

    for (var i = 0; i < data.nominados.length; i++) {
        let row = myTable.insertRow();
        let cell1 = row.insertCell(0);
        let cell2 = row.insertCell(1);
        let cell3 = row.insertCell(2);

        cell1.classList.add("text-wrap");
        cell3.classList.add("text-wrap");

        cell1.innerHTML = data.nominados[i].evento;
        cell2.innerHTML = data.nominados[i].ejemplares;
        cell3.innerHTML = data.nominados[i].elegible;

        //.append("<tr><td>data.cuadras_ejemplares[i].cuadra</td><td>data.cuadras_ejemplares[i].ejemplares</td></tr>");
    }

    //nominados eventos
    myTable = document.getElementById('result_list_rr').getElementsByTagName('tbody')[0];

    for (var i = 0; i < data.recibos.length; i++) {
        let row = myTable.insertRow();
        let cell1 = row.insertCell(0);
        let cell2 = row.insertCell(1);
        let cell3 = row.insertCell(2);

        cell1.classList.add("text-wrap");
        cell3.classList.add("text-wrap");

        cell1.innerHTML = data.recibos[i].evento;
        cell2.innerHTML = data.recibos[i].cuota;
        cell3.innerHTML = data.recibos[i].total;

        //.append("<tr><td>data.cuadras_ejemplares[i].cuadra</td><td>data.cuadras_ejemplares[i].ejemplares</td></tr>");
    }
}

function eventosTemporada(data, filtro){

    var filtered = [];
    var data_Set;
    if (filtro !== ""){
        for (var i = 0; i < data.eventos_temporada.length; i++) {
          if (data.eventos_temporada[i].tipo === filtro) {
                filtered.push(data.eventos_temporada[i]);
          }
        }
        data_Set = filtered;
    }
    else{
         data_Set = data.eventos_temporada;
    }
     console.log("==" + filtered + "==");
    console.log("==" + filtro + "==");
    console.log(data);
    //eventos temporada


    myTable = document.getElementById('result_list_et').getElementsByTagName('tbody')[0];
    myTable.innerHTML = '';
    for (var i = 0; i < data_Set.length; i++) {

            let row = myTable.insertRow();
            let cell1 = row.insertCell(0);
            let cell2 = row.insertCell(1);
            let cell3 = row.insertCell(2);
            let cell4 = row.insertCell(3);
            let cell5 = row.insertCell(4);
            let cell6 = row.insertCell(5);
            let cell7 = row.insertCell(6);

            cell1.classList.add("text-wrap");

            cell1.innerHTML = data_Set[i].nombre;
            if (data_Set[i].cuotas.length > 1) {
                cell2.innerHTML = "$ " + data_Set[i].cuotas[0].cuotaMonto + "<br/>" + data_Set[i].cuotas[0].cuotaFecha;
                cell3.innerHTML = "$ " + data_Set[i].cuotas[1].cuotaMonto + "<br/>" + data_Set[i].cuotas[1].cuotaFecha;
            } else if (data_Set[i].cuotas.length == 1) {
                cell2.innerHTML = data_Set[i].cuotas[0].cuotaMonto + "<br/>" + data_Set[i].cuotas[0].cuotaFecha;
                cell3.innerHTML = "&nbsp;";
            } else {
                cell2.innerHTML = "&nbsp;";
                cell3.innerHTML = "&nbsp;";

            }

            if (data_Set[i].fechas.length > 1) {
                cell4.innerHTML = data_Set[i].fechas[0].tipoFecha + "<br/>" + data_Set[i].fechas[0].fecha;
                cell5.innerHTML = data_Set[i].fechas[1].tipoFecha + "<br/>" + data_Set[i].fechas[1].fecha;
            } else {
                cell4.innerHTML = "&nbsp;";
                cell5.innerHTML = data_Set[i].fechas[0].tipoFecha + "<br/>" + data_Set[i].fechas[0].fecha;
            }
            condicion = ""
            for (var j = 0; j < data_Set[i].condicion.length; j++) {
                condicion = data_Set[i].condicion[j].condicion + "<br/>";
            }
            //cell6.classList.add("text-wrap");
            //cell6.innerHTML = condicion;
            cell6.innerHTML = data_Set[i].distancia;

            // let row2 = myTable.insertRow();
            // let cell21 = row2.insertCell(0);
            // cell21.setAttribute('colspan',6);
            // cell21.classList.add("smallandcenter");
            // cell21.innerHTML = condicion;

            //.append("<tr><td>data.cuadras_ejemplares[i].cuadra</td><td>data.cuadras_ejemplares[i].ejemplares</td></tr>");

    }


}