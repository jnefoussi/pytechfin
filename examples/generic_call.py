from pytechfin.techfin import Techfin
from pytechfin.auth import TOTVSRacAuth


cred = {
   "client_id": "123",
   "client_secret": "123",
}

auth = TOTVSRacAuth(**cred)

tt = Techfin(auth=auth)

r = tt.call_api(path="provisioner/api/v1/provisioning", method='GET')