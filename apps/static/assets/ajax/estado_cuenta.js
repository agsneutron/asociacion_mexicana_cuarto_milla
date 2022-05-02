/**
 * Created by ariaocho on 11/08/17.
 */
var $j = jQuery.noConflict();

$j(document).on('ready', main_consulta);

function main_consulta() {

    $("#guarda").click(function (){
        setEstadoCuenta()
    });

     $("#descarga").click(function (){
        getRecibosPDF()
    });


}

function setEstadoCuenta() {

    var cuadra_id = $("#cuadra").val();


    if (cuadra_id !="") {
        url_set = "/amcm/set_estado_cuenta_x_cuadra/?cuadra_id=" + cuadra_id;

        $.ajaxSetup(
            {
                beforeSend: function (xhr, settings) {
                    if (settings.type == "POST")
                        xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
                    if (settings.type == "GET")
                        xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
                }
            }
        );

        var message = "";

        $.ajax({
            url: url_set,
            type: 'get',
            success: function (data) {
                swal("Se guardo correctamente el estado de cuenta");
                swal({
                    title: "Registro Exitoso!",
                    text: data.message,
                    dangerMode: true,
                });

            },
            error: function (data) {

                swal("No se guardo el estado de cuenta");
                swal({
                    title: "Ocurrió un error!",
                    text: data.message,
                    dangerMode: true,
                });

            }
        });
    }else{
        swal("No ha seleccionado una cuadra");
                swal({
                    title: "Aviso!",
                    text: "Por favor selecciona una cuadra.",
                    dangerMode: true,
                });
    }
}

function getRecibosPDF(){

    var cuadra_id = $("#cuadra").val();

    if (cuadra_id !="") {
        url_set = "/amcm/get_estado_cuenta_x_cuadra/?cuadra_id=" + cuadra_id;
        document.location.href = url_set;
    }else{
        swal("No ha seleccionado una cuadra");
                swal({
                    title: "Aviso!",
                    text: "Por favor selecciona una cuadra.",
                    dangerMode: true,
                });
    }


}