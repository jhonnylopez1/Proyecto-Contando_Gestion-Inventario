from sqlmodel import SQLModel,Field

class Proveedor(SQLModel,table=True):
    __tablename__="proveedor"

    id_proveedor:int=Field(primary_key=True)
    nombre_proveedor:str=Field(max_length=50)
    tel_proveedor:int=Field(max_length=15)
    correo_proveedor:str=Field(max_length=50)
    direccion_proveedor:str=Field(max_length=50)
    estado:int