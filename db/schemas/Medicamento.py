from pydantic import BaseModel
from typing import Optional


class Medicamento(BaseModel):
    id: Optional[int]
    monodroga: str
    presentacion: str
    accion: str
    precio: float
