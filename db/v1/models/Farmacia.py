from psycopg2 import DatabaseError
from .Base import Base
from .Inventario import Inventario


class Farmacia(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "farmacias"
        self.attr = ('id', 'nombre', 'ubicacion')
        self.inventario = Inventario()

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
            return sorted([dict(zip(self.attr, dat)) for dat in data],
                          key=lambda k: k['id'])
        except DatabaseError:
            return {}

    def getMedicamentos(self, id=""):
        from .Medicamento import Medicamento
        medicamento = Medicamento()
        try:
            inv = self.inventario.getByFarmacia(id)
            print(inv)
            data = []
            for me in inv:
                med = medicamento.get(me[0])[0]
                med.update({"cantidad": me[1]})
                data.append(med)
            return data if data else []
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
