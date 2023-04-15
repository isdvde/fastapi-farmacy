from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from db.v1.models.Medicamento import Medicamento as MedicamentoModel
from db.v1.schemas.Medicamento import Create as CreateMedicamentoSchema
from db.v1.schemas.Medicamento import Update as UpdateMedicamentoSchema
from db.v1.schemas.Medicamento import Medicamento as MedicamentoSchema

Medicamento = APIRouter(prefix="/medicamento", tags=['v1.medicamento'])


@Medicamento.get("/", status_code=status.HTTP_200_OK)
def get(id=""):
    db = MedicamentoModel()
    data = db.get(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Medicamento.post("/", status_code=status.HTTP_201_CREATED)
def set(f: CreateMedicamentoSchema):
    db = MedicamentoModel()
    try:
        data = MedicamentoSchema(**dict(f))
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


@Medicamento.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, f: UpdateMedicamentoSchema):
    db = MedicamentoModel()
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


@Medicamento.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete(id):
    db = MedicamentoModel()
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
