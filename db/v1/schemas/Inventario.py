from pydantic import BaseModel
from typing import Optional


class Inventario(BaseModel):
    id: Optional[int]
    id_farmacia: int
    id_medicamento: int
    cantidad: int
