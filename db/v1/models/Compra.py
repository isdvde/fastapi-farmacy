from psycopg2 import DatabaseError
from .Base import Base


class Compra(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "compras"
        self.attr = ('id', 'id_pedido', 'vencimiento', 'cancelado')

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                id_pedido int not null,
                vencimiento date,
                cancelado bool
                );"""
        self.db.run(sql)

    def initRelations(self, data=...):
        return super().initRelations([
            ('id_pedido', 'pedidos')])

    def get(self, id="", med=True):
        from .Pedido import Pedido
        from .CompraMedicamento import CompraMedicamento
        from .Medicamento import Medicamento
        pedido = Pedido()
        compramedicamento = CompraMedicamento()
        medicamento = Medicamento()
        try:
            data = super().get(id)
            data = sorted([dict(zip(self.attr, dat)) for dat in data],
                          key=lambda k: k['id'])
            for d in data:
                d['vencimiento'] = str(d['vencimiento'])
                p = pedido.get(d['id_pedido'], med=False)
                d.update({"pedido": p})
                if med:
                    cm = compramedicamento.getByCompra(d['id'])
                    m = [medicamento.get(me[0])[0] for me in cm]
                    d.update({"medicamentos": m})
            return data
        except DatabaseError:
            return {}

    def getLastId(self):
        return super().getLastId()

    def insert(self, data=...):
        from .CompraMedicamento import CompraMedicamento
        compramedicamento = CompraMedicamento()
        attr = ','.join(self.attr[1:])
        values = ",".join([str('%('+item+')s') for item in self.attr[1:]])
        if super().insert(attr=attr,
                          values=values,
                          data=data):
            for m in data['medicamentos']:
                print(m)
                compramedicamento.insert(
                        data={'id_compra': self.getLastId(),
                              'id_medicamento': m})
            return True
        return False

    def getMedicamentos(self, id=""):
        from .CompraMedicamento import CompraMedicamento
        from .Medicamento import Medicamento
        compramedicamento = CompraMedicamento()
        medicamento = Medicamento()
        try:
            cm = compramedicamento.getByCompra(id)
            return [medicamento.get(me[0])[0] for me in cm]
        except DatabaseError:
            return {}

    def deleteMedicamentos(self, id_compra="", id_medicamento=""):
        from .CompraMedicamento import CompraMedicamento
        compramedicamento = CompraMedicamento()
        return compramedicamento.delete(id_compra, id_medicamento)
