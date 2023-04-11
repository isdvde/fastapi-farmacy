from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from db.v1.models.Medicamento import Medicamento as MedicamentoModel
from db.v1.schemas.Medicamento import Create as CreateMedicamentoSchema
from db.v1.schemas.Medicamento import Medicamento as MedicamentoSchema

Medicamento = APIRouter(prefix="/medicamento", tags=['v1.medicamento'])


@Medicamento.get("/")
def get():
    db = MedicamentoModel()
    data = db.get()
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Medicamento.get("/{id}")
def getById(id: str):
    db = MedicamentoModel()
    data = db.get(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Medicamento.post("/")
def set(f: CreateMedicamentoSchema):
    db = MedicamentoModel()
    try:
        data = MedicamentoSchema(**dict(f))
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


@Medicamento.patch("/{id}")
def update(id, f: CreateMedicamentoSchema):
    db = MedicamentoModel()
    data = f.dict()
    if not db.update(id, data):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="No se ha podido actualizar los valores")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Actualizacion correcta")


@Medicamento.delete("/{id}")
def delete(id):
    db = MedicamentoModel()
    if not db.delete(id):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="Error al borrar el registro")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Registro borrado con exito")

    del db
