from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from db.v1.models.Farmacia import Farmacia as FarmaciaModel
from db.v1.schemas.Farmacia import Create as CreateFarmaciaSchema
from db.v1.schemas.Farmacia import Farmacia as FarmaciaSchema

Farmacia = APIRouter(prefix="/farmacia", tags=['v1.farmacia'])


@Farmacia.get("/")
def get():
    db = FarmaciaModel()
    data = db.get()
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})

@Farmacia.get("/{id}")
def getById(id: str):
    db = FarmaciaModel()
    data = db.get(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


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
    data = f.dict()
    if not db.update(id, data):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="No se ha podido actualizar los valores")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Actualizacion correcta")


@Farmacia.delete("/{id}")
def delete(id):
    db = FarmaciaModel()
    if not db.delete(id):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="Error al borrar el registro")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Registro borrado con exito")

    del db
