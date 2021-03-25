from pytechfin import Techfin, TOTVSRacAuth, TechfinDataModel
from pytechfin.enums import EnumApps


tf = Techfin()
dm = TechfinDataModel(tf)


r = dm.get_table_record_count( carol_tenant='tenant54b78fbb913d11eab6e00a5864613d5f', techfin_app=EnumApps.CASHFLOW.value)

print(r)