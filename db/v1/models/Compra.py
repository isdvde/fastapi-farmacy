from .Base import Base


class Compra(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "compras"

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
