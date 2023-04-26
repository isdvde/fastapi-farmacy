from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from db.v1.models.Compra import Compra as CompraModel
from db.v1.schemas.Compra import Create as CreateCompraSchema
from db.v1.schemas.Compra import Update as UpdateCompraSchema
from db.v1.schemas.Compra import Compra as CompraSchema

Compra = APIRouter(prefix="/compra", tags=['v1.compra'])


@Compra.get("/")
def get(id=""):
    db = CompraModel()
    data = db.get(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Compra.post("/")
def set(f: CreateCompraSchema):
    db = CompraModel()
    try:
        data = CompraSchema(**dict(f))
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


@Compra.patch("/{id}")
def update(id, f: UpdateCompraSchema):
    db = CompraModel()
    data = f.dict()
    if not db.update(id, data):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="No se ha podido actualizar los valores")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Actualizacion correcta")


@Compra.delete("/{id}")
def delete(id):
    db = CompraModel()
    if not db.delete(id):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="Error al borrar el registro")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Registro borrado con exito")


@Compra.get("/{id}/medicamentos")
def getMedicamentos(id):
    db = CompraModel()
    data = db.getMedicamentos(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Compra.delete("/{id_pedido}/medicamento/{id_medicamento}")
def deleteMedicamentos(id_compra, id_medicamento):
    db = CompraModel()
    if not db.deleteMedicamentos(id_compra, id_medicamento):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="Error al borrar el registro")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Registro borrado con exito")
