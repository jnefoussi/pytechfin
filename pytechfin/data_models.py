from .misc import get_tenant_id

class TechfinDataModel:

    def __init__(self, techfin):
        self.techfin = techfin

    def get_pks(self, dm_name, techfin_tenant=None, carol_tenant=None, page_size=1000, page=1, debug=False):
        """Get PKs from a data model

        Args:
            dm_name (str): Data model name
            techfin_tenant (str, optional): techfin tenant id. Defaults to None.
            carol_tenant (str, optional): carol tenant name. Defaults to Nonte.
            page_size (int, optional): number of records to get in each interation. Defaults to 1000.
            page (int, optional): initial page to start to fetch the records.. Defaults to 1.

        Returns:
            lsit: List of PKs
        """

        techfin_tenant_id =  get_tenant_id(techfin_tenant=techfin_tenant, carol_tenant=carol_tenant)

        total_data = []
        params = {
            "dataModel":  dm_name,
            "page": 1,
            "pageSize": page_size
            }

        while True:
            data = self.techfin.call_api(path=f"provisioner/api/v1/carol-sync-monitoring/{techfin_tenant_id}/ids", techfin_app='cashflow' ,method='GET', params=params, )
            if(len(data) == 0):
                break

            total_data.extend(data)
            params['page'] +=1

            if debug:
                #TODO: use loggers?
                print("total loaded: ", len(total_data)," &page=" + str(page) + " &pageSize=" + str(page_size) )


            total_data = [d.replace('-', '') for d in total_data]

        return total_data
