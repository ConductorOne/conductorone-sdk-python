# app_entitlement_search

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
        oauth="",
    ),
)

req = shared.AppEntitlementSearchServiceSearchRequest(
    app_entitlement_expand_mask=shared.AppEntitlementExpandMask(
        paths=[
            'sapiente',
            'quo',
            'odit',
            'at',
        ],
    ),
    access_review_id='at',
    alias='maiores',
    app_ids=[
        'quod',
        'quod',
    ],
    app_user_ids=[
        'totam',
        'porro',
    ],
    compliance_framework_ids=[
        'dicta',
        'nam',
        'officia',
    ],
    exclude_app_ids=[
        'fugit',
        'deleniti',
        'hic',
    ],
    exclude_app_user_ids=[
        'totam',
        'beatae',
        'commodi',
        'molestiae',
    ],
    only_get_expiring=False,
    page_size=2645.55,
    page_token='qui',
    query='impedit',
    resource_type_ids=[
        'esse',
        'ipsum',
        'excepturi',
    ],
    risk_level_ids=[
        'perferendis',
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

