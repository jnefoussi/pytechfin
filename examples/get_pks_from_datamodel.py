from pytechfin import Techfin,  CarolSyncMonitoring
from pytechfin.enums import EnumApps

tf = Techfin()
csm = CarolSyncMonitoring(tf)

pks = csm.get_pks(dm_name='arinvoice', carol_tenant='tenant70827589d8a611eabbf10a586460272f',
               page_size=5000, techfin_app=EnumApps.CASHFLOW.value)

print(f'Get by CarolSyncMonitoring Class: {pks}')


# With Context Class

from pytechfin import Context
from pytechfin.enums import EnumApps

context = Context(use_production_context=True, carol_tenant='tenant70827589d8a611eabbf10a586460272f')
pks = context.techfin.carol_sync_monitoring.get_pks('arinvoice', page_size=5000, techfin_app=EnumApps.CASHFLOW.value)
print(f'Get by Context Class: {pks}')
