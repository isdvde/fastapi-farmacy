from .Base import Base


class Pedido(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "pedidos"

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
