from pydantic import BaseModel,Field
from typing import Optional
from datetime import date
from backend_contando.modelos.ingreso_facturas import EstadoPago,EstadoIngreso

class DetalleIngresoCrear(BaseModel):
    id_articulo:int
    cantidad:int
    precio_unitario:int

class IngresoCompraCrear(BaseModel):
    id_proveedor:int
    numero_factura_proveedor:str|None=Field(default=None,max_length=50)
    fecha_ingreso:date
    estado_pago:EstadoPago
    detalle:list[DetalleIngresoCrear]

class IngresoCompraCrearResponse(BaseModel):
    mensaje: str
    id_ingreso_compra: int

class IngresoCompraRead(BaseModel):
    id_ingreso_compra:int
    nombre_proveedor:str
    numero_factura_proveedor:str|None=Field(default=None,max_length=50)
    fecha_ingreso:date
    estado_pago:EstadoPago
    estado_ingreso:EstadoIngreso
    total:int

class DetalleIngresoRead(BaseModel):
    nombre_articulo:str
    cantidad:int
    precio_unitario:int
    subtotal:int

class IngresoCompraDetalleRead(IngresoCompraRead):
    detalles:list[DetalleIngresoRead]
    
class EstadoPagoUpdate(BaseModel):
    estado_pago:EstadoPago

