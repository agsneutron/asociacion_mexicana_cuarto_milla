/**
 * Created by ariaocho on 11/08/17.
 */
var $j = jQuery.noConflict();

$j(document).on('ready', main_consulta);

function main_consulta() {

    $("#filtrar").click(function (){
        getRecibos()
    });

     $("#descarga").click(function (){
        getRecibosPDF()
    });

}

function getRecibos() {

    // var evento_id = document.getElementById("evento").value;
    // var fecha_de = document.getElementById("fecha_de").value;
    // var fecha_a = document.getElementById("fecha_a").value;

    var evento_id = $("#evento").val();
    var fecha_de = $("#fecha_de").val();
    var fecha_a = $("#fecha_a").val();

    document.location.href = "/amcm/get_reporte_recibos/?evento_id=" + evento_id + '&fecha_de=' + fecha_de + '&fecha_a=' + fecha_a;
}

function getRecibosPDF(){

    var evento_id = $("#evento").val();
    var fecha_de = $("#fecha_de").val();
    var fecha_a = $("#fecha_a").val();


    document.location.href = "/amcm/get_reporte_recibos_pdf/?evento_id=" + evento_id + '&fecha_de=' + fecha_de + '&fecha_a=' + fecha_a;

}