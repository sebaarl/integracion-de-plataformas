$(document).ready(function() {
    $("#enviar").click(function() {
        $.get("http://127.0.0.1:8000/AppProducto/product-list/",
            function(data) {
                $.each(data, function(i, item) { 
                    $("#categorias").append("<tr>" + 
                        "<td>" + item.id  + "</td>" +
                        "<td>" + item.nombre + "</td>" +
                        "<td>" + item.precio + "</td>" +
                        "<td>" + item.descripcion + "</td>" +
                        "</tr>")
                });
            }
        )
        $("#enviar").prop('disabled',true);
    });        
});