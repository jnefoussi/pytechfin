from pytechfin import Techfin,  TechfinDataModel
from pytechfin.enums import EnumApps

tf = Techfin()
dm = TechfinDataModel(tf)

pks = dm.get_pks(dm_name='arinvoice', carol_tenant='tenant70827589d8a611eabbf10a586460272f',
               page_size=5000, techfin_app=EnumApps.CASHFLOW.value)

print(f'Get by TechfinDataModel Class: {pks}')


# With Context Class

from pytechfin import Context
from pytechfin.enums import EnumApps

context = Context(use_production_context=True, carol_tenant='tenant70827589d8a611eabbf10a586460272f')
pks = context.techfin.datamodel.get_pks('arinvoice', page_size=5000, techfin_app=EnumApps.CASHFLOW.value)
print(f'Get by Context Class: {pks}')
