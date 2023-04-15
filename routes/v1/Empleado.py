from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from db.v1.models.Empleado import Empleado as EmpleadoModel
from db.v1.schemas.Empleado import Create as CreateEmpleadoSchema
from db.v1.schemas.Empleado import Empleado as EmpleadoSchema

Empleado = APIRouter(prefix="/empleado", tags=['v1.empleado'])


@Empleado.get("/", status_code=status.HTTP_200_OK)
def get(id=""):
    db = EmpleadoModel()
    data = db.get(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Empleado.post("/", status_code=status.HTTP_201_CREATED)
def set(f: CreateEmpleadoSchema):
    db = EmpleadoModel()
    try:
        data = EmpleadoSchema(**dict(f))
        if not db.insert(dict(data)):
            data = {"status": "Error",
                    "message": "No se ha podido crear el registro"}
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
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


@Empleado.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, f: CreateEmpleadoSchema):
    db = EmpleadoModel()
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


@Empleado.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete(id):
    db = EmpleadoModel()
    if not db.delete(id):
        data = {"status": "Error",
                "message": "No se ha podido borrar el registro"}
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content=jsonable_encoder(data))
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Registro borrado con exito")
