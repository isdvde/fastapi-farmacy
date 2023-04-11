from fastapi import APIRouter
from .Farmacia import Farmacia as FarmaciaRouter
from .Empleado import Empleado as EmpleadoRouter

v1 = APIRouter(prefix="/v1")
v1.include_router(FarmaciaRouter)
v1.include_router(EmpleadoRouter)
