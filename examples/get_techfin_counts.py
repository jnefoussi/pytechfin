from pytechfin import Techfin, TOTVSRacAuth, CarolSyncMonitoring
from pytechfin.enums import EnumApps


tf = Techfin()
csm = CarolSyncMonitoring(tf)


r = csm.get_table_record_count(carol_tenant='tenant70827589d8a611eabbf10a586460272f', techfin_app=EnumApps.CASHFLOW.value)

print(r)