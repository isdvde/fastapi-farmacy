from db.models.Compra import Compra as CompraModel
from db.models.CompraMedicamento import CompraMedicamento as CompraMedicamentoModel
from db.models.Empleado import Empleado as EmpleadoModel
from db.models.Farmacia import Farmacia as FarmaciaModel
from db.models.Inventario import Inventario as InventarioModel
from db.models.Laboratorio import Laboratorio as LaboratorioModel
from db.models.LaboratorioMedicamento import LaboratorioMedicamento as LaboratorioMedicamentoModel
from db.models.Medicamento import Medicamento as MedicamentoModel
from db.models.Pedido import Pedido as PedidoModel
from db.models.PedidoMedicamento import PedidoMedicamento as PedidoMedicamentoModel

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
