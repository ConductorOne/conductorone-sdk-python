# RequestCatalogSearch
(*request_catalog_search*)

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
            'Cotton',
        ],
    ),
    app_display_name='Santa Savings siemens',
    entitlement_alias='male virtual',
    granted_status=shared.RequestCatalogSearchServiceSearchEntitlementsRequestGrantedStatus.GRANTED,
    include_deleted=False,
    page_size=8308.06,
    page_token='Gloves if EXE',
    query='intuitive UDP',
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

