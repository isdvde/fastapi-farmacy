from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from db.v1.models.Pedido import Pedido as PedidoModel
from db.v1.schemas.Pedido import Create as CreatePedidoSchema
from db.v1.schemas.Pedido import Update as UpdatePedidoSchema
from db.v1.schemas.Pedido import Pedido as PedidoSchema

Pedido = APIRouter(prefix="/pedido", tags=['v1.pedido'])


@Pedido.get("/")
def get(id=""):
    db = PedidoModel()
    data = db.get(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Pedido.post("/")
def set(f: CreatePedidoSchema):
    db = PedidoModel()
    try:
        data = PedidoSchema(**dict(f))
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


@Pedido.patch("/{id}")
def update(id, f: UpdatePedidoSchema):
    db = PedidoModel()
    data = f.dict()
    if not db.update(id, data):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="No se ha podido actualizar los valores")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Actualizacion correcta")


@Pedido.delete("/{id}")
def delete(id):
    db = PedidoModel()
    if not db.delete(id):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="Error al borrar el registro")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Registro borrado con exito")


@Pedido.get("/{id}/medicamentos")
def getMedicamentos(id):
    db = PedidoModel()
    data = db.getMedicamentos(id)
    del db
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": data})


@Pedido.delete("/{id_pedido}/medicamento/{id_medicamento}")
def deleteMedicamentos(id_pedido, id_medicamento):
    db = PedidoModel()
    if not db.deleteMedicamentos(id_pedido, id_medicamento):
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            content="Error al borrar el registro")
    del db
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                        content="Registro borrado con exito")
