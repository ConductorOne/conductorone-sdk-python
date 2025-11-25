# AppUser
(*app_user*)

## Overview

### Available Operations

* [list](#list) - List
* [list_app_user_credentials](#list_app_user_credentials) - List App User Credentials
* [list_app_users_for_user](#list_app_users_for_user) - List App Users For User
* [search](#search) - Search
* [update](#update) - Update

## list

Invokes the c1.api.app.v1.AppUserService.List method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppUserService.List" method="get" path="/api/v1/apps/{app_id}/app_users" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_user.list(request={
        "app_id": "<id>",
    })

    assert res.app_user_service_list_response is not None

    # Handle response
    print(res.app_user_service_list_response)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.C1APIAppV1AppUserServiceListRequest](../../models/operations/c1apiappv1appuserservicelistrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.C1APIAppV1AppUserServiceListResponse](../../models/operations/c1apiappv1appuserservicelistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_app_user_credentials

Invokes the c1.api.app.v1.AppUserService.ListAppUserCredentials method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppUserService.ListAppUserCredentials" method="get" path="/api/v1/apps/{app_id}/app_users/{app_user_id}/credentials" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_user.list_app_user_credentials(request={
        "app_id": "<id>",
        "app_user_id": "<id>",
    })

    assert res.app_user_service_list_credentials_response is not None

    # Handle response
    print(res.app_user_service_list_credentials_response)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.C1APIAppV1AppUserServiceListAppUserCredentialsRequest](../../models/operations/c1apiappv1appuserservicelistappusercredentialsrequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |

### Response

**[operations.C1APIAppV1AppUserServiceListAppUserCredentialsResponse](../../models/operations/c1apiappv1appuserservicelistappusercredentialsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_app_users_for_user

Invokes the c1.api.app.v1.AppUserService.ListAppUsersForUser method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppUserService.ListAppUsersForUser" method="get" path="/api/v1/apps/{app_id}/users/{user_id}/app_users" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_user.list_app_users_for_user(request={
        "app_id": "<id>",
        "user_id": "<id>",
    })

    assert res.app_users_for_user_service_list_response is not None

    # Handle response
    print(res.app_users_for_user_service_list_response)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.C1APIAppV1AppUserServiceListAppUsersForUserRequest](../../models/operations/c1apiappv1appuserservicelistappusersforuserrequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |

### Response

**[operations.C1APIAppV1AppUserServiceListAppUsersForUserResponse](../../models/operations/c1apiappv1appuserservicelistappusersforuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## search

Search app users based on filters specified in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppUserService.Search" method="post" path="/api/v1/search/app_users" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_user.search()

    assert res.app_user_service_search_response is not None

    # Handle response
    print(res.app_user_service_search_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.AppUserServiceSearchRequest](../../models/shared/appuserservicesearchrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.C1APIAppV1AppUserServiceSearchResponse](../../models/operations/c1apiappv1appuserservicesearchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Update an app user by ID. Only the fields specified in the update mask are updated.
 Currently, only the appUserType, and identityUserId fields can be updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppUserService.Update" method="post" path="/api/v1/apps/{app_user_app_id}/app_users/{app_user_id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_user.update(request={
        "app_user_app_id": "<id>",
        "app_user_id": "<id>",
    })

    assert res.app_user_service_update_response is not None

    # Handle response
    print(res.app_user_service_update_response)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.C1APIAppV1AppUserServiceUpdateRequest](../../models/operations/c1apiappv1appuserserviceupdaterequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.C1APIAppV1AppUserServiceUpdateResponse](../../models/operations/c1apiappv1appuserserviceupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |