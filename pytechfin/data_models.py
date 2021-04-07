from .misc import get_tenant_techfin
from .enums import EnumApps


class TechfinDataModel:

    def __init__(self, techfin):
        self.techfin = techfin

    def get_pks(self, dm_name, techfin_app, techfin_tenant=None, carol_tenant=None, page_size=1000, page=1, debug=False):
        """Get PKs from a data model

        Args:
            dm_name (str): Data model name
            techfin_app (str): techfin app name.
            techfin_tenant (str, optional): techfin tenant id. Defaults to None.
            carol_tenant (str, optional): carol tenant name. Defaults to Nonte.
            page_size (int, optional): number of records to get in each interation. Defaults to 1000.
            page (int, optional): initial page to start to fetch the records.. Defaults to 1.

        Returns:
            list: List of PKs
        """

        if (techfin_tenant is None and carol_tenant is None):
            techfin_tenant = self.techfin.techfin_tenant

        if not EnumApps.exists_value(techfin_app):
            raise ValueError(f'techfin_app invalid. Value used" {techfin_app}. Check pytechfin.enums.EnumApps')

        techfin_tenant_id = get_tenant_techfin(
            techfin_tenant=techfin_tenant, carol_tenant=carol_tenant)

        total_data = []
        params = {
            "dataModel":  dm_name,
            "page": 1,
            "pageSize": page_size
        }

        while True:
            data = self.techfin.call_api(path=f"provisioner/api/v1/carol-sync-monitoring/{techfin_tenant_id}/ids",
                                         techfin_app=techfin_app, method='GET', params=params, )
            if(len(data) == 0):
                break

            total_data.extend(data)
            params['page'] += 1

            if debug:
                # TODO: use loggers?
                print("total loaded: ", len(total_data), " &page=" +
                      str(page) + " &pageSize=" + str(page_size))

            total_data = [d.replace('-', '') for d in total_data]

        return total_data

    def get_table_record_count(self, techfin_app, techfin_tenant=None, carol_tenant=None):
        """Get number of records per table in techfin

        Args:
            techfin_app (str): techfin app name.
            techfin_tenant (str, optional): techfin tenant id. Defaults to None.
            carol_tenant (str, optional): carol tenant name. Defaults to Nonte.

        Returns:
            list of dict: counts per data model.
        """


        if not EnumApps.exists_value(techfin_app):
            raise ValueError(f'techfin_app invalid. Value used" {techfin_app}. Check pytechfin.enums.EnumApps')

        techfin_tenant_id = get_tenant_techfin(
            techfin_tenant=techfin_tenant, carol_tenant=carol_tenant)

        r = self.techfin.call_api(path=f'provisioner/api/v1/carol-sync-monitoring/{techfin_tenant_id}/table-record-count',
                                  method='GET', techfin_app=techfin_app)
        return r
