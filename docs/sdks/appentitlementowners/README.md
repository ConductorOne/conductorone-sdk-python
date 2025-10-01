# AppEntitlementOwners
(*app_entitlement_owners*)

## Overview

### Available Operations

* [add](#add) - Add
* [delete](#delete) - Delete
* [list](#list) - List
* [list_owner_i_ds](#list_owner_i_ds) - List Owner I Ds
* [remove](#remove) - Remove
* [set](#set) - Set

## add

Add an owner to a given app entitlement.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementOwners.Add" method="post" path="/api/v1/apps/{app_id}/entitlements/{entitlement_id}/owners" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlement_owners.add(request={
        "app_id": "<id>",
        "entitlement_id": "<id>",
    })

    assert res.add_app_entitlement_owner_response is not None

    # Handle response
    print(res.add_app_entitlement_owner_response)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.C1APIAppV1AppEntitlementOwnersAddRequest](../../models/operations/c1apiappv1appentitlementownersaddrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[operations.C1APIAppV1AppEntitlementOwnersAddResponse](../../models/operations/c1apiappv1appentitlementownersaddresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Delete deletes the owners from a given app entitlement.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementOwners.Delete" method="delete" path="/api/v1/apps/{app_id}/entitlements/{entitlement_id}/owners" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlement_owners.delete(request={
        "app_id": "<id>",
        "entitlement_id": "<id>",
    })

    assert res.delete_app_entitlement_owners_response is not None

    # Handle response
    print(res.delete_app_entitlement_owners_response)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIAppV1AppEntitlementOwnersDeleteRequest](../../models/operations/c1apiappv1appentitlementownersdeleterequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.C1APIAppV1AppEntitlementOwnersDeleteResponse](../../models/operations/c1apiappv1appentitlementownersdeleteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

List owners for a given app entitlement.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementOwners.List" method="get" path="/api/v1/apps/{app_id}/entitlements/{entitlement_id}/owners" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlement_owners.list(request={
        "app_id": "<id>",
        "entitlement_id": "<id>",
    })

    assert res.list_app_entitlement_owners_response is not None

    # Handle response
    print(res.list_app_entitlement_owners_response)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.C1APIAppV1AppEntitlementOwnersListRequest](../../models/operations/c1apiappv1appentitlementownerslistrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.C1APIAppV1AppEntitlementOwnersListResponse](../../models/operations/c1apiappv1appentitlementownerslistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_owner_i_ds

ListUserIDs lists owner IDs for a given app entitlement.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementOwners.ListOwnerIDs" method="get" path="/api/v1/apps/{app_id}/entitlements/{entitlement_id}/ownerids" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlement_owners.list_owner_i_ds(request={
        "app_id": "<id>",
        "entitlement_id": "<id>",
    })

    assert res.list_app_entitlement_owner_i_ds_response is not None

    # Handle response
    print(res.list_app_entitlement_owner_i_ds_response)

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.C1APIAppV1AppEntitlementOwnersListOwnerIDsRequest](../../models/operations/c1apiappv1appentitlementownerslistowneridsrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |

### Response

**[operations.C1APIAppV1AppEntitlementOwnersListOwnerIDsResponse](../../models/operations/c1apiappv1appentitlementownerslistowneridsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove

Remove an owner from a given app entitlement.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementOwners.Remove" method="delete" path="/api/v1/apps/{app_id}/entitlements/{entitlement_id}/owners/{user_id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlement_owners.remove(request={
        "app_id": "<id>",
        "entitlement_id": "<id>",
        "user_id": "<id>",
    })

    assert res.remove_app_entitlement_owner_response is not None

    # Handle response
    print(res.remove_app_entitlement_owner_response)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIAppV1AppEntitlementOwnersRemoveRequest](../../models/operations/c1apiappv1appentitlementownersremoverequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.C1APIAppV1AppEntitlementOwnersRemoveResponse](../../models/operations/c1apiappv1appentitlementownersremoveresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## set

Sets the owners for a given app entitlement to the specified list of users.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementOwners.Set" method="put" path="/api/v1/apps/{app_id}/entitlements/{entitlement_id}/owners" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlement_owners.set(request={
        "app_id": "<id>",
        "entitlement_id": "<id>",
    })

    assert res.set_app_entitlement_owners_response is not None

    # Handle response
    print(res.set_app_entitlement_owners_response)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.C1APIAppV1AppEntitlementOwnersSetRequest](../../models/operations/c1apiappv1appentitlementownerssetrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[operations.C1APIAppV1AppEntitlementOwnersSetResponse](../../models/operations/c1apiappv1appentitlementownerssetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |