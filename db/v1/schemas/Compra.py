from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class Compra(BaseModel):
    id: Optional[int]
    id_pedido: int
    vencimiento: datetime
    cancelado: bool
    medicamentos: List[int]


class Create(BaseModel):
    id_pedido: Optional[int]
    vencimiento: Optional[datetime]
    cancelado: Optional[bool]
    medicamentos: Optional[List[int]]


class Update(BaseModel):
    id_farmacia: Optional[int]
    id_laboratorio: Optional[int]
    id_empleado: Optional[int]
    forma_pago: Optional[str]
