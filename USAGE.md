<!-- Start SDK Example Usage -->


```python
import sdk
from sdk.models import shared

s = sdk.SdkWithCredentials("CLIENT_ID", "CLIENT_SECRET")

req = shared.AppEntitlementSearchServiceSearchRequest(
    page_size=100,
)

res = s.app_entitlement_search.search(req)

if res.app_entitlement_search_service_search_response is not None:
    # For more decoding options, see `https://pypi.org/project/dataclasses-json/`
    res = res.app_entitlement_search_service_search_response.to_dict()
```
<!-- End SDK Example Usage -->