from urllib3.util.retry import Retry
import requests
from requests.adapters import HTTPAdapter

def _retry_session(retries=5, session=None, backoff_factor=0.5, status_forcelist=(500, 502, 503, 504, 524),
                       allowed_methods=frozenset(['HEAD', 'TRACE', 'GET', 'PUT', 'OPTIONS', 'DELETE'])):
        """
        Static method used to handle retries between calls.

        Args:

            retries: `int` , default `5`
                Number of retries for the API calls
            session: Session object dealt `None`
                It allows you to persist certain parameters across requests.
            backoff_factor: `float` , default `0.5`
                Backoff factor to apply between  attempts. It will sleep for:
                        {backoff factor} * (2 ^ ({retries} - 1)) seconds
            status_forcelist: `iterable` , default (500, 502, 503, 504, 524).
                A set of integer HTTP status codes that we should force a retry on.
                A retry is initiated if the request method is in allowed_methods and the response status code is in
                status_forcelist.
            allowed_methods: `iterable` , default frozenset(['HEAD', 'TRACE', 'GET', 'PUT', 'OPTIONS', 'DELETE']))
                Set of uppercased HTTP method verbs that we should retry on.

        Returns:
            :class:`requests.Section`
        """

        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
            method_whitelist=allowed_methods,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session
