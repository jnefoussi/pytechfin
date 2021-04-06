from pytechfin.techfin import Techfin
from pytechfin.auth import TOTVSRacAuth
from pytechfin.enums import EnumApps


tt = Techfin()

r = tt.call_api(path="provisioner/api/v1/provisioning", techfin_app=EnumApps.CASHFLOW.value, method='GET')
print(r)

# To use inline credentials instead of .env variables
cred = {
   "client_id": "123",
   "client_secret": "123",
}

auth = TOTVSRacAuth(**cred)
tt = Techfin(auth)
r = tt.call_api(path="provisioner/api/v1/provisioning", techfin_app=EnumApps.CASHFLOW.value, method='GET')
print(r)