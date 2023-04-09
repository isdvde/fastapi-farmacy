from psycopg2 import DatabaseError
from .Base import Base


class Farmacia(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "farmacias"
        self.attr = ('id', 'nombre', 'ubicacion')

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                nombre varchar unique not null,
                ubicacion varchar
                );"""
        self.db.run(sql)

    def get(self, id=""):
        try:
            data = super().get(id)
            return [dict(zip(self.attr, dat)) for dat in data]
        except DatabaseError:
            return {}

    def insert(self, data=...):
        return super().insert(attr="nombre, ubicacion",
                              values="%(nombre)s, %(ubicacion)s",
                              data=data)
