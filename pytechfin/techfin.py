import json
import os
import copy
import os.path
from . import __version__
from .exceptions import TechfinApiResponseException, InvalidToken
from .http import _retry_session


class Techfin:
    """
    This class handle all Techfin`s API calls It will handle all API calls,
    for a given authentication method. :param domain: `str`.

    Args:

        domain: `str`. default `None`.
            Tenant name. e.x., domain.carol.ai
        app_name: `str`. default `None`.
            Carol app name.
        auth: `PwdAuth` or `ApiKeyAuth`.
            object Auth Carol object to handle authentication
        connector_id: `str` , default `__CONNECTOR_PYCAROL__`.
            Connector Id
        port: `int` , default 443.
            Port to be used (when running locally it could change)
        verbose: `bool` , default `False`.
            If True will print the header, method and URL of each API call.
        organization: `str` , default `None`.
            Organization domain.
        environment: `str`, default `carol.ai`,
            Which Carol's environment to use. There are three possible values today.

                1. 'carol.ai' for the production environment
                2. 'karol.ai' for the explore environment
                3. 'qarol.ai' for the QA environment

        host: `str` default `None`
            This will overwrite the host used. Today the host is:

                1. if organization is None, host={domain}.{environment}
                2. else host={organization}.{environment}

            See Carol._set_host.

    OBS:
        In case all parameters are `None`, pycarol will try yo find their values in the environment variables.
        The values are:

             1. `CAROLTENANT` for domain
             2. `CAROLAPPNAME` for app_name
             3. `CAROLAPPOAUTH` for auth
             4. `CAROLORGANIZATION` for organization
             5. `CAROLCONNECTORID` for connector_id
             6. `CAROL_DOMAIN` for environment
             7. `CAROLUSER` for carol user email
             8. `CAROLPWD` for user password.


    """

    def __init__(self, auth=None, port=443, host=None):

        if auth is None:
            client_id = os.getenv('TECHFINCLIENTID')
            client_secret = os.getenv('TECHFINCLIENTSECRET')

            auth = ClientAuth(client_id=client_id, client_secret=client_secret)

        self.port = port
        self.host = host or 'totvs.app'
        self.auth = auth
        self.auth.login(self)


    def call_api(self, path, techfin_app, method=None, data=None, auth=True, params=None, content_type='application/json', retries=8,
                 session=None, backoff_factor=0.5, status_forcelist=(502, 503, 504, 524), downloadable=False,
                 method_whitelist=frozenset(['HEAD', 'TRACE', 'GET', 'PUT', 'OPTIONS', 'DELETE', 'POST']), errors='raise',
                 extra_headers=None, files=None,
                 **kwds):
        """
        This method handles all the API calls.

        Args:

            path: `str`.
                API URI path. e.x.  v2/staging/schema
            method: 'str', default `None`.
                Set of uppercased HTTP method verbs that we should call on.
            data: 'dict`, default `None`.
                Dictionary, list of tuples, bytes, or file-like object to send in
                the body of the request.
            auth: :class: `pycarol.ApiKeyAuth` or `pycarol.PwdAuth`
                Auth type to be used within the API's calls.
            params: (optional) Dictionary, list of tuples or bytes to send
                     in the query string for the :class:`requests.Request`.
            content_type: `str`, default 'application/json'
                Content type for the api call
            retries: `int` , default `5`
                Number of retries for the API calls
            session: :class `requests.Session` object dealt `None`
                It allows you to persist certain parameters across requests.
            backoff_factor: `float` , default `0.5`
                Backoff factor to apply between  attempts. It will sleep for:
                        {backoff factor} * (2 ^ ({retries} - 1)) seconds
            status_forcelist: `iterable` , default (500, 502, 503, 504, 524).
                A set of integer HTTP status codes that we should force a retry on.
                A retry is initiated if the request method is in method_whitelist and the response status code is in
                status_forcelist.
            downloadable: `bool` default `False`.
                If the request will return a file to download.
            method_whitelist: `iterable` , default frozenset(['HEAD', 'TRACE', 'GET', 'PUT', 'OPTIONS', 'DELETE']))
                Set of uppercased HTTP method verbs that we should retry on.
            errors: {‘ignore’, ‘raise’}, default ‘raise’
                If ‘raise’, then invalid request will raise an exception If ‘ignore’,
                then invalid request will return the request response
            extra_headers: `dict` default `None`
                extra headers to be sent.
            files: `dict` default `None`
                Used when uploading files to carol. This will be sent to :class: `requests.request`
            kwds: `dict` default `None`
                Extra parameters to be sent to :class: `requests.request`

        Rerturn:
            Dict with API response.

        """

        extra_headers = extra_headers or {}
        url = f'https://{techfin_app}.{self.host}:{self.port}/{path}'

        if method is None:
            if data is None:
                method = 'GET'
            else:
                method = 'POST'

        met_list = ['HEAD', 'TRACE', 'GET', 'PUT', 'POST', 'OPTIONS', 'PATCH',
                    'DELETE', 'CONNECT']
        assert method in met_list, f"API method must be {met_list}"

        headers = {'accept': 'application/json'}
        if auth:
            self.auth.authenticate_request(headers)

        data_json = None
        if method == 'GET':
            pass

        elif (method == 'POST') or (method == 'DELETE') or (method == 'PUT'):
            if content_type is not None:
                headers['content-type'] = content_type

            if content_type == 'application/json':
                data_json = data
                data = None

        headers.update(extra_headers)
        headers.update({'User-Agent': f'techfin/{__version__}'})

        __count = 0
        while True:
            if session is None:
                session = _retry_session(retries=retries, session=session, backoff_factor=backoff_factor,
                                              status_forcelist=status_forcelist, method_whitelist=method_whitelist)

            response = session.request(method=method, url=url, data=data, json=data_json,
                                       headers=headers, params=params, files=files, **kwds)

            if response.ok or errors == 'ignore':
                if downloadable:
                    return response

                response.encoding = 'utf-8'
                self.response = response
                if response.text == '':
                    return {}
                return json.loads(response.text)

            elif ("invalid_client" in response.text):

                # TODO: Need to check the error when token expires.
                # self.auth.get_access_token()  # It will refresh token if Unauthorized
                # __count += 1
                # if __count < 5:  # To avoid infinity loops
                #     continue
                # else:
                #     raise TechfinApiResponseException(
                #         'Too many retries to refresh token.\n', response.text, response.status_code)

                raise TechfinApiResponseException("wrong cliend_id/client_secret",
                 response.text, response.status_code)

            else:
                TechfinApiResponseException(response.text, response.status_code)

        


