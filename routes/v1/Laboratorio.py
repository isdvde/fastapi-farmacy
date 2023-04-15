from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from db.v1.models.Laboratorio import Laboratorio as LaboratorioModel
from db.v1.schemas.Laboratorio import Create as CreateLaboratorioSchema
from db.v1.schemas.Laboratorio import Laboratorio as LaboratorioSchema

Laboratorio = APIRouter(prefix="/laboratorio", tags=['v1.laboratorio'])


@Laboratorio.get("/", status_code=status.HTTP_200_OK)
def get(id=""):
    db = LaboratorioModel()
    data = db.get(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Laboratorio.post("/", status_code=status.HTTP_201_CREATED)
def set(f: CreateLaboratorioSchema):
    db = LaboratorioModel()
    try:
        data = LaboratorioSchema(**dict(f))
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


@Laboratorio.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, f: CreateLaboratorioSchema):
    db = LaboratorioModel()
    data = f.dict()
    if not db.update(id, data):
        data = {"status": "Error",
                "message": "No se ha podido actualizar el registro"}
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content=jsonable_encoder(data))
    del db
    data = {"status": "Ok",
            "message": "Registro actualizado exitosamente"}
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content=jsonable_encoder(data))


@Laboratorio.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete(id):
    db = LaboratorioModel()
    if not db.delete(id):
        data = {"status": "Error",
                "message": "No se ha podido borrar el registro"}
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content=jsonable_encoder(data))
    del db
    data = {"status": "Ok",
            "message": "Registro borrado exitosamente"}
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content=jsonable_encoder(data))


@Laboratorio.get("/{id}/medicamentos", status_code=status.HTTP_200_OK)
def getMedicamentos(id):
    db = LaboratorioModel()
    data = db.getMedicamentos(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})
