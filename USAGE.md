<!-- Start SDK Example Usage [usage] -->
```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = shared.CreateAppRequest(
    owners=[
        'string',
    ],
)

res = s.apps.create(req)

if res.create_app_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->