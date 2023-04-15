from psycopg2 import DatabaseError
from .Base import Base


class Inventario(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "inventario"
        self.attr = ('id', 'id_farmacia', 'id_medicamento', 'cantidad')

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                id_farmacia int not null,
                id_medicamento int not null,
                cantidad int not null
                );"""
        self.db.run(sql)

    def initRelations(self, data=...):
        return super().initRelations([
            ('id_farmacia', 'farmacias'),
            ('id_medicamento', 'medicamentos')])

    def getByFarmacia(self, id=""):
        try:
            sql = f"select id_medicamento, cantidad from {self.tablename} where id_farmacia = {id}"
            data = self.db.get(sql)
            return data
        except DatabaseError:
            return {}

    def insert(self, data=...):
        attr = ','.join(self.attr[1:])
        values = ",".join([str('%('+item+')s') for item in self.attr[1:]])
        return super().insert(attr=attr,
                              values=values,
                              data=data)

    def update(self, id="", data=...):
        return super().update(id, data)

    def delete(self, id=""):
        return super().delete(id)
