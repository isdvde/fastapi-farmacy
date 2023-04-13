from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from db.v1.models.Laboratorio import Laboratorio as LaboratorioModel
from db.v1.schemas.Laboratorio import Create as CreateLaboratorioSchema
from db.v1.schemas.Laboratorio import Laboratorio as LaboratorioSchema

Laboratorio = APIRouter(prefix="/laboratorio", tags=['v1.laboratorio'])


@Laboratorio.get("/")
def get():
    db = LaboratorioModel()
    data = db.get()
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Laboratorio.get("/{id}")
def getById(id: str):
    db = LaboratorioModel()
    data = db.get(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Laboratorio.post("/")
def set(f: CreateLaboratorioSchema):
    db = LaboratorioModel()
    try:
        data = LaboratorioSchema(**dict(f))
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


@Laboratorio.patch("/{id}")
def update(id, f: CreateLaboratorioSchema):
    db = LaboratorioModel()
    data = f.dict()
    if not db.update(id, data):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="No se ha podido actualizar los valores")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Actualizacion correcta")


@Laboratorio.delete("/{id}")
def delete(id):
    db = LaboratorioModel()
    if not db.delete(id):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="Error al borrar el registro")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Registro borrado con exito")


@Laboratorio.get("/{id}/medicamentos")
def getMedicamentos(id):
    db = LaboratorioModel()
    data = db.getMedicamentos(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})
