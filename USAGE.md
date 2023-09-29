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
    add_app_entitlement_owner_request=shared.AddAppEntitlementOwnerRequest(
        user_id='Small West',
    ),
    app_id='Officer impactful',
    entitlement_id='Developer portals editorialise',
)

res = s.app_entitlement_owners.add(req)

if res.add_app_entitlement_owner_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->