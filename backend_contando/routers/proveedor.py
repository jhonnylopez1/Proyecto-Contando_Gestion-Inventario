#importaciones necesarias para crear el modulo router para proveedor
from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session,select
from typing import List,Optional

from backend_contando.db import engine
from backend_contando.modelos.proveedor import Proveedor
from backend_contando.schemas.proveedor import Proveedor_Read,Proveedor_Actualizar,Proveedor_Crear

#Definir nombre de la ruta
router = APIRouter(
    prefix="/proveedores",
    tags=["Proveedores"]
)

#se define la ruta get para proveedor
@router.get("/",response_model=list[Proveedor_Read])
def get_proveedores(estado:Optional[int]=None):
    try:
        with Session(engine) as session:
            proveedores=select(Proveedor)
            if estado is not None:
                proveedores=proveedores.where(Proveedor.estado==estado)
            proveedores=session.exec(proveedores).all()
            return proveedores
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener articulos:{str(e)}"
        )

#Se define la ruta para eliminar un proveedor
@router.delete("/{id_proveedor}")
def eliminar_proveedor(id_proveedor:int):
    try:
        with Session(engine) as session:
            proveedor=session.get(Proveedor,id_proveedor)
            if not proveedor:
                raise HTTPException(
                    status_code=404,
                    detail="Proveedor no encontrado"
                )
            proveedor.estado=0
            session.commit()
            return{"mensaje":"Proveedor desactivado"}
    except Exception as e:
        print("ERROR REAL",e)
        raise HTTPException(
            status_code=500,
            detail=f"Error al eliminar proveedor:{str(e)}"
        )

#ruta para actualizar proveedor
@router.put("/{id_proveedor}",response_model=Proveedor_Read)
def actualizar_proveedor(id_proveedor:int, data:Proveedor_Actualizar):
    try:
        with Session(engine) as session:
            proveedor=session.get(Proveedor,id_proveedor)
            if not proveedor:
                raise HTTPException(
                    status_code=404,
                    detail="Proveedor no encontrado"
                )
            datos_actualizados = data.model_dump(exclude_unset=True)
            for key,value in datos_actualizados.items():
                setattr(proveedor,key,value)#setattr:"establecer atributo",ejemplo:articulo.precio_articulo=5000
            session.commit()
            session.refresh(proveedor)
            return proveedor
    except Exception as e:
        print("ERROR REAL",e)
        raise HTTPException(
            status_code=500,
            detail=f"Error al eliminar proveedor:{str(e)}"
        )

####Reactivar Proveedor
@router.put("/{id_proveedor}/reactivar")
def reactivar_proveedor(id_proveedor:int):
    try:
        with Session(engine) as session:
            proveedor=session.get(Proveedor,id_proveedor)
            if not proveedor:
                raise HTTPException(
                    status_code=404,
                    detail="Proveedor no encontrado"
                )
            proveedor.estado=1
            session.commit()
            session.refresh(proveedor)
            return {"mensaje":"Proveedor activado"}
    except Exception as e:
        print("ERROR REAL",e)
        raise HTTPException(
            status_code=500,
            detail=f"Error al reactivar proveedor:{str(e)}"
        )

#Ruta para crear proveedor
@router.post("/",response_model=Proveedor_Read)
def crear_proveedor(data:Proveedor_Crear):
    try:
        with Session(engine) as session:
            nuevo_proveedor = Proveedor(
                nombre_proveedor=data.nombre_proveedor,
                tel_proveedor=data.tel_proveedor,
                correo_proveedor=data.correo_proveedor,
                direccion_proveedor=data.direccion_proveedor,
                estado=1
            )
            session.add(nuevo_proveedor)
            session.commit()
            session.refresh(nuevo_proveedor)
            return nuevo_proveedor
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=f"Error al crear proveedor:{str(e)}"
        )
