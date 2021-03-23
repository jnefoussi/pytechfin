from pytechfin.techfin import Techfin
from pytechfin.auth import TOTVSRacAuth
from pytechfin.enums import Apps

cred = {
   "client_id": "123",
   "client_secret": "123",
}

auth = TOTVSRacAuth(**cred)

tt = Techfin(auth)

r = tt.call_api(path="provisioner/api/v1/provisioning", techfin_app=Apps.CASHFLOW.value, method='GET')
