import os
from .misc import get_tenant_name
from pycarol.carol import Carol
from pycarol.staging import Staging
from pycarol.auth.ApiKeyAuth import ApiKeyAuth
from pycarol.auth.PwdAuth import PwdAuth

class CarolContext():
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
            self.staging  = Staging(carol)
        except Exception as e: 
            print(e)
