# RequestCatalogSearch

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
        bearer_auth="",
        oauth="",
    ),
)

req = shared.RequestCatalogSearchServiceSearchEntitlementsRequest(
    app_entitlement_expand_mask=shared.AppEntitlementExpandMask(
        paths=[
            'id',
        ],
    ),
    app_display_name='quis',
    entitlement_alias='reprehenderit',
    granted_status=shared.RequestCatalogSearchServiceSearchEntitlementsRequestGrantedStatus.GRANTED,
    include_deleted=False,
    page_size=764.86,
    page_token='corporis',
    query='quidem',
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

