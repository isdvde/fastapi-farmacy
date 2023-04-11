from fastapi import APIRouter
from .Farmacia import Farmacia as FarmaciaRouter
from .Empleado import Empleado as EmpleadoRouter
from .Medicamento import Medicamento as MedicamentoRouter
from .Laboratorio import Laboratorio as LaboratorioRouter

v1 = APIRouter(prefix="/v1")
v1.include_router(FarmaciaRouter)
v1.include_router(EmpleadoRouter)
v1.include_router(MedicamentoRouter)
v1.include_router(LaboratorioRouter)
