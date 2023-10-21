# AppEntitlementSearch
(*app_entitlement_search*)

### Available Operations

* [search](#search) - Search

## search

Search app entitlements based on filters specified in the request body.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = shared.AppEntitlementSearchServiceSearchRequest(
    app_entitlement_expand_mask=shared.AppEntitlementExpandMask(
        paths=[
            'string',
        ],
    ),
    app_ids=[
        'string',
    ],
    app_user_ids=[
        'string',
    ],
    compliance_framework_ids=[
        'string',
    ],
    exclude_app_ids=[
        'string',
    ],
    exclude_app_user_ids=[
        'string',
    ],
    resource_type_ids=[
        'string',
    ],
    risk_level_ids=[
        'string',
    ],
)

res = s.app_entitlement_search.search(req)

if res.app_entitlement_search_service_search_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [shared.AppEntitlementSearchServiceSearchRequest](../../models/shared/appentitlementsearchservicesearchrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.C1APIAppV1AppEntitlementSearchServiceSearchResponse](../../models/operations/c1apiappv1appentitlementsearchservicesearchresponse.md)**

