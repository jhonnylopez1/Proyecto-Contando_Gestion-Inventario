from typing import Optional
from sqlmodel import SQLModel, Field

class Articulo(SQLModel, table=True):
    __tablename__ = "articulo"

    id_articulo:int = Field(primary_key=True)
    nombre_articulo:str = Field(max_length=50)
    precio_articulo:int
    marca_articulo:str = Field(max_length=30)
    descripcion_articulo:str = Field(max_length=50)
    stock:Optional[int] = Field(default=0)



