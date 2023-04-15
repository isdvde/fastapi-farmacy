from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from db.v1.models.Farmacia import Farmacia as FarmaciaModel
from db.v1.schemas.Farmacia import Create as CreateFarmaciaSchema
from db.v1.schemas.Farmacia import Farmacia as FarmaciaSchema

Farmacia = APIRouter(prefix="/farmacia", tags=['v1.farmacia'])


@Farmacia.get("/")
def get(id=""):
    db = FarmaciaModel()
    data = db.get(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Farmacia.post("/", status_code=status.HTTP_201_CREATED)
def set(f: CreateFarmaciaSchema):
    db = FarmaciaModel()
    try:
        data = FarmaciaSchema(**dict(f))
        if not db.insert(dict(data)):
            data = {"status": "Error",
                    "message": "No se ha podido crear el registro"}
            return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                content=jsonable_encoder(data))
    except ValidationError as e:
        data = {"message": "Debe cumplir con los parametros",
                "error": f"{e}"}
        return JSONResponse(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                content=jsonable_encoder(data))
    del db
    data = {"status": "Ok",
            "message": "Registro agregado exitosamente"}
    return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder(data))


@Farmacia.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, f: CreateFarmaciaSchema):
    db = FarmaciaModel()
    data = f.dict()
    if not db.update(id, data):
        data = {"status": "Error",
                "message": "No se ha podido actualizar el registro"}
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content=jsonable_encoder(data))
    del db
    data = {"status": "Ok",
            "message": "Actualizacion correcta"}
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content=jsonable_encoder(data))


@Farmacia.delete("/{id}")
def delete(id):
    db = FarmaciaModel()
    if not db.delete(id):
        data = {"status": "Error",
                "message": "No se ha podido borrar el registro"}
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content=jsonable_encoder(data))
    del db
    data = {"status": "Ok",
            "message": "Registro borado correctamente"}
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content=jsonable_encoder(data))


@Farmacia.get("/{id}/inventario")
def getInventario(id: str):
    db = FarmaciaModel()
    data = db.getMedicamentos(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})
