from pydantic import BaseModel
from typing import Optional


class LaboratorioMedicamento(BaseModel):
    id: Optional[int]
    id_laboratorio: int
    id_medicamento: int
