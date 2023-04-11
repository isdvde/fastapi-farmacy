from .Base import Base


class CompraMedicamento(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "compra_medicamento"

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
