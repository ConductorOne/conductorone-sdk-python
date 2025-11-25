# AppEntitlements
(*app_entitlements*)

## Overview

### Available Operations

* [add_automation_exclusion](#add_automation_exclusion) - Add Automation Exclusion
* [add_manually_managed_members](#add_manually_managed_members) - Add Manually Managed Members
* [create](#create) - Create
* [create_automation](#create_automation) - Create Automation
* [delete](#delete) - Delete
* [delete_automation](#delete_automation) - Delete Automation
* [get](#get) - Get
* [get_automation](#get_automation) - Get Automation
* [list](#list) - List
* [list_automation_exclusions](#list_automation_exclusions) - List Automation Exclusions
* [list_for_app_resource](#list_for_app_resource) - List For App Resource
* [list_for_app_user](#list_for_app_user) - List For App User
* [~~list_users~~](#list_users) - List Users :warning: **Deprecated**
* [remove_automation_exclusion](#remove_automation_exclusion) - Remove Automation Exclusion
* [remove_entitlement_membership](#remove_entitlement_membership) - Remove Entitlement Membership
* [update](#update) - Update
* [update_automation](#update_automation) - Update Automation

## add_automation_exclusion

Invokes the c1.api.app.v1.AppEntitlements.AddAutomationExclusion method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.AddAutomationExclusion" method="post" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/automation/exclusions" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.add_automation_exclusion(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
    })

    assert res.add_automation_exclusion_response is not None

    # Handle response
    print(res.add_automation_exclusion_response)

```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                              | [operations.C1APIAppV1AppEntitlementsAddAutomationExclusionRequest](../../models/operations/c1apiappv1appentitlementsaddautomationexclusionrequest.md) | :heavy_check_mark:                                                                                                                                     | The request object to use for the request.                                                                                                             |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |

### Response

**[operations.C1APIAppV1AppEntitlementsAddAutomationExclusionResponse](../../models/operations/c1apiappv1appentitlementsaddautomationexclusionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## add_manually_managed_members

Invokes the c1.api.app.v1.AppEntitlements.AddManuallyManagedMembers method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.AddManuallyManagedMembers" method="post" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/add-manual-user" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.add_manually_managed_members(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
    })

    assert res.manually_managed_users_response is not None

    # Handle response
    print(res.manually_managed_users_response)

```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.C1APIAppV1AppEntitlementsAddManuallyManagedMembersRequest](../../models/operations/c1apiappv1appentitlementsaddmanuallymanagedmembersrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |
| `retries`                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                             | :heavy_minus_sign:                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                          |

### Response

**[operations.C1APIAppV1AppEntitlementsAddManuallyManagedMembersResponse](../../models/operations/c1apiappv1appentitlementsaddmanuallymanagedmembersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

Invokes the c1.api.app.v1.AppEntitlements.Create method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.Create" method="post" path="/api/v1/apps/{app_id}/entitlements" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.create(request={
        "app_id": "<id>",
    })

    assert res.create_app_entitlement_response is not None

    # Handle response
    print(res.create_app_entitlement_response)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.C1APIAppV1AppEntitlementsCreateRequest](../../models/operations/c1apiappv1appentitlementscreaterequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[operations.C1APIAppV1AppEntitlementsCreateResponse](../../models/operations/c1apiappv1appentitlementscreateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_automation

Invokes the c1.api.app.v1.AppEntitlements.CreateAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.CreateAutomation" method="post" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/automation/create" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.create_automation(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
    })

    assert res.create_automation_response is not None

    # Handle response
    print(res.create_automation_response)

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.C1APIAppV1AppEntitlementsCreateAutomationRequest](../../models/operations/c1apiappv1appentitlementscreateautomationrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |

### Response

**[operations.C1APIAppV1AppEntitlementsCreateAutomationResponse](../../models/operations/c1apiappv1appentitlementscreateautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Invokes the c1.api.app.v1.AppEntitlements.Delete method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.Delete" method="delete" path="/api/v1/apps/{app_id}/entitlements/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.delete(request={
        "app_id": "<id>",
        "id": "<id>",
    })

    assert res.delete_app_entitlement_response is not None

    # Handle response
    print(res.delete_app_entitlement_response)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.C1APIAppV1AppEntitlementsDeleteRequest](../../models/operations/c1apiappv1appentitlementsdeleterequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[operations.C1APIAppV1AppEntitlementsDeleteResponse](../../models/operations/c1apiappv1appentitlementsdeleteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_automation

Invokes the c1.api.app.v1.AppEntitlements.DeleteAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.DeleteAutomation" method="delete" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/automation" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.delete_automation(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
    })

    assert res.delete_automation_response is not None

    # Handle response
    print(res.delete_automation_response)

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.C1APIAppV1AppEntitlementsDeleteAutomationRequest](../../models/operations/c1apiappv1appentitlementsdeleteautomationrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |

### Response

**[operations.C1APIAppV1AppEntitlementsDeleteAutomationResponse](../../models/operations/c1apiappv1appentitlementsdeleteautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Get an app entitlement by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.Get" method="get" path="/api/v1/apps/{app_id}/entitlements/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.get(request={
        "app_id": "<id>",
        "id": "<id>",
    })

    assert res.get_app_entitlement_response is not None

    # Handle response
    print(res.get_app_entitlement_response)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.C1APIAppV1AppEntitlementsGetRequest](../../models/operations/c1apiappv1appentitlementsgetrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.C1APIAppV1AppEntitlementsGetResponse](../../models/operations/c1apiappv1appentitlementsgetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_automation

Invokes the c1.api.app.v1.AppEntitlements.GetAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.GetAutomation" method="get" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/automation" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.get_automation(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
    })

    assert res.app_entitlement_service_get_automation_response is not None

    # Handle response
    print(res.app_entitlement_service_get_automation_response)

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.C1APIAppV1AppEntitlementsGetAutomationRequest](../../models/operations/c1apiappv1appentitlementsgetautomationrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `retries`                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                     | :heavy_minus_sign:                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                  |

### Response

**[operations.C1APIAppV1AppEntitlementsGetAutomationResponse](../../models/operations/c1apiappv1appentitlementsgetautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

List app entitlements associated with an app.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.List" method="get" path="/api/v1/apps/{app_id}/entitlements" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.list(request={
        "app_id": "<id>",
    })

    assert res.list_app_entitlements_response is not None

    # Handle response
    print(res.list_app_entitlements_response)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.C1APIAppV1AppEntitlementsListRequest](../../models/operations/c1apiappv1appentitlementslistrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.C1APIAppV1AppEntitlementsListResponse](../../models/operations/c1apiappv1appentitlementslistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_automation_exclusions

Invokes the c1.api.app.v1.AppEntitlements.ListAutomationExclusions method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.ListAutomationExclusions" method="get" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/automation/exclusions" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.list_automation_exclusions(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
    })

    assert res.list_automation_exclusions_response is not None

    # Handle response
    print(res.list_automation_exclusions_response)

```

### Parameters

| Parameter                                                                                                                                                  | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                  | [operations.C1APIAppV1AppEntitlementsListAutomationExclusionsRequest](../../models/operations/c1apiappv1appentitlementslistautomationexclusionsrequest.md) | :heavy_check_mark:                                                                                                                                         | The request object to use for the request.                                                                                                                 |
| `retries`                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                           | :heavy_minus_sign:                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                        |

### Response

**[operations.C1APIAppV1AppEntitlementsListAutomationExclusionsResponse](../../models/operations/c1apiappv1appentitlementslistautomationexclusionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_for_app_resource

List app entitlements associated with an app resource.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.ListForAppResource" method="get" path="/api/v1/apps/{app_id}/entitlements/resource_types/{app_resource_type_id}/resources/{app_resource_id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.list_for_app_resource(request={
        "app_id": "<id>",
        "app_resource_id": "<id>",
        "app_resource_type_id": "<id>",
    })

    assert res.list_app_entitlements_response is not None

    # Handle response
    print(res.list_app_entitlements_response)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.C1APIAppV1AppEntitlementsListForAppResourceRequest](../../models/operations/c1apiappv1appentitlementslistforappresourcerequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |

### Response

**[operations.C1APIAppV1AppEntitlementsListForAppResourceResponse](../../models/operations/c1apiappv1appentitlementslistforappresourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_for_app_user

List app entitlements associated with an app user.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.ListForAppUser" method="get" path="/api/v1/apps/{app_id}/entitlements/users/{app_user_id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.list_for_app_user(request={
        "app_id": "<id>",
        "app_user_id": "<id>",
    })

    assert res.list_app_entitlements_response is not None

    # Handle response
    print(res.list_app_entitlements_response)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.C1APIAppV1AppEntitlementsListForAppUserRequest](../../models/operations/c1apiappv1appentitlementslistforappuserrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[operations.C1APIAppV1AppEntitlementsListForAppUserResponse](../../models/operations/c1apiappv1appentitlementslistforappuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## ~~list_users~~

List the users, as AppEntitlementUsers objects, of an app entitlement.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.ListUsers" method="get" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/users" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.list_users(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
    })

    assert res.list_app_entitlement_users_response is not None

    # Handle response
    print(res.list_app_entitlement_users_response)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.C1APIAppV1AppEntitlementsListUsersRequest](../../models/operations/c1apiappv1appentitlementslistusersrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.C1APIAppV1AppEntitlementsListUsersResponse](../../models/operations/c1apiappv1appentitlementslistusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_automation_exclusion

Invokes the c1.api.app.v1.AppEntitlements.RemoveAutomationExclusion method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.RemoveAutomationExclusion" method="delete" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/automation/exclusions" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.remove_automation_exclusion(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
    })

    assert res.remove_automation_exclusion_response is not None

    # Handle response
    print(res.remove_automation_exclusion_response)

```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.C1APIAppV1AppEntitlementsRemoveAutomationExclusionRequest](../../models/operations/c1apiappv1appentitlementsremoveautomationexclusionrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |
| `retries`                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                             | :heavy_minus_sign:                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                          |

### Response

**[operations.C1APIAppV1AppEntitlementsRemoveAutomationExclusionResponse](../../models/operations/c1apiappv1appentitlementsremoveautomationexclusionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_entitlement_membership

Invokes the c1.api.app.v1.AppEntitlements.RemoveEntitlementMembership method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.RemoveEntitlementMembership" method="delete" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/remove-membership" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.remove_entitlement_membership(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
    })

    assert res.remove_entitlement_membership_response is not None

    # Handle response
    print(res.remove_entitlement_membership_response)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                        | [operations.C1APIAppV1AppEntitlementsRemoveEntitlementMembershipRequest](../../models/operations/c1apiappv1appentitlementsremoveentitlementmembershiprequest.md) | :heavy_check_mark:                                                                                                                                               | The request object to use for the request.                                                                                                                       |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |

### Response

**[operations.C1APIAppV1AppEntitlementsRemoveEntitlementMembershipResponse](../../models/operations/c1apiappv1appentitlementsremoveentitlementmembershipresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Update an app entitlement by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.Update" method="post" path="/api/v1/apps/{app_id}/entitlements/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import operations, shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.update(request=operations.C1APIAppV1AppEntitlementsUpdateRequest(
        app_id="<id>",
        id="<id>",
    ))

    assert res.update_app_entitlement_response is not None

    # Handle response
    print(res.update_app_entitlement_response)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.C1APIAppV1AppEntitlementsUpdateRequest](../../models/operations/c1apiappv1appentitlementsupdaterequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[operations.C1APIAppV1AppEntitlementsUpdateResponse](../../models/operations/c1apiappv1appentitlementsupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_automation

Invokes the c1.api.app.v1.AppEntitlements.UpdateAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlements.UpdateAutomation" method="post" path="/api/v1/apps/{app_id}/entitlements/{app_entitlement_id}/automation/update" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlements.update_automation(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
    })

    assert res.app_entitlement_service_update_automation_response is not None

    # Handle response
    print(res.app_entitlement_service_update_automation_response)

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.C1APIAppV1AppEntitlementsUpdateAutomationRequest](../../models/operations/c1apiappv1appentitlementsupdateautomationrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |

### Response

**[operations.C1APIAppV1AppEntitlementsUpdateAutomationResponse](../../models/operations/c1apiappv1appentitlementsupdateautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |