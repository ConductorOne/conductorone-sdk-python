<!-- Start SDK Example Usage -->


```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIAppV1AppEntitlementOwnersAddRequest(
    add_app_entitlement_owner_request=shared.AddAppEntitlementOwnerRequest(),
    app_id='string',
    entitlement_id='string',
)

res = s.app_entitlement_owners.add(req)

if res.add_app_entitlement_owner_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->