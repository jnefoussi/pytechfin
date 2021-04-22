from .misc import *
from .techfin import Techfin
from .carol_techfin import CarolTechfin
from pycarol import CarolAPI

class Context():
    """Carol context. This class will encapsulate all context modules needed. 

        Args:
            use_production_context (bool, optional): Use techfin production envs.. Defaults to False.
            user (str, optional): Carol's user name. Defaults to None.
            password (str, optional): Carol's password. Defaults to None.
            environment (str, optional): Carol's environment name. Defaults to 'carol.ai'.
            organization (str, optional): Carol's organization. Defaults to None.
            connector_id (str, optional): Carol's connector Id. Defaults to None.
            app_name (str, optional): Carol's app name. Defaults to None.
            carol_tenant (str, optional): Carol's tenant name. Defaults to None.
            techfin_tenant (str, optional): Techfin tenant Id. Defaults to None.
            techfin_auth (TOTVSRacAuth, optional): TOTVS RAC Credentials. Defaults to None 
            techfin_port (int, optional): API URL port. Defaults to 443. 
            techfin_host (string, optional): API host address. Defaults to None or totvs.app (production).
    """
    def __init__(self, use_production_context=False, 
            user=None, password=None, auth=None, environment='carol.ai', organization=None, connector_id=None, app_name=None,  
            carol_tenant=None, techfin_tenant=None, techfin_auth=None, techfin_port=443, techfin_host=None):
        
        if carol_tenant is None:
            self._carol_tenant = get_tenant_name(techfin_tenant)
            self._techfin_tenant = techfin_tenant
        else:
            self._carol_tenant = carol_tenant
            self._techfin_tenant = get_tenant_techfin(carol_tenant, techfin_tenant)
    
        if use_production_context:
            organization = 'totvstechfin'
            app_name = 'techfinplataform'

        self._carol = CarolAPI(self._carol_tenant, app_name, auth=auth, user=user, password=password,
                    environment=environment, organization=organization, connector_id=connector_id)
        
        self._techfin = Techfin(auth=techfin_auth, port=techfin_port, host=techfin_host, techfin_tenant=self.techfin_tenant)

        self.carol.add_module('caroltechfin', CarolTechfin)
        
    @property
    def carol(self):
        return self._carol

    @property
    def techfin(self):
        return self._techfin

    @property
    def carol_tenant(self):
        return self._carol_tenant
    
    @property
    def techfin_tenant(self):
        return self._techfin_tenant
    
    @property
    def current(self):
        current_info = {}
        
        # Carol
        current_info['carol'] = self.carol.get_current()
        current_info['carol']['apps'] = self.carol.apps.all()

        # Techfin
        current_info['techfin'] = {'tenant_id': self.techfin_tenant}

        return current_info
