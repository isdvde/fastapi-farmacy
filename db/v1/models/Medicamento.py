from psycopg2 import DatabaseError
from .LaboratorioMedicamento import LaboratorioMedicamento
from .Base import Base


class Medicamento(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "medicamentos"
        self.attr = ('id', 'monodroga', 'presentacion', 'accion', 'precio')
        self.laboratoriomedicamento = LaboratorioMedicamento()

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                monodroga varchar,
                presentacion varchar,
                accion varchar,
                precio float
                );"""
        self.db.run(sql)

    def get(self, id="", laboratorio=True):
        try:
            data = super().get(id)
            data = sorted([dict(zip(self.attr, dat)) for dat in data],
                          key=lambda k: k['id'])
            if laboratorio:
                for d in data:
                    la = self.getLaboratorio(d['id'])
                    d.update({'laboratorio': la})
            return data if data else []
        except DatabaseError:
            return {}

    def getLaboratorio(self, id=""):
        from .Laboratorio import Laboratorio
        laboratorio = Laboratorio()
        try:
            id_laboratorio = self.laboratoriomedicamento.getByMedicamento(id)
            data = [laboratorio.get(id[0], False)[0] for id in id_laboratorio]
            return data if data else []
        except DatabaseError:
            return {}

    def getLastId(self):
        return super().getLastId()

    def insert(self, data=...):
        attr = ','.join(self.attr[1:])
        values = ",".join([str('%('+item+')s') for item in self.attr[1:]])
        if super().insert(attr=attr,
                          values=values,
                          data=data):
            self.laboratoriomedicamento.insert(
                    data={'id_medicamento': self.getLastId(),
                          'id_laboratorio': data['laboratorio']})
            return True
        return False

    def update(self, id="", data=...):
        return super().update(id, data)

    def delete(self, id=""):
        return super().delete(id)
