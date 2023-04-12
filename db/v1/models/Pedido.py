from psycopg2 import DatabaseError
from .Base import Base
from .Farmacia import Farmacia
from .Empleado import Empleado
from .Laboratorio import Laboratorio
from .PedidoMedicamento import PedidoMedicamento
from .Medicamento import Medicamento


class Pedido(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "pedidos"
        self.attr = ('id', 'id_farmacia', 'id_laboratorio', 'id_empleado', 'forma_pago')
        self.farmacia = Farmacia()
        self.empleado = Empleado()
        self.laboratorio = Laboratorio()
        self.pedidomedicamento = PedidoMedicamento()
        self.medicamento = Medicamento()

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                id_farmacia int not null,
                id_laboratorio int not null,
                id_empleado int not null,
                forma_pago varchar not null
                );"""
        self.db.run(sql)

    def initRelations(self, data=...):
        return super().initRelations([
            ('id_farmacia', 'farmacias'),
            ('id_laboratorio', 'laboratorios'),
            ('id_empleado', 'empleados')])

    def get(self, id=""):
        try:
            data = super().get(id)
            data = sorted([dict(zip(self.attr, dat)) for dat in data],
                          key=lambda k: k['id'])
            for d in data:
                f = self.farmacia.get(d['id_farmacia'])[0]
                e = self.empleado.get(d['id_empleado'])[0]
                la = self.laboratorio.get(d['id_laboratorio'])[0]
                pm = self.pedidomedicamento.getByPedido(d['id'])
                m = [self.medicamento.get(me[0])[0] for me in pm]
                d.update({
                    "farmacia": f,
                    "empleado": e,
                    "laboratorio": la,
                    "medicamentos": m})
            return data
        except DatabaseError:
            return {}

    def getMedicamentos(self, id=""):
        try:
            pm = self.pedidomedicamento.getByPedido(id)
            return [self.medicamento.get(me[0])[0] for me in pm]
        except DatabaseError:
            return {}

    def deleteMedicamentos(self, id_pedido="", id_medicamento=""):
        return self.pedidomedicamento.delete(id_pedido, id_medicamento)

    def getLastId(self):
        return super().getLastId()

    def insert(self, data=...):
        attr = ','.join(self.attr[1:])
        values = ",".join([str('%('+item+')s') for item in self.attr[1:]])
        if super().insert(attr=attr,
                          values=values,
                          data=data):
            for m in data['medicamentos']:
                print(m)
                self.pedidomedicamento.insert(
                        data={'id_pedido': self.getLastId(),
                              'id_medicamento': m})
            return True
        return False

    def update(self, id="", data=...):
        return super().update(id, data)

    def delete(self, id=""):
        if super().delete(id):
            self.pedidomedicamento.delete(id_pedido=id)
            return True
        return False
