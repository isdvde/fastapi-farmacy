from fastapi import APIRouter
from .Farmacia import Farmacia as FarmaciaRouter

v1 = APIRouter(prefix="/v1")
v1.include_router(FarmaciaRouter)
