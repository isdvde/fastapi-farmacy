from .Base import Base


class LaboratorioMedicamento(Base):
    def __init__(self):
        super().__init__()
        self.tablename = "laboratorio_medicamento"

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
