from pytechfin import Techfin
from pytechfin.enums import EnumApps

tf = Techfin()
cashflow = tf.provisioning.get_techfin_app_tenants(EnumApps.CASHFLOW.value)
print(cashflow)

fmscash = tf.provisioning.get_techfin_app_tenants(EnumApps.FMSCASH.value)
print(fmscash)

