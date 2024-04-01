<!-- Start SDK Example Usage [usage] -->
```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = shared.CreateAppRequest()

res = s.apps.create(req)

if res.create_app_response is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->