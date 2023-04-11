from .Base import Base


class Inventario(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "inventario"

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
