#importaciones necesarias para crear el router ingreso_factura
from fastapi import APIRouter, Depends,HTTPException
from sqlmodel import Session,select
from typing import List, Optional

from backend_contando.db import engine
from backend_contando.modelos.ingreso_facturas import IngresoCompra,DetalleIngreso
from backend_contando.schemas.ingreso_facturas import IngresoCompraCrear,DetalleIngresoCrear,IngresoCompraRead,DetalleIngresoRead,IngresoCompraDetalleRead,EstadoPagoUpdate,IngresoCompraCrearResponse

#Se define el nombre de la ruta
router = APIRouter(
    prefix="/ingreso_facturas",
    tags=["Ingreso_Facturas"]
)

#Ruta post para ingresar una factura
@router.post("/",response_model=IngresoCompraCrearResponse)
def crear_ingreso_facturas(data:IngresoCompraCrear):
    try:
        with Session(engine) as session:
            nueva_factura_ingreso= IngresoCompra(
                id_proveedor=data.id_proveedor,
                numero_factura_proveedor=data.numero_factura_proveedor,
                fecha_ingreso=data.fecha_ingreso,
                estado_pago=data.estado_pago,
            )
            session.add(nueva_factura_ingreso)
            session.flush() #Hace una especie de Post "temporal" antes de enviar el commit definitivo
            total=0
            for detalle in data.detalle:
                subtotal=detalle.cantidad*detalle.precio_unitario
                total+=subtotal
                ingreso_nuevo_detalle=DetalleIngreso(
                    id_ingreso_compra=nueva_factura_ingreso.id_ingreso_compra,
                    id_articulo=detalle.id_articulo,
                    cantidad=detalle.cantidad,
                    precio_unitario=detalle.precio_unitario,
                    subtotal=subtotal
                )
                session.add(ingreso_nuevo_detalle)
            nueva_factura_ingreso.total=total
            session.commit()
            return IngresoCompraCrearResponse(
                mensaje="Ingreso creado correctamente",
                id_ingreso_compra=nueva_factura_ingreso.id_ingreso_compra
            )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al crear articulo:{str(e)}"
        )

