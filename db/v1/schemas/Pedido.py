from pydantic import BaseModel
from typing import List, Optional


class Pedido(BaseModel):
    id: Optional[int]
    id_farmacia: int
    id_laboratorio: int
    id_empleado: int
    forma_pago: str
    medicamentos: List[int]


class Create(BaseModel):
    id_farmacia: Optional[int]
    id_laboratorio: Optional[int]
    id_empleado: Optional[int]
    forma_pago: Optional[str]
    medicamentos: Optional[List[int]]


class Update(BaseModel):
    id_farmacia: Optional[int]
    id_laboratorio: Optional[int]
    id_empleado: Optional[int]
    forma_pago: Optional[str]
