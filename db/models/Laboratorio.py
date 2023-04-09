from .Base import Base


class Laboratorio(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "laboratorios"

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                nombre varchar unique not null,
                ubicacion varchar,
                telefono varchar
                );"""
        self.db.run(sql)
