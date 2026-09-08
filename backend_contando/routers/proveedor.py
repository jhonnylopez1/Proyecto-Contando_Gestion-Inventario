#importaciones necesarias para crear el modulo router para proveedor
from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session,select
from typing import List,Optional

from backend_contando.db import engine
from backend_contando.modelos.proveedor import Proveedor
from backend_contando.schemas.proveedor import Proveedor_Read,Proveedor_Actualizar,Proveedor_Crear

#Definir nombre de la ruta
router = APIRouter(
    prefix="/proveedores",
    tags=["Proveedores"]
)

