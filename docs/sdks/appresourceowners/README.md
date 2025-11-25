# AppResourceOwners
(*app_resource_owners*)

## Overview

### Available Operations

* [add](#add) - Add
* [delete](#delete) - Delete
* [list](#list) - List
* [list_owner_i_ds](#list_owner_i_ds) - List Owner I Ds
* [remove](#remove) - Remove
* [set](#set) - Set

## add

Invokes the c1.api.app.v1.AppResourceOwners.Add method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceOwners.Add" method="post" path="/api/v1/apps/{app_id}/resource_types/{resource_type_id}/resource/{resource_id}/owners" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_resource_owners.add(request={
        "app_id": "<id>",
        "resource_id": "<id>",
        "resource_type_id": "<id>",
    })

    assert res.add_app_resource_owner_response is not None

    # Handle response
    print(res.add_app_resource_owner_response)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.C1APIAppV1AppResourceOwnersAddRequest](../../models/operations/c1apiappv1appresourceownersaddrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.C1APIAppV1AppResourceOwnersAddResponse](../../models/operations/c1apiappv1appresourceownersaddresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Delete deletes the owners from a given app resource.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceOwners.Delete" method="delete" path="/api/v1/apps/{app_id}/resource_types/{resource_type_id}/resource/{resource_id}/ownerids" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_resource_owners.delete(request={
        "app_id": "<id>",
        "resource_id": "<id>",
        "resource_type_id": "<id>",
    })

    assert res.delete_app_resource_owners_response is not None

    # Handle response
    print(res.delete_app_resource_owners_response)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.C1APIAppV1AppResourceOwnersDeleteRequest](../../models/operations/c1apiappv1appresourceownersdeleterequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[operations.C1APIAppV1AppResourceOwnersDeleteResponse](../../models/operations/c1apiappv1appresourceownersdeleteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

List all owners of an app resource.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceOwners.List" method="get" path="/api/v1/apps/{app_id}/resource_types/{resource_type_id}/resource/{resource_id}/owners" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_resource_owners.list(request={
        "app_id": "<id>",
        "resource_id": "<id>",
        "resource_type_id": "<id>",
    })

    assert res.list_app_resource_owners_response is not None

    # Handle response
    print(res.list_app_resource_owners_response)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.C1APIAppV1AppResourceOwnersListRequest](../../models/operations/c1apiappv1appresourceownerslistrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[operations.C1APIAppV1AppResourceOwnersListResponse](../../models/operations/c1apiappv1appresourceownerslistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_owner_i_ds

ListOwnerIDs lists owner IDs for a given app resource.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceOwners.ListOwnerIDs" method="get" path="/api/v1/apps/{app_id}/resource_types/{resource_type_id}/resource/{resource_id}/ownerids" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_resource_owners.list_owner_i_ds(request={
        "app_id": "<id>",
        "resource_id": "<id>",
        "resource_type_id": "<id>",
    })

    assert res.list_app_resource_owner_i_ds_response is not None

    # Handle response
    print(res.list_app_resource_owner_i_ds_response)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.C1APIAppV1AppResourceOwnersListOwnerIDsRequest](../../models/operations/c1apiappv1appresourceownerslistowneridsrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[operations.C1APIAppV1AppResourceOwnersListOwnerIDsResponse](../../models/operations/c1apiappv1appresourceownerslistowneridsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove

Invokes the c1.api.app.v1.AppResourceOwners.Remove method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceOwners.Remove" method="delete" path="/api/v1/apps/{app_id}/resource_types/{resource_type_id}/resource/{resource_id}/owners" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_resource_owners.remove(request={
        "app_id": "<id>",
        "resource_id": "<id>",
        "resource_type_id": "<id>",
    })

    assert res.remove_app_resource_owner_response is not None

    # Handle response
    print(res.remove_app_resource_owner_response)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.C1APIAppV1AppResourceOwnersRemoveRequest](../../models/operations/c1apiappv1appresourceownersremoverequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[operations.C1APIAppV1AppResourceOwnersRemoveResponse](../../models/operations/c1apiappv1appresourceownersremoveresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## set

Sets the owners for a given app resource to the specified list of users.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceOwners.Set" method="put" path="/api/v1/apps/{app_id}/resource_types/{resource_type_id}/resource/{resource_id}/owners" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_resource_owners.set(request={
        "app_id": "<id>",
        "resource_id": "<id>",
        "resource_type_id": "<id>",
    })

    assert res.set_app_resource_owners_response is not None

    # Handle response
    print(res.set_app_resource_owners_response)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.C1APIAppV1AppResourceOwnersSetRequest](../../models/operations/c1apiappv1appresourceownerssetrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.C1APIAppV1AppResourceOwnersSetResponse](../../models/operations/c1apiappv1appresourceownerssetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |