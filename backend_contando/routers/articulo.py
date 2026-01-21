#importaciones necesarias para crear el modulo router para articulo
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from db import engine
from modelos.articulo import Articulo
from schemas.articulo import Articulos_Read

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
            articulos = session.exec(select(Articulo)).all()
            return articulos
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener articulos:{str(e)}"
        )