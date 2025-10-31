# AppResourceType
(*app_resource_type*)

## Overview

### Available Operations

* [create_manually_managed_resource_type](#create_manually_managed_resource_type) - Create Manually Managed Resource Type
* [delete_manually_managed_resource_type](#delete_manually_managed_resource_type) - Delete Manually Managed Resource Type
* [get](#get) - Get
* [list](#list) - List
* [update_manually_managed_resource_type](#update_manually_managed_resource_type) - Update Manually Managed Resource Type

## create_manually_managed_resource_type

Invokes the c1.api.app.v1.AppResourceTypeService.CreateManuallyManagedResourceType method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceTypeService.CreateManuallyManagedResourceType" method="post" path="/api/v1/apps/{app_id}/resource_types" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource_type.create_manually_managed_resource_type(request={
        "create_manually_managed_resource_type_request": {
            "display_name": "Vito_Goyette",
            "resource_type": shared.ResourceType.PROFILE_TYPE,
        },
        "app_id": "<id>",
    })

    assert res.create_manually_managed_resource_type_response is not None

    # Handle response
    print(res.create_manually_managed_resource_type_response)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                  | [operations.C1APIAppV1AppResourceTypeServiceCreateManuallyManagedResourceTypeRequest](../../models/operations/c1apiappv1appresourcetypeservicecreatemanuallymanagedresourcetyperequest.md) | :heavy_check_mark:                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                 |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |

### Response

**[operations.C1APIAppV1AppResourceTypeServiceCreateManuallyManagedResourceTypeResponse](../../models/operations/c1apiappv1appresourcetypeservicecreatemanuallymanagedresourcetyperesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_manually_managed_resource_type

Invokes the c1.api.app.v1.AppResourceTypeService.DeleteManuallyManagedResourceType method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceTypeService.DeleteManuallyManagedResourceType" method="delete" path="/api/v1/apps/{app_id}/resource_types/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource_type.delete_manually_managed_resource_type(request={
        "delete_manually_managed_resource_type_request": {},
        "app_id": "<id>",
        "id": "<id>",
    })

    assert res.delete_manually_managed_resource_type_response is not None

    # Handle response
    print(res.delete_manually_managed_resource_type_response)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                  | [operations.C1APIAppV1AppResourceTypeServiceDeleteManuallyManagedResourceTypeRequest](../../models/operations/c1apiappv1appresourcetypeservicedeletemanuallymanagedresourcetyperequest.md) | :heavy_check_mark:                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                 |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |

### Response

**[operations.C1APIAppV1AppResourceTypeServiceDeleteManuallyManagedResourceTypeResponse](../../models/operations/c1apiappv1appresourcetypeservicedeletemanuallymanagedresourcetyperesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Get an app resource type.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceTypeService.Get" method="get" path="/api/v1/apps/{app_id}/resource_types/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource_type.get(request={
        "app_id": "<id>",
        "id": "<id>",
    })

    assert res.app_resource_type_service_get_response is not None

    # Handle response
    print(res.app_resource_type_service_get_response)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.C1APIAppV1AppResourceTypeServiceGetRequest](../../models/operations/c1apiappv1appresourcetypeservicegetrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[operations.C1APIAppV1AppResourceTypeServiceGetResponse](../../models/operations/c1apiappv1appresourcetypeservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

List app resource types.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceTypeService.List" method="get" path="/api/v1/apps/{app_id}/resource_types" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource_type.list(request={
        "app_id": "<id>",
    })

    assert res.app_resource_type_service_list_response is not None

    # Handle response
    print(res.app_resource_type_service_list_response)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIAppV1AppResourceTypeServiceListRequest](../../models/operations/c1apiappv1appresourcetypeservicelistrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.C1APIAppV1AppResourceTypeServiceListResponse](../../models/operations/c1apiappv1appresourcetypeservicelistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_manually_managed_resource_type

Invokes the c1.api.app.v1.AppResourceTypeService.UpdateManuallyManagedResourceType method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceTypeService.UpdateManuallyManagedResourceType" method="post" path="/api/v1/apps/{app_id}/resource_types/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource_type.update_manually_managed_resource_type(request={
        "update_manually_managed_resource_type_request": {},
        "app_id": "<id>",
        "id": "<id>",
    })

    assert res.update_manually_managed_resource_type_response is not None

    # Handle response
    print(res.update_manually_managed_resource_type_response)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                  | [operations.C1APIAppV1AppResourceTypeServiceUpdateManuallyManagedResourceTypeRequest](../../models/operations/c1apiappv1appresourcetypeserviceupdatemanuallymanagedresourcetyperequest.md) | :heavy_check_mark:                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                 |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |

### Response

**[operations.C1APIAppV1AppResourceTypeServiceUpdateManuallyManagedResourceTypeResponse](../../models/operations/c1apiappv1appresourcetypeserviceupdatemanuallymanagedresourcetyperesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |