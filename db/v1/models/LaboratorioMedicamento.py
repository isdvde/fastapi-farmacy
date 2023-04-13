from psycopg2 import DatabaseError
from .Base import Base


class LaboratorioMedicamento(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "laboratorio_medicamento"
        self.attr = ('id', 'id_laboratorio', 'id_medicamento')

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                id_laboratorio int not null,
                id_medicamento int not null
                );"""
        self.db.run(sql)

    def initRelations(self, data=...):
        return super().initRelations([
            ('id_laboratorio', 'laboratorios'),
            ('id_medicamento', 'medicamentos')])

    def getByLaboratorio(self, id=""):
        try:
            data = []
            sql = f"select id_medicamento from {self.tablename} where id_laboratorio = {id}"
            data = self.db.get(sql)
            return data if data else []
        except DatabaseError:
            return {}

    def getByMedicamento(self, id=""):
        try:
            data = []
            sql = f"select id_laboratorio from {self.tablename} where id_medicamento = {id}"
            data = self.db.get(sql)
            return data if data else []
        except DatabaseError:
            return {}

    def insert(self, data=...):
        attr = ','.join(self.attr[1:])
        values = ",".join([str('%('+item+')s') for item in self.attr[1:]])
        return super().insert(attr=attr,
                              values=values,
                              data=data)

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
