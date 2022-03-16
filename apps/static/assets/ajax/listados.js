/**
 * Created by ariaocho on 11/08/17.
 */
var $j = jQuery.noConflict();

$j(document).on('ready', main_consulta);
var dataJson;

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
}


function setRetirado(id_eventoejemplar) {
    var api = "/amcm/set_retirar_ejemplar/?evento_ejemplar_id="+id_eventoejemplar;
    $.ajax({
        url: api,
        type: 'GET',
        success: function (data) {
            console.log(data);
            if (data.message = "success") {
                dataJson = data;
                actualizaTabla(dataJson,id_eventoejemplar);
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

function actualizaTabla(dataJson,id_eventoejemplar){
    var btn_to_hide = document.getElementById('retirar_' + id_eventoejemplar);
    var td_to_update = document.getElementById('ejemplar_' + id_eventoejemplar);
    td_to_update.append("RETIRADO");
    td_to_update.innerHTML = "RETIRADO";
    td_to_update.innerText = "RETIRADO";
    btn_to_hide.style.display = 'none';
    btn_to_hide.hidden = true;
    console.log(btn_to_hide);
    console.log(td_to_update);
}