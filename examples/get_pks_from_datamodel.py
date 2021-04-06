from pytechfin import Techfin, TOTVSRacAuth, TechfinDataModel
from pytechfin.enums import EnumApps

tf = Techfin()
dm = TechfinDataModel(tf)

r = dm.get_pks(dm_name='arinvoice', carol_tenant='tenant70827589d8a611eabbf10a586460272f',
               page_size=5000, techfin_app=EnumApps.CASHFLOW.value)

print(r)