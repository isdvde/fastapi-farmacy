from pydantic import BaseModel
from typing import Optional


class Laboratorio(BaseModel):
    id: Optional[int]
    id_farmacia: int
    id_laboratorio: int
    id_empleado: int
    forma_pago: str
