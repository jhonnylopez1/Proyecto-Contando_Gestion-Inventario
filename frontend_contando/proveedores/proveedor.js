//URL de la ruta proveedores

const URL_proveedores= "http://127.0.0.1:8000/proveedores";

//Funcion para obtener proveedores del backend
async function obtener_proveedores(estado){
    try{
        let url;
        if(estado!==undefined){
            url =`${URL_proveedores}?estado=${estado}`
        }
        else{
            url=URL_proveedores
        }
        const response=await fetch(url);//peticion al backend
        const proveedores=await response.json();//convierte a json
        mostrar_proveedores(proveedores,estado)

    }
    catch(error){
        console.error("Error al obtener proveedores:",error);
    }
}

const tabla_Proveedores=document.getElementById("tabla_Proveedores")

//Boton proveedor Activo e Inactivo
const botonActivos=document.querySelector(".btn_proveedores_activos");
const botonInactivos=document.querySelector(".btn_proveedores_inactivos");
const botonTodos=document.querySelector(".btn_todos_proveedores")

//Mostrar todos los proveedores
botonTodos.addEventListener("click",()=>{
    tabla_Proveedores.style.display="block";
    botonTodos.classList.add("btn_proveedor_seleccionado")
    botonInactivos.classList.remove("btn_proveedor_seleccionado");
    botonActivos.classList.remove("btn_proveedor_seleccionado");
    obtener_proveedores();
});

//MOSTRAR PROVEEDORES ACTIVOS
botonActivos.addEventListener("click", () => {

    tabla_Proveedores.style.display = "block";

    botonActivos.classList.add("btn_proveedor_seleccionado");
    botonInactivos.classList.remove("btn_proveedor_seleccionado");
    botonTodos.classList.remove("btn_proveedor_seleccionado")


    obtener_proveedores(1);
});

//MOSTRAR PROVEEDORES INACTIVOS
botonInactivos.addEventListener("click", () => {

    tabla_Proveedores.style.display = "block";

    botonInactivos.classList.add("btn_proveedor_seleccionado");
    botonActivos.classList.remove("btn_proveedor_seleccionado");
    botonTodos.classList.remove("btn_proveedor_seleccionado")

    obtener_proveedores(0);
});

//ID PROVEEDOR
let idProveedorActual = null;

//Mostrar Proveedores
function mostrar_proveedores(proveedores,estado){
    const tabla_proveedor=document.querySelector("#tabla_proveedor tbody");//donde insertar proveedores

    tabla_proveedor.innerHTML=""; //limpiar la tabla

    proveedores.forEach(proveedor=>{
        const fila=document.createElement("tr")
        fila.innerHTML=`
            <td>${proveedor.id_proveedor}</td>
            <td>${proveedor.nombre_proveedor}</td>
            <td>${proveedor.tel_proveedor}</td>
            <td>${proveedor.correo_proveedor}</td>
            <td>${proveedor.direccion_proveedor}</td>
            ${crear_botones(proveedor.estado,proveedor)}
        `;

        tabla_proveedor.appendChild(fila);
    });

}

//Funcion para crear botones e insertarlos en la funcion mostrar proveedores

function crear_botones(estado,proveedor){
    if (estado==1){
        return `
            <td>
            <button class="btn btn-outline-warning text-dark btn-sm"
            onclick="mostrarFormularioActualizar(
                ${proveedor.id_proveedor},
                '${proveedor.nombre_proveedor}',
                ${proveedor.tel_proveedor},
                '${proveedor.correo_proveedor}',
                '${proveedor.direccion_proveedor}',
                ${proveedor.stock}
            );document.querySelector('.seccion_crear_proveedor').style.display='none'">
            Editar
            </button>
            <button class="btn btn-outline-danger text-dark btn-sm" onclick="eliminarProveedor(${proveedor.id_proveedor})">
                Eliminar
            </button>
            </td>
        `
        
    }
    else if (estado==0){
        return `
            <td>
                <button class="btn btn-outline-success text-dark btn-sm" onclick="reactivar_proveedor_inactivo(${proveedor.id_proveedor})">
                    Reactivar
                </button>
            </td>
        `
    }

};

//Buscador de Proveedores
document.getElementById("buscadorInventario").addEventListener("keyup", function () {
    let filtro = this.value.toLowerCase();
    let filas = document.querySelectorAll("#cuerpoProveedores tr");

    filas.forEach(fila => {
        let texto = fila.textContent.toLowerCase();
        if (texto.includes(filtro)) {
            fila.style.display = "";
        } else {
            fila.style.display = "none";
        }
    });
});

//Funcion para reactivar proveedor inactivo
async function reactivar_proveedor_inactivo(id) {
    try{
        const respuesta = await fetch(
            `http://127.0.0.1:8000/proveedores/${id}/reactivar`,
            {
                method:"PUT",
                headers:{
                    "Content-Type":"application/json"
                }
            }
        );
        if(!respuesta.ok){
            throw new Error("Error al actualizar")
        }
        alert("Proveedor Reactivado");
        obtener_proveedores(estado=0);
    }catch(error){
        console.error(error);
        alert("Error al actualizar el proveedor")
    }
         
}

//Funcion para eliminar Proveedores(Desactivarlos)
async function eliminarProveedor(id){
    const confirmar = confirm("Esta seguro de eliminar este proveedor?");
    if(!confirmar) return;

    try{
        const respuesta = await fetch(`http://127.0.0.1:8000/proveedores/${id}`, {method:"DELETE"});

        if(!respuesta.ok){
            throw new Error(
                "No se pudo eliminar el proveedor"
            );}

        const datos = await respuesta.json();
        alert(datos.mensaje);
        //Sea cual sea la respuesta recarga nuevamente la tabla
        obtener_proveedores(estado=1);

        }catch(error){
            console.error("Error:",error);
            alert("Error al eliminar el proveedor");
        }

}

//Funcion para mostrar el formulario para editar el proveedor
function mostrarFormularioActualizar(
    id,nombre,telefono,correo,direccion
){
    
    document.getElementById("contenedorActualizar").style.display="block";
    idProveedorActual=id;
    document.getElementById("actualizar_nombre").value = nombre;
    document.getElementById("actualizar_telefono").value = telefono;
    document.getElementById("actualizar_correo").value = correo;
    document.getElementById("actualizar_direccion").value = direccion;
    
    //Funcion para abrir el modal de bootstrap
    const modal = new bootstrap.Modal(
        document.getElementById("modalActualizar")
    );

    modal.show();   
}

// Detectar cuando el modal se cierre
const modalElemento = document.getElementById("modalActualizar");

modalElemento.addEventListener("hidden.bs.modal", function () {
    document.querySelector(".seccion_crear_proveedor").style.display = "block";
});

//Funcion PUT para actualizar Proveedor
document.getElementById("actualizarProveedorForm").addEventListener("submit",async function(event) {
    event.preventDefault();
        
    const datosActualizados = {

        nombre_proveedor:
            document.getElementById("actualizar_nombre").value,

        tel_proveedor:
            document.getElementById("actualizar_telefono").value,

        correo_proveedor:
            document.getElementById("actualizar_correo").value,

        direccion_proveedor:
            document.getElementById("actualizar_direccion").value,
    };
    try{
        const response = await fetch(
            `http://127.0.0.1:8000/proveedores/${idProveedorActual}`,
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
        alert("Proveedor actualizado correctamente");
        document.getElementById(
            "contenedorActualizar"
        ).style.display = "none";

        //################## ocultar modal
        const modalElement = document.getElementById("modalActualizar");
        const modal = bootstrap.Modal.getInstance(modalElement);
        modal.hide();
        //##################
        obtener_proveedores();
    }catch(error){
        console.error(error);
        alert("Error al actualizar el proveedor")
    }
});

//Crear un nuevo proveedor
document.getElementById("proveedorForm").addEventListener("submit",
    async function(event){
        event.preventDefault();

        const formulario = event.target;
        
        const nuevoProveedor = {
            nombre_proveedor:formulario.nombre_proveedor.value,
            tel_proveedor:formulario.tel_proveedor.value,
            correo_proveedor:formulario.correo_proveedor.value,
            direccion_proveedor:formulario.direccion_proveedor.value
        };
        

        try{
            
            const response = await fetch(URL_proveedores + "/",{
                method:"POST",
                headers:{
                    "Content-Type": "application/json"
                },
                body:JSON.stringify(nuevoProveedor)
            });

            if (!response.ok){
                throw new Error("No se pudo crear el proveedor");
            }
            alert("Proveedor creado correctamente");

            formulario.reset();

            obtener_proveedores();
        }catch(error){
            console.error(error);
            alert("Error al guardar el proveedor");
        }
    }
);