# AppEntitlementUserBinding
(*app_entitlement_user_binding*)

## Overview

### Available Operations

* [list_app_users_for_identity_with_grant](#list_app_users_for_identity_with_grant) - List App Users For Identity With Grant
* [remove_grant_duration](#remove_grant_duration) - Remove Grant Duration
* [search_grant_feed](#search_grant_feed) - Search Grant Feed
* [search_past_grants](#search_past_grants) - Search Past Grants
* [update_grant_duration](#update_grant_duration) - Update Grant Duration

## list_app_users_for_identity_with_grant

Returns a list of app users for the identity in the app. If that app user also has a grant to the entitlement from the request, data about the grant is also returned. It will always return ALL app users for this identity, but only SOME may have grant data.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementUserBindingService.ListAppUsersForIdentityWithGrant" method="get" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/users/{identity_user_id}/grants" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlement_user_binding.list_app_users_for_identity_with_grant(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
        "identity_user_id": "<id>",
    })

    assert res.list_app_users_for_identity_with_grant_response is not None

    # Handle response
    print(res.list_app_users_for_identity_with_grant_response)

```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                    | [operations.C1APIAppV1AppEntitlementUserBindingServiceListAppUsersForIdentityWithGrantRequest](../../models/operations/c1apiappv1appentitlementuserbindingservicelistappusersforidentitywithgrantrequest.md) | :heavy_check_mark:                                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                          |

### Response

**[operations.C1APIAppV1AppEntitlementUserBindingServiceListAppUsersForIdentityWithGrantResponse](../../models/operations/c1apiappv1appentitlementuserbindingservicelistappusersforidentitywithgrantresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_grant_duration

Invokes the c1.api.app.v1.AppEntitlementUserBindingService.RemoveGrantDuration method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementUserBindingService.RemoveGrantDuration" method="post" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/users/{app_user_id}/remove-grant-duration" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlement_user_binding.remove_grant_duration(request={
        "remove_grant_duration_request": {},
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
        "app_user_id": "<id>",
    })

    assert res.remove_grant_duration_response is not None

    # Handle response
    print(res.remove_grant_duration_response)

```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                          | [operations.C1APIAppV1AppEntitlementUserBindingServiceRemoveGrantDurationRequest](../../models/operations/c1apiappv1appentitlementuserbindingserviceremovegrantdurationrequest.md) | :heavy_check_mark:                                                                                                                                                                 | The request object to use for the request.                                                                                                                                         |
| `retries`                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                |

### Response

**[operations.C1APIAppV1AppEntitlementUserBindingServiceRemoveGrantDurationResponse](../../models/operations/c1apiappv1appentitlementuserbindingserviceremovegrantdurationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## search_grant_feed

Invokes the c1.api.app.v1.AppEntitlementUserBindingService.SearchGrantFeed method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementUserBindingService.SearchGrantFeed" method="post" path="/api/v1/grants/feed" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlement_user_binding.search_grant_feed(request={})

    assert res.search_grant_feed_response is not None

    # Handle response
    print(res.search_grant_feed_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.SearchGrantFeedRequest](../../models/shared/searchgrantfeedrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.C1APIAppV1AppEntitlementUserBindingServiceSearchGrantFeedResponse](../../models/operations/c1apiappv1appentitlementuserbindingservicesearchgrantfeedresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## search_past_grants

Invokes the c1.api.app.v1.AppEntitlementUserBindingService.SearchPastGrants method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementUserBindingService.SearchPastGrants" method="post" path="/api/v1/search/past-grants" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlement_user_binding.search_past_grants(request={})

    assert res.search_past_grants_response is not None

    # Handle response
    print(res.search_past_grants_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.SearchPastGrantsRequest](../../models/shared/searchpastgrantsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.C1APIAppV1AppEntitlementUserBindingServiceSearchPastGrantsResponse](../../models/operations/c1apiappv1appentitlementuserbindingservicesearchpastgrantsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_grant_duration

Invokes the c1.api.app.v1.AppEntitlementUserBindingService.UpdateGrantDuration method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementUserBindingService.UpdateGrantDuration" method="post" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/users/{app_user_id}/update-grant-duration" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlement_user_binding.update_grant_duration(request={
        "update_grant_duration_request": {},
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
        "app_user_id": "<id>",
    })

    assert res.update_grant_duration_response is not None

    # Handle response
    print(res.update_grant_duration_response)

```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                          | [operations.C1APIAppV1AppEntitlementUserBindingServiceUpdateGrantDurationRequest](../../models/operations/c1apiappv1appentitlementuserbindingserviceupdategrantdurationrequest.md) | :heavy_check_mark:                                                                                                                                                                 | The request object to use for the request.                                                                                                                                         |
| `retries`                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                |

### Response

**[operations.C1APIAppV1AppEntitlementUserBindingServiceUpdateGrantDurationResponse](../../models/operations/c1apiappv1appentitlementuserbindingserviceupdategrantdurationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |