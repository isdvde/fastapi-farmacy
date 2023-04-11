from pydantic import BaseModel, Field
from typing import Optional


class Farmacia(BaseModel):
    id: Optional[int]
    nombre: str = Field(nullable=False)
    ubicacion: str = Field(nullable=False)


class Create(BaseModel):
    nombre: Optional[str]
    ubicacion: Optional[str]

