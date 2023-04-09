from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from db.models.Farmacia import Farmacia as FarmaciaModel
from db.schemas.Farmacia import Create as CreateFarmaciaSchema
from db.schemas.Farmacia import Farmacia as FarmaciaSchema

Farmacia = APIRouter(prefix="/farmacia", tags=['farmacia'])


@Farmacia.get("/")
def get():
    db = FarmaciaModel()
    data = db.get()
    del db
    return data


@Farmacia.get("/{id}")
def getById(id: str):
    db = FarmaciaModel()
    data = db.get(id)
    del db
    return data


@Farmacia.post("/")
def set(f: CreateFarmaciaSchema):
    db = FarmaciaModel()
    try:
        data = FarmaciaSchema(**dict(f))
        if not db.insert(dict(data)):
            return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                content="No se ha podido crear el registro")
    except ValidationError as e:
        data = {"message": "Debe cumplir con los parametros",
                "error": f"{e}"}
        return JSONResponse(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                content=jsonable_encoder(data))
    del db
    return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content="Registro creado correctamente")


@Farmacia.patch("/{id}")
def update(id, f: CreateFarmaciaSchema):
    db = FarmaciaModel()

    del db


@Farmacia.delete("/{id}")
def delete(id):
    db = FarmaciaModel()

    del db
