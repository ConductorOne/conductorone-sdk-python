# AppEntitlementSearch
(*app_entitlement_search*)

### Available Operations

* [search](#search) - Search
* [search_app_entitlements_with_expired](#search_app_entitlements_with_expired) - Search App Entitlements With Expired

## search

Search app entitlements based on filters specified in the request body.

### Example Usage

```python
from sdk import SDK
from sdk.models import shared

s = SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.app_entitlement_search.search()

if res.app_entitlement_search_service_search_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [shared.AppEntitlementSearchServiceSearchRequest](../../models/shared/appentitlementsearchservicesearchrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |


### Response

**[operations.C1APIAppV1AppEntitlementSearchServiceSearchResponse](../../models/operations/c1apiappv1appentitlementsearchservicesearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## search_app_entitlements_with_expired

Search app entitlements, include app users, users, expires, discovered.

### Example Usage

```python
from sdk import SDK
from sdk.models import shared

s = SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.app_entitlement_search.search_app_entitlements_with_expired(request={
    "app_entitlement_id": "<value>",
    "app_id": "<value>",
})

if res.search_app_entitlements_with_expired_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                          | [operations.C1APIAppV1AppEntitlementSearchServiceSearchAppEntitlementsWithExpiredRequest](../../models/operations/c1apiappv1appentitlementsearchservicesearchappentitlementswithexpiredrequest.md) | :heavy_check_mark:                                                                                                                                                                                 | The request object to use for the request.                                                                                                                                                         |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |


### Response

**[operations.C1APIAppV1AppEntitlementSearchServiceSearchAppEntitlementsWithExpiredResponse](../../models/operations/c1apiappv1appentitlementsearchservicesearchappentitlementswithexpiredresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
