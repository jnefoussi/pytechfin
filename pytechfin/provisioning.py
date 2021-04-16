from pytechfin.enums import EnumApps


class Provisioning: 

    def __init__(self, techfin):
        self.techfin = techfin

    def get_techfin_app_tenants(self, techfin_app,):
            """Get all tenants information by techfin_app

            Args:
                techfin_app (str): techfin app name.

            Returns:
                list of dict: techfin tenants information .
            """

            if not EnumApps.exists_value(techfin_app):
                raise ValueError(
                    f'techfin_app invalid. Value used" {techfin_app}. Check pytechfin.enums.EnumApps')

            r = self.techfin.call_api(path=f'provisioner/api/v1/provisioning', method='GET', techfin_app=techfin_app)
            
            return r
