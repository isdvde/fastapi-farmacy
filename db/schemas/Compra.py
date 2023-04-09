from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Compra(BaseModel):
    id: Optional[int]
    id_pedido: int
    vencimiento: datetime
    cancelado: bool
