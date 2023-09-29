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
            'transition',
        ],
    ),
    access_review_id='withdrawal Coordinator Ngultrum',
    alias='Russian Northeast yearningly',
    app_ids=[
        'Southeast',
    ],
    app_user_ids=[
        'Books',
    ],
    compliance_framework_ids=[
        'Other',
    ],
    exclude_app_ids=[
        'eligendi',
    ],
    exclude_app_user_ids=[
        'Tobago',
    ],
    include_deleted=False,
    only_get_expiring=False,
    page_size=7320.8,
    page_token='Arsenic Gasoline Oklahoma',
    query='opposite',
    resource_type_ids=[
        'Synchronised',
    ],
    risk_level_ids=[
        'huzzah',
    ],
)

res = s.app_entitlement_search.search(req)

if res.app_entitlement_search_service_search_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [shared.AppEntitlementSearchServiceSearchRequest](../../models/shared/appentitlementsearchservicesearchrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.C1APIAppV1AppEntitlementSearchServiceSearchResponse](../../models/operations/c1apiappv1appentitlementsearchservicesearchresponse.md)**

