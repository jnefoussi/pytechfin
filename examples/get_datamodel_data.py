from pytechfin import Techfin,  TechfinDataModel
from pytechfin.enums import EnumApps

tf = Techfin()
dm = TechfinDataModel(tf)


pks = dm.get_pks(dm_name='arinvoice', carol_tenant='tenant70827589d8a611eabbf10a586460272f',
                  page_size=10, techfin_app=EnumApps.CASHFLOW.value, max_hits=10)

pks = pks[:10]
pks = dm.get_data_by_pk(dm_name='arinvoice', pk_list=pks, carol_tenant='tenant70827589d8a611eabbf10a586460272f',
               page_size=5000, techfin_app=EnumApps.CASHFLOW.value)

print(f'Get by TechfinDataModel Class: {pks.shape}')


# With Context Class

from pytechfin import Context
from pytechfin.enums import EnumApps

context = Context(use_production_context=True, carol_tenant='tenant70827589d8a611eabbf10a586460272f')
pks = context.techfin.datamodel.get_data_by_pk('arinvoice', page_size=5000,  pk_list=pks, techfin_app=EnumApps.CASHFLOW.value)
print(f'Get by Context Class: {pks.shape}')
