from psycopg2 import DatabaseError
from .Base import Base
from .Farmacia import Farmacia


class Empleado(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "empleados"
        self.attr = ('id', 'id_farmacia', 'nombre', 'apellido', 'edad', 'cargo')
        self.farmacia = Farmacia()

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                id_farmacia int not null,
                nombre varchar not null,
                apellido varchar not null,
                edad int not null,
                cargo varchar
                );"""
        self.db.run(sql)

    def initRelations(self, data=...):
        return super().initRelations([('id_farmacia', 'farmacias')])

    def get(self, id=""):
        try:
            data = super().get(id)
            data = sorted([dict(zip(self.attr, dat)) for dat in data],
                          key=lambda k: k['id'])
            for d in data:
                f = self.farmacia.get(d['id_farmacia'])[0]
                d.update({"farmacia": f})
            return data
        except DatabaseError:
            return {}

    def insert(self, data=...):
        return super().insert(
                attr="id_farmacia, nombre, apellido, edad, cargo",
                values="%(id_farmacia)s, %(nombre)s, %(apellido)s, %(edad)s, %(cargo)s",
                data=data)

    def update(self, id="", data=...):
        return super().update(id, data)

    def delete(self, id=""):
        return super().delete(id)
