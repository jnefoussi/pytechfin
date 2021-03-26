import os
from .misc import get_tenant_name
from pycarol.carol import Carol
from pycarol.staging import Staging
from pycarol.auth.PwdAuth import PwdAuth

class CarolContext():
    def __init__(self, use_production_context=False, 
            user=None, password=None, environment=None, organization=None, connector_name=None, app_name=None,  
            carol_tenant=None, techfin_tenant=None):
        
        if user is None or password is None:
            user = os.getenv('CAROLUSER')
            password = os.getenv('CAROLPWD')

        if user and password:
            auth = PwdAuth(user=user, password=password)
        else:
            raise ValueError("user and password must be set to `auth` method or pycarol env variables must be set.")

        if use_production_context:
            organization = 'totvstechfin'
            app_name = 'techfinplataform'

        if organization is None:
            organization = os.getenv('CAROLORGANIZATION')
            if organization is None:
                raise ValueError("`organization` must be set.")

        if app_name is None:
            app_name = os.getenv('CAROLAPPNAME', ' ')

        if carol_tenant is None:
            carol_tenant = get_tenant_name(techfin_tenant)

        if organization is None or app_name is None or auth is None:
            raise ValueError("organization, app_name and auth must be specified as parameters, either " +
                             "in the environment variables CAROLORGANIZATION, CAROLAPPNAME and CAROLUSER + CAROLPWD")

        self._environment = environment
        self._organization = organization
        self._connector_name = connector_name
        self._app_name = app_name
        self._carol_tenant = carol_tenant
        self._user = user
        self._password = password
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

    def _create_context(self):
        try:
            carol = Carol(self.carol_tenant, self.app_name, auth=PwdAuth(self.user, self.password), environment='carol.ai', organization=self.organization)
            
            print('Login success in Tenant: ' + carol.get_current()['env_name'])
            
            self.carol = carol
            self.staging  = Staging(carol)
        except Exception as e: 
            print(e)
