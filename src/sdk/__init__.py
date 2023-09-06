"""
ConductorOne SDK for Python
=====

How to authenticate requests
----------------------------
You need to obtain an API key from ConductorOne `<https://conductor-one.stoplight.io/docs/conductorone-api/a76uioi122862-how-to-authenticate-requests>`.
Then, you can use the following code snippet to instantiate the SDK with your credentials:
  >>> import sdk
  >>> s = sdk.SdkWithCredentials(client_id, client_secret)

API Documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and our API documentation page `<https://conductor-one.stoplight.io/>`.

"""

from .sdk import *
from .sdkconfiguration import *
from .sdkwithcredentials import *