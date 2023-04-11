from .Base import Base


class Medicamento(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "medicamentos"

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                monodroga varchar,
                presentacion varchar,
                accion varchar,
                precio float
                );"""
        self.db.run(sql)
