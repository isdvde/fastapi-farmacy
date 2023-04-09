from pydantic import BaseModel
from typing import Optional


class Laboratorio(BaseModel):
    id: Optional[int]
    nombre: str
    ubicacion: str
    telefono: str
