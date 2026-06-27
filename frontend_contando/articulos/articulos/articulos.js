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
            <td>
                <button class="btn btn-warning btn-sm"
                onclick="mostrarFormularioActualizar(
                    ${articulo.id_articulo},
                    '${articulo.nombre_articulo}',
                    ${articulo.precio_articulo},
                    '${articulo.marca_articulo}',
                    '${articulo.descripcion_articulo}',
                    ${articulo.stock}
                )">
                Editar
                </button>
                <button onclick="eliminarArticulo(${articulo.id_articulo})">
                    Eliminar
                </button>
            </td>
        `;

        tabla_articulo.appendChild(fila);
    });
}




//Funcion para eliminar Articulos(Desactivarlos)
async function eliminarArticulo(id){
    const confirmar = confirm("Esta seguro de eliminar este articulo?");
    if(!confirmar) return;

    try{
        const respuesta = await fetch(`http://127.0.0.1:8000/articulos/${id}`, {method:"DELETE"});

        if(!respuesta.ok){
            throw new Error(
                "No se pudo eliminar el articulo"
            );}
        
        //Sea cual sea la respuesta recarga nuevamente la tabla
        obtener_articulos();

        }catch(error){
            console.error("Error:",error);
            alert("Error al eliminar el articulo");
        }

}
//Funcion para mostrar el formulario para editar el articulo
function mostrarFormularioActualizar(
    id,nombre,precio,marca,descripcion,stock
){
    document.getElementById("contenedorActualizar").style.display="block";
    document.getElementById("actualizar_id").value = id;
    document.getElementById("actualizar_nombre").value = nombre;
    document.getElementById("actualizar_precio").value = precio;
    document.getElementById("actualizar_marca").value = marca;
    document.getElementById("actualizar_descripcion").value = descripcion;
    document.getElementById("actualizar_stock").value = stock;
}
//Funcion PUT para actualizar Articulo
document.getElementById("actualizarArticuloForm").addEventListener("submit",async function(event) {
    event.preventDefault();
    const id =
        document.getElementById("actualizar_id").value;

    const datosActualizados = {

        nombre_articulo:
            document.getElementById("actualizar_nombre").value,

        precio_articulo:
            parseInt(document.getElementById("actualizar_precio").value),

        marca_articulo:
            document.getElementById("actualizar_marca").value,

        descripcion_articulo:
            document.getElementById("actualizar_descripcion").value,

        stock:
            parseInt(document.getElementById("actualizar_stock").value)
    };
    try{
        const response = await fetch(
            `http://127.0.0.1:8000/articulos/${id}`,
            {
                method:"PUT",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify(datosActualizados)
            }
        );
        if(!response.ok){
            throw new Error("Error al actualizar")
        }
        alert("Articulo actualizado correctamente");
        document.getElementById(
            "contenedorActualizar"
        ).style.display = "none";

        obtener_articulos();
    }catch(error){
        console.error(error);
        alert("Error al actualizar el articulo")
    }
});

//Crear un nuevo articulo
document.getElementById("articuloForm").addEventListener("submit",
    async function(event){
        event.preventDefault();

        const formulario = event.target;
        
        const nuevoArticulo = {
            id_articulo:parseInt(formulario.id_articulo.value),
            nombre_articulo:formulario.nombre_articulo.value,
            precio_articulo:parseInt(formulario.precio_articulo.value),
            marca_articulo:formulario.marca_articulo.value,
            descripcion_articulo:formulario.descripcion_articulo.value
        };

        try{
            const response = await fetch(URL_articulos + "/",{
                method:"POST",
                headers:{
                    "Content-Type": "application/json"
                },
                body:JSON.stringify(nuevoArticulo)
            });

            if (!response.ok){
                throw new Error("No se pudo crear el articulo");
            }
            alert("Articulo creado correctamente");

            formulario.reset();

            obtener_articulos();
        }catch(error){
            console.error(error);
            alert("Error al guardar el articulo");
        }
    }
);

document.addEventListener("DOMContentLoaded", obtener_articulos);