from psycopg2 import DatabaseError
from .Base import Base


class CompraMedicamento(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "compra_medicamento"
        self.attr = ('id', 'id_compra', 'id_medicamento')

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                id_compra int not null,
                id_medicamento int not null
                );"""
        self.db.run(sql)

    def initRelations(self, data=...):
        return super().initRelations([
            ('id_compra', 'compras'),
            ('id_medicamento', 'medicamentos')])

    def getByCompra(self, id=""):
        try:
            sql = f"select id_medicamento from {self.tablename} where id_compra = {id}"
            data = self.db.get(sql)
            return data
        except DatabaseError:
            return {}

    def delete(self, id_compra="", id_medicamento=""):
        try:
            if id_medicamento:
                sql = (f"delete from {self.tablename} " +
                       f"where id_compra = {id_compra} "
                       f"and id_medicamento = {id_medicamento}")
            else:
                sql = f"delete from {self.tablename} where id_compra = {id_compra}"
            self.db.run(sql)
            return True
        except DatabaseError as e:
            print(e)
            return False

    def insert(self, data=...):
        attr = ','.join(self.attr[1:])
        values = ",".join([str('%('+item+')s') for item in self.attr[1:]])
        return super().insert(attr=attr,
                              values=values,
                              data=data)
