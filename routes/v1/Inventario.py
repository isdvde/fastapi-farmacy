from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from db.v1.models.Inventario import Inventario as InventarioModel
from db.v1.schemas.Inventario import Create as CreateInventarioSchema
from db.v1.schemas.Inventario import Inventario as InventarioSchema

Inventario = APIRouter(prefix="/inventario", tags=['v1.inventario'])


@Inventario.get("/")
def get():
    db = InventarioModel()
    data = db.get()
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Inventario.get("/{id}")
def getById(id: str):
    db = InventarioModel()
    data = db.get(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Inventario.post("/")
def set(f: CreateInventarioSchema):
    db = InventarioModel()
    try:
        data = InventarioSchema(**dict(f))
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


@Inventario.patch("/{id}")
def update(id, f: CreateInventarioSchema):
    db = InventarioModel()
    data = f.dict()
    if not db.update(id, data):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="No se ha podido actualizar los valores")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Actualizacion correcta")


@Inventario.delete("/{id}")
def delete(id):
    db = InventarioModel()
    if not db.delete(id):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="Error al borrar el registro")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Registro borrado con exito")

    del db
