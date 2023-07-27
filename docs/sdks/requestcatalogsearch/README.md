# request_catalog_search

### Available Operations

* [search_entitlements](#search_entitlements) - Search Entitlements

## search_entitlements

Search request catalogs based on filters specified in the request body.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = shared.RequestCatalogSearchServiceSearchEntitlementsRequest(
    app_entitlement_expand_mask=shared.AppEntitlementExpandMask(
        paths=[
            'esse',
            'nemo',
            'reprehenderit',
        ],
    ),
    app_display_name='est',
    entitlement_alias='quis',
    granted_status=shared.RequestCatalogSearchServiceSearchEntitlementsRequestGrantedStatus.GRANTED,
    page_size=8806.79,
    page_token='impedit',
    query='hic',
)

res = s.request_catalog_search.search_entitlements(req)

if res.request_catalog_search_service_search_entitlements_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [shared.RequestCatalogSearchServiceSearchEntitlementsRequest](../../models/shared/requestcatalogsearchservicesearchentitlementsrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.C1APIRequestcatalogV1RequestCatalogSearchServiceSearchEntitlementsResponse](../../models/operations/c1apirequestcatalogv1requestcatalogsearchservicesearchentitlementsresponse.md)**

