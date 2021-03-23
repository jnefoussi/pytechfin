=======
pytechfin
=======


Initializing 
------------

.. code:: python

    from pytechfin import Techfin, TOTVSRacAuth

    cred = {
        "client_id": "123",
        "client_secret": "123",  }

    auth = TOTVSRacAuth(**cred)
    tf = Techfin(auth)


Good practice using token
-------------------------

Never write in plain text your credentials. One can use 
the environment variables

 1. ``TECHFINCLIENTID`` for the client ID
 2. ``TECHFINCLIENTSECRET`` for the client secret
 
 e.g., one can create a ``.env`` file like this:

.. code:: python

    TECHFINCLIENTID=123
    TECHFINCLIENTSECRET=1234

and then

.. code:: python

    from pytechfin import Techfin
    from dotenv import load_dotenv
    load_dotenv(".env") #this will import these env variables to your execution.
    tf = Techfin()