# AppResourceOwners
(*app_resource_owners*)

## Overview

### Available Operations

* [add](#add) - Add
* [list](#list) - List
* [remove](#remove) - Remove

## add

Invokes the c1.api.app.v1.AppResourceOwners.Add method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceOwners.Add" method="post" path="/api/v1/apps/{app_id}/resource_types/{resource_type_id}/resource/{resource_id}/owners" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource_owners.add(request={
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

## list

List all owners of an app resource.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceOwners.List" method="get" path="/api/v1/apps/{app_id}/resource_types/{resource_type_id}/resource/{resource_id}/owners" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource_owners.list(request={
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

## remove

Invokes the c1.api.app.v1.AppResourceOwners.Remove method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceOwners.Remove" method="delete" path="/api/v1/apps/{app_id}/resource_types/{resource_type_id}/resource/{resource_id}/owners" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource_owners.remove(request={
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