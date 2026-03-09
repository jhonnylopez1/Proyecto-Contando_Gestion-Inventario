//URL de la ruta articulos en el backend

const URL_articulos = "http://127.0.0.1:8000/articulos";

//Function obtener articulos del backend
async function obtener_articulos() {
    try {
        const response=await fetch(URL_articulos); //peticion al backend

        const articulos=await response.json(); //convierte respuesta en json

        mostrar_articulos(articulos);
    }
    catch(error) {
        console.error("Error al obtener articulos:", error);
    }
}

//Function para mostrar los articulos

function mostrar_articulos(articulos){
    const tabla_articulo = document.querySelector("#tabla_articulo tbody"); //seleccionar donde voy a insertar los articulos

    tabla_articulo.innerHTML=""; //limpiar la tabla por si ya tenia algun dato

    articulos.forEach(articulo=>{
        const fila = document.createElement("tr")
        fila.innerHTML=`
            <td>${articulo.id_articulo}</td>
            <td>${articulo.nombre_articulo}</td>
            <td>${articulo.precio_articulo}</td>
            <td>${articulo.marca_articulo}</td>
            <td>${articulo.descripcion_articulo}</td>
        `;

        tabla_articulo.appendChild(fila);
    });



}

document.addEventListener("DOMContentLoaded", obtener_articulos);