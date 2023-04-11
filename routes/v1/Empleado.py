from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from db.v1.models.Empleado import Empleado as EmpleadoModel
from db.v1.schemas.Empleado import Create as CreateEmpleadoSchema
from db.v1.schemas.Empleado import Empleado as EmpleadoSchema

Empleado = APIRouter(prefix="/empleado", tags=['v1.empleado'])


@Empleado.get("/")
def get():
    db = EmpleadoModel()
    data = db.get()
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Empleado.get("/{id}")
def getById(id: str):
    db = EmpleadoModel()
    data = db.get(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Empleado.post("/")
def set(f: CreateEmpleadoSchema):
    db = EmpleadoModel()
    try:
        data = EmpleadoSchema(**dict(f))
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


@Empleado.patch("/{id}")
def update(id, f: CreateEmpleadoSchema):
    db = EmpleadoModel()
    data = f.dict()
    if not db.update(id, data):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="No se ha podido actualizar los valores")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Actualizacion correcta")


@Empleado.delete("/{id}")
def delete(id):
    db = EmpleadoModel()
    if not db.delete(id):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="Error al borrar el registro")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Registro borrado con exito")

    del db
