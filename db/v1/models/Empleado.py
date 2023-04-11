from .Base import Base


class Empleado(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "empleados"

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                id_farmacia int not null,
                nombre varchar not null,
                apellido varchar not null,
                edad int not null,
                cargo varchar
                );"""
        self.db.run(sql)

    def initRelations(self, data=...):
        return super().initRelations([('id_farmacia', 'farmacias')])
