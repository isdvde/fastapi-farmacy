from pydantic import BaseModel
from typing import Optional


class CompraMedicamento(BaseModel):
    id: Optional[int]
    id_compra: int
    id_medicamento: int
