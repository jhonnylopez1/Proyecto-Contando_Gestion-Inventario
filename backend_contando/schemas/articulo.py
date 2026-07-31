from pydantic import BaseModel, Field
from typing import Optional

class Articulos(BaseModel):
    id_articulo:int
    nombre_articulo:str=Field(min_length=2,max_length=50)
    precio_articulo:int=Field(gt=0)
    marca_articulo:str=Field(min_length=2,max_length=30)
    descripcion_articulo:str=Field(min_length=2,max_length=50)
    stock:Optional[int]=Field(default=None,ge=0)

    model_config = {
        "from_attributes": True}

class Articulos_Actualizar(BaseModel):
    nombre_articulo:Optional[str]=Field(default=None,min_length=2,max_length=50)
    precio_articulo:Optional[int]=Field(default=None,gt=0)
    marca_articulo:Optional[str]=Field(default=None,min_length=2,max_length=30)
    descripcion_articulo:Optional[str]=Field(default=None,min_length=2,max_length=50)
    # stock:Optional[int]=Field(default=None,ge=0)

    # model_config = {
    #     "from_attributes": True}

class Articulos_Read(Articulos):
    pass

class ArticuloCrear(BaseModel):
    nombre_articulo:str=Field(min_length=2,max_length=50)
    precio_articulo:int = Field(gt=0)
    marca_articulo:str=Field(min_length=2,max_length=30)
    descripcion_articulo:str=Field(min_length=2,max_length=50)
