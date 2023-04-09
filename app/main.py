from fastapi import FastAPI
from routes.Farmacia import Farmacia as FarmaciaRouter

app = FastAPI()

app.include_router(FarmaciaRouter)
