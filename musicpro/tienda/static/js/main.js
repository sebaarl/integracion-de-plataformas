$(document).ready(function() {
    // vamos a probar el servicio rest
    // vamos a llamar el servicio y mostrar los elementos en la tabla de categorias
    // al hacer click en el botón
    $("#enviar").click(function() {
        $.get("http://127.0.0.1:8000/AppProducto/product-list/",
            function(data) {
                // en data se capturan toda la info que retorna el servicio
                $.each(data, function(i, item) { 
                    // por cada categoria le agregamos una fila en la tabla
                    // y por cada fila le agregamos los datos que vienen como info
                    $("#categorias").append("<tr>" + 
                        "<td>" + item.id  + "</td>" +
                        "<td>" + item.nombre + "</td>" +
                        "<td>" + item.precio + "</td>" +
                        "<td>" + item.descripcion + "</td>" +
                        "</tr>")
                });
            }
        )
        // despues de mostrar los datos en la tabla, desactivamos el botón
        // para que no duplique la información
        $("#enviar").prop('disabled',true);
    });        
});