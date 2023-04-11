from fastapi import FastAPI
from routes.v1.v1 import v1 as v1Router

app = FastAPI()

app.include_router(v1Router)
