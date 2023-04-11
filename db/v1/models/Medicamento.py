from psycopg2 import DatabaseError
from .Base import Base


class Medicamento(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "medicamentos"
        self.attr = ('id', 'monodroga', 'presentacion', 'accion', 'precio')

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                monodroga varchar,
                presentacion varchar,
                accion varchar,
                precio float
                );"""
        self.db.run(sql)

    def get(self, id=""):
        try:
            data = super().get(id)
            return sorted([dict(zip(self.attr, dat)) for dat in data],
                          key=lambda k: k['id'])
        except DatabaseError:
            return {}

    def insert(self, data=...):
        return super().insert(attr="monodroga, presentacion, accion, precio",
                              values="%(monodroga)s, %(presentacion)s, %(accion)s, %(precio)s",
                              data=data)

    def update(self, id="", data=...):
        return super().update(id, data)

    def delete(self, id=""):
        return super().delete(id)
