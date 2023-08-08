"""
ConductorOne SDK for Python
=====

How to authenticate requests
----------------------------
You need to `obtain an API key from ConductorOne <https://conductor-one.stoplight.io/docs/conductorone-api/a76uioi122862-how-to-authenticate-requests>`_.
Then, you can use the following code snippet to instantiate the SDK with your credentials:
The docstring examples assume that our SDK is imported as ``sdk``:
  >>> import sdk
  >>> s = sdk.SDKWithCredentials(client_id, client_secret)

API Documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and our `API documentation page <https://conductor-one.stoplight.io/>`_.

"""

from .sdk import *
from .sdkconfiguration import *
from .sdkwithcredentials import *