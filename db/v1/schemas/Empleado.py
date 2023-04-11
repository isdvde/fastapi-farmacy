from pydantic import BaseModel
from typing import Optional


class Empleado(BaseModel):
    id: Optional[int]
    id_farmacia: int
    nombre: str
    apellido: str
    edad: int
    cargo: str


class Create(BaseModel):
    id_farmacia: Optional[int]
    nombre: Optional[str]
    apellido: Optional[str]
    edad: Optional[int]
    cargo: Optional[str]
