from pycarol.carol import Carol
from pycarol.staging import Staging
from pycarol.data_models import DataModel

tenantName = 'tenant70827589d8a611eabbf10a586460272f'
env = 'carol.ai'
org = 'totvstechfin'
appName = 'techfinplatform'
connector_name = 'protheus_carol' 
 
try:
    login = Carol(tenantName, appName, environment=env, organization=org )
    stag  = Staging(login)
    print('Login success in Tenant: ' + login.get_current()['env_name'])
except Exception as e: 
    print(e)

#GOLDEN POR DATAMODEL
max_workers=30  
col = None
max_hits= None 

return_metadata = True
merge_records = True

dm  = DataModel(login)

cds = dm.fetch_parquet(
    dm_name='arinvoice', max_workers=max_workers, columns=col, merge_records=merge_records, 
    return_metadata=return_metadata, max_hits=max_hits)

print(cds)