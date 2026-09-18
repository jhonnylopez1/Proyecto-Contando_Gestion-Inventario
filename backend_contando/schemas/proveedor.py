from pydantic import BaseModel,Field
from typing import Optional

class Proveedor(BaseModel):
    id_proveedor:int
    nombre_proveedor:str=Field(min_length=2,max_length=50)
    tel_proveedor:str=Field(min_length=7,max_length=15,pattern=r"^\d{10}$")
    correo_proveedor:str=Field(min_length=5,max_length=50)
    direccion_proveedor:str=Field(min_length=2,max_length=50)

    model_config = {
            "from_attributes": True}

class Proveedor_Actualizar(BaseModel):
    nombre_proveedor:str=Field(min_length=2,max_length=50)
    tel_proveedor:str=Field(min_length=7,max_length=15,pattern=r"^\d{10}$")
    correo_proveedor:str=Field(min_length=5,max_length=50)
    direccion_proveedor:str=Field(min_length=2,max_length=50)

class Proveedor_Read(Proveedor):
    pass
    estado:Optional[int]=None

class Proveedor_Crear(BaseModel):
    nombre_proveedor:str=Field(min_length=2,max_length=50)
    tel_proveedor:str=Field(min_length=7,max_length=15,pattern=r"^\d{10}$")
    correo_proveedor:str=Field(min_length=5,max_length=50)
    direccion_proveedor:str=Field(min_length=2,max_length=50)