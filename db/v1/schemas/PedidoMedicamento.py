from pydantic import BaseModel
from typing import Optional


class PedidoMedicamento(BaseModel):
    id: Optional[int]
    id_farmacia: int
    id_pedido: int
    id_medicamento: int


class Create(BaseModel):
    id_farmacia: Optional[int]
    id_pedido: Optional[int]
    id_medicamento: Optional[int]
