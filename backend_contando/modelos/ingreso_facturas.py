from sqlmodel import SQLModel,Field
from datetime import date
from enum import Enum

class EstadoPago(str,Enum):
    pendiente="pendiente"
    pagada="pagada"

class IngresoCompra(SQLModel,table=True):
    __tablename__="ingreso_compra"
    id_ingreso_compra:int=Field(primary_key=True)
    id_proveedor:int=Field(foreign_key="proveedor.id_proveedor")
    numero_factura_proveedor:str|None=Field(default=None,max_length=50)
    fecha_ingreso:date
    estado_pago:EstadoPago
    total:int=0

class DetalleIngreso(SQLModel,table=True):
    __tablename__="detalle_ingreso"
    id_detalle_ingreso:int=Field(primary_key=True)
    id_ingreso_compra:int=Field(foreign_key="ingreso_compra.id_ingreso_compra")
    id_articulo:int=Field(foreign_key="articulo.id_articulo")
    cantidad:int
    precio_unitario:int
    subtotal:int