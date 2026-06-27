#importaciones necesarias para crear el modulo router para articulo
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from backend_contando.db import engine
from backend_contando.modelos.articulo import Articulo
from backend_contando.schemas.articulo import Articulos_Read
from backend_contando.schemas.articulo import Articulos_Actualizar
from backend_contando.schemas.articulo import ArticuloCrear

#Se define el nombre de la ruta
router = APIRouter(
    prefix="/articulos",
    tags=["Articulos"]
)


#Se define la ruta get para articulo
@router.get("/", response_model=list[Articulos_Read])
def get_articulos():
    try:
        with Session(engine) as session:
            articulos = session.exec(select(Articulo).where(Articulo.estado == 1)).all() #Trae solo los articulos activos, con estado 1
            return articulos
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener articulos:{str(e)}"
        )

#Se define la ruta para eliminar un articulo
@router.delete("/{id_articulo}",response_model=Articulos_Read)
def eliminar_articulo(id_articulo:int):
    try:
        with Session(engine) as session:
            articulo = session.get(Articulo,id_articulo)
            if not articulo:
                raise HTTPException(
                    status_code=404,
                    detail="Articulo no encontrado"
                )
            articulo.estado = 0
            session.commit()
            return {"mensaje":"Articulo desactivado"}
    except Exception as e:
        print("ERROR REAL",e)
        raise HTTPException(
            status_code=500,
            detail=f"Error al eliminar articulo:{str(e)}"
        )


@router.put("/{id_articulo}",response_model=Articulos_Read)
def actualizar_articulo(id_articulo:int, data:Articulos_Actualizar):
    try:
        with Session(engine) as session:
            articulo = session.get(Articulo,id_articulo)
            if not articulo:
                raise HTTPException(
                    status_code=404,
                    detail="Articulo no encontrado"
                )
            # Actualizar la informacion enviada desde el formulario, si no viene nada no se actualiza, quedan los valores actuales
            datos_actualizados = data.model_dump(exclude_unset=True)

            for key,value in datos_actualizados.items():
                setattr(articulo,key,value) #setattr:"establecer atributo",ejemplo:articulo.precio_articulo=5000
            
            session.commit()
            session.refresh(articulo)

##############NOTA: ya quedo el router, la proxima vez debo aprender a conectar esto con el Frontend

    except Exception as e:
        print("ERROR REAL",e)
        raise HTTPException(
            status_code=500,
            detail=f"Error al eliminar articulo:{str(e)}"
        )

@router.post("/",response_model=Articulos_Read)
def crear_articulo(data:ArticuloCrear):
    try:
        with Session(engine) as session:
            nuevo_articulo = Articulo(
                id_articulo=data.id_articulo,
                nombre_articulo=data.nombre_articulo,
                precio_articulo=data.precio_articulo,
                marca_articulo=data.marca_articulo,
                descripcion_articulo=data.descripcion_articulo,
                stock=data.stock if data.stock is not None else 0,
                estado=1
            )
            session.add(nuevo_articulo)
            session.commit()
            session.refresh(nuevo_articulo)

            return nuevo_articulo
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al crear articulo:{str(e)}"
        )