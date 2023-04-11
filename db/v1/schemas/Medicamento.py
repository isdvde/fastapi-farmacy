from pydantic import BaseModel
from typing import Optional


class Medicamento(BaseModel):
    id: Optional[int]
    monodroga: str
    presentacion: str
    accion: str
    precio: float


class Create(BaseModel):
    monodroga: Optional[str]
    presentacion: Optional[str]
    accion: Optional[str]
    precio: Optional[float]
