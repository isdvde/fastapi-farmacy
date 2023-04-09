from .Base import Base


class PedidoMedicamento(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "pedido_medicamento"

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
