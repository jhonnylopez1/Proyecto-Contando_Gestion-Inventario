from fastapi import FastAPI,HTTPException
from sqlmodel import Session, select
from db import engine
from modelos.articulo import Articulo
from schemas.articulo import Articulos_Read
from typing import List

app= FastAPI()

@app.get("/")
def prueba():
    return {"mensaje":"hola mundo"}

@app.get("/test")
def test_db ():
    with Session(engine) as session:
        return {"mensaje":"Conexion Exitosa"}

@app.get("/articulos",response_model=List[Articulos_Read])
def get_articulos():
    try:
        with Session(engine) as session:
            articulos=session.exec(select(Articulo)).all()
            return articulos
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener articulos: {str(error)}")
