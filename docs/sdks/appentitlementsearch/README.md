# AppEntitlementSearch
(*app_entitlement_search*)

## Overview

### Available Operations

* [search](#search) - Search
* [search_app_entitlements_for_app_user](#search_app_entitlements_for_app_user) - Search App Entitlements For App User
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## search_app_entitlements_for_app_user

Invokes the c1.api.app.v1.AppEntitlementSearchService.SearchAppEntitlementsForAppUser method.

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

res = s.app_entitlement_search.search_app_entitlements_for_app_user(request={
    "app_id": "<id>",
    "app_user_id": "<id>",
})

if res.list_app_entitlements_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                        | Type                                                                                                                                                                                             | Required                                                                                                                                                                                         | Description                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                        | [operations.C1APIAppV1AppEntitlementSearchServiceSearchAppEntitlementsForAppUserRequest](../../models/operations/c1apiappv1appentitlementsearchservicesearchappentitlementsforappuserrequest.md) | :heavy_check_mark:                                                                                                                                                                               | The request object to use for the request.                                                                                                                                                       |
| `retries`                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                              |

### Response

**[operations.C1APIAppV1AppEntitlementSearchServiceSearchAppEntitlementsForAppUserResponse](../../models/operations/c1apiappv1appentitlementsearchservicesearchappentitlementsforappuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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
    "app_entitlement_id": "<id>",
    "app_id": "<id>",
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |