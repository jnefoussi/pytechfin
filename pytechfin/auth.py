"""
Standard User/Password Auth

"""

import types
import time


class TOTVSRacAuth:
    """

    Args:

        client_id: `str`
            client_id
        client_secret: `str`
            client_secret

    """

    def __init__(self, client_id, client_secret):
        self.client_secret = client_secret
        self.client_id = client_id
        self._token = None

    def _set_token(self, data):
        self._token = types.SimpleNamespace()
        self._token.access_token = data['access_token']
        self._token.expiration = time.time() - 60 + (data['expires_in'])

    def login(self, techfin):
        """

        Args:

            techfin: techfin.Techfin
                Techfin() instance.

        Returns:
            None

        """
        self.techfin = techfin

        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials',
            'scope': "authorization_api",
        }
        resp = self.techfin.call_api(
            path='totvs.rac/connect/token', techfin_app='totvs.rac',
            auth=False, data=data, method='POST',
            content_type='application/x-www-form-urlencoded'
            )

        self._set_token(resp)

    def authenticate_request(self, headers):
        headers['Authorization'] = "Bearer " + self.get_access_token()
        return headers

    def _is_token_expired(self):
        if self._token is None:
            return True

        if self._token.expiration == 0:
            return False

        now = time.time()
        # Adds 1 min buffer
        expiry = self._token.expiration - 60

        return now > expiry

    def get_access_token(self):
        if self._is_token_expired():
            self._refresh_token()

        return self._token.access_token

    def _refresh_token(self):

        # TODO: No refresh token from techfin. keep as placeholder.
        self.login()
