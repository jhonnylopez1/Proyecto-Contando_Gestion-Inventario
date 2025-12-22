from pydantic import BaseModel
from typing import Optional

class Articulos(BaseModel):
    id_articulo:int
    nombre_articulo:str
    precio_articulo:int
    marca_articulo:str
    descripcion_articulo:str
    stock:Optional[int]

    model_config = {
        "from_attributes": True}

class Articulos_Read(Articulos):
    pass