import os
from .misc import get_tenant_name
from pycarol import Carol, Staging, DataModel, Apps, CDSGolden, CDSStaging, Connectors
from pycarol.staging import Staging
from pycarol.auth.ApiKeyAuth import ApiKeyAuth
from pycarol.auth.PwdAuth import PwdAuth

CAROL_KNOWN_MODULES = {
    'datamodel' : DataModel,
    'staging' : Staging,
    'apps' : Apps,
    'CDSGolden' : CDSGolden,
    'CDSStaging' : CDSStaging,
    'connectors': Connectors

}

class CarolContext:
    """Carol context. This class will encapsulate all pycarol's modules needed. 

        Args:
            use_production_context (bool, optional): Use techfin production envs.. Defaults to False.
            user (str, optional): Carol's user name. Defaults to None.
            password (str, optional): Carol's password. Defaults to None.
            environment (str, optional): Carol's environment name. Defaults to None.
            organization (str, optional): Carol's organization. Defaults to None.
            connector_id (str, optional): Carol's connector Id. Defaults to None.
            connector_name (str, optional): Carol's connector name. Defaults to None.
            app_name (str, optional): Carol's app name. Defaults to None.
            carol_tenant (str, optional): Carol's tenant name. Defaults to None.
            techfin_tenant (str, optional): Techfin tenant Id. Defaults to None.


    """
    def __init__(self, use_production_context=False, 
            user=None, password=None, environment=None, organization=None, connector_id=None, connector_name=None, app_name=None,  
            carol_tenant=None, techfin_tenant=None):


        self._auth = None

        if user is None or password is None:
            user = os.getenv('CAROLUSER')
            password = os.getenv('CAROLPWD')

            if user and password:
                self._auth = PwdAuth(user, password)
            else:
                auth_token = os.getenv('CAROLAPPOAUTH')
                connector_id = os.getenv('CAROLCONNECTORID')
                self._auth = ApiKeyAuth(auth_token)
            if self._auth is None:
                raise ValueError("either `auth` method or pycarol env variables must be set.")
        else:
            self._auth = PwdAuth(user, password)
         
        if carol_tenant is None:
            carol_tenant = get_tenant_name(techfin_tenant)

        if use_production_context:
            organization = 'totvstechfin'
            app_name = 'techfinplataform'

        self._environment = environment
        self._organization = organization
        self._connector_name = connector_name
        self._app_name = app_name
        self._carol_tenant = carol_tenant
        self._user = user
        self._password = password
        self._connector_id = connector_id
        self._context = self._create_context()
        self._all_modules = set()
        
    @property
    def environment(self):
        return self._environment

    @property
    def organization(self):
        return self._organization

    @property
    def connector_name(self):
        return self._connector_name

    @property
    def app_name(self):
        return self._app_name

    @property
    def carol_tenant(self):
        return self._carol_tenant

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @property
    def connector_id(self):
        return self._connector_id

    @property
    def auth(self):
        return self._auth

    def _create_context(self):
        try:
            carol = Carol(self.carol_tenant, self.app_name, auth=self.auth, 
                    environment='carol.ai', organization=self.organization, connector_id=self.connector_id)
            
            print('Login success in Tenant: ' + carol.get_current()['env_name'])
            
            self.carol = carol
        except Exception as e: 
            print(e)
            return

        for module_name, module in CAROL_KNOWN_MODULES.items():
            self.add_module(module_name, module)
            



    def add_module(self, module_name, module):
        """Adds module to context

        Args:
            module_name (str): attribute to be created
            module (pyCarol modude): the module will be inicialized with the pycarol.Carol instance.
        """
        setattr(self, module_name, module(self.carol))
        self._all_modules.update([module_name])

