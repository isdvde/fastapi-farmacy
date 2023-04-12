from psycopg2 import DatabaseError
from .Base import Base


class PedidoMedicamento(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "pedido_medicamento"
        self.attr = ('id', 'id_pedido', 'id_medicamento')

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                id_pedido int not null,
                id_medicamento int not null
                );"""
        self.db.run(sql)

    def initRelations(self, data=...):
        return super().initRelations([
            ('id_pedido', 'pedidos'),
            ('id_medicamento', 'medicamentos')])

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

    def getByPedido(self, id=""):
        try:
            sql = f"select id_medicamento from {self.tablename} where id_pedido = {id}"
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

    def delete(self, id_pedido="", id_medicamento=""):
        try:
            if id_medicamento:
                sql = (f"delete from {self.tablename} " +
                       f"where id_pedido = {id_pedido} "
                       f"and id_medicamento = {id_medicamento}")
            else:
                sql = f"delete from {self.tablename} where id_pedido = {id_pedido}"
            self.db.run(sql)
            return True
        except DatabaseError as e:
            print(e)
            return False
