from db.v1.models.Compra import Compra as CompraModel
from db.v1.models.CompraMedicamento import CompraMedicamento as CompraMedicamentoModel
from db.v1.models.Empleado import Empleado as EmpleadoModel
from db.v1.models.Farmacia import Farmacia as FarmaciaModel
from db.v1.models.Inventario import Inventario as InventarioModel
from db.v1.models.Laboratorio import Laboratorio as LaboratorioModel
from db.v1.models.LaboratorioMedicamento import LaboratorioMedicamento as LaboratorioMedicamentoModel
from db.v1.models.Medicamento import Medicamento as MedicamentoModel
from db.v1.models.Pedido import Pedido as PedidoModel
from db.v1.models.PedidoMedicamento import PedidoMedicamento as PedidoMedicamentoModel

c = CompraModel()
c.drop()
c.init()

cm = CompraMedicamentoModel()
cm.drop()
cm.init()

e = EmpleadoModel()
e.drop()
e.init()

f = FarmaciaModel()
f.drop()
f.init()

i = InventarioModel()
i.drop()
i.init()

la = LaboratorioModel()
la.drop()
la.init()

lm = LaboratorioMedicamentoModel()
lm.drop()
lm.init()

m = MedicamentoModel()
m.drop()
m.init()

p = PedidoModel()
p.drop()
p.init()

pm = PedidoMedicamentoModel()
pm.drop()
pm.init()

c.initRelations()
cm.initRelations()
e.initRelations()
f.initRelations()
i.initRelations()
la.initRelations()
m.initRelations()
p.initRelations()
pm.initRelations()
lm.initRelations()
