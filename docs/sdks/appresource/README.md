# AppResource
(*app_resource*)

## Overview

### Available Operations

* [create_manually_managed_app_resource](#create_manually_managed_app_resource) - Create Manually Managed App Resource
* [delete_manually_managed_app_resource](#delete_manually_managed_app_resource) - Delete Manually Managed App Resource
* [get](#get) - Get
* [list](#list) - List
* [update](#update) - Update

## create_manually_managed_app_resource

Invokes the c1.api.app.v1.AppResourceService.CreateManuallyManagedAppResource method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceService.CreateManuallyManagedAppResource" method="post" path="/api/v1/apps/{app_id}/resource_types/{app_resource_type_id}/resources" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource.create_manually_managed_app_resource(request={
        "app_id": "<id>",
        "app_resource_type_id": "<id>",
    })

    assert res.create_manually_managed_app_resource_response is not None

    # Handle response
    print(res.create_manually_managed_app_resource_response)

```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                        | [operations.C1APIAppV1AppResourceServiceCreateManuallyManagedAppResourceRequest](../../models/operations/c1apiappv1appresourceservicecreatemanuallymanagedappresourcerequest.md) | :heavy_check_mark:                                                                                                                                                               | The request object to use for the request.                                                                                                                                       |
| `retries`                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                              |

### Response

**[operations.C1APIAppV1AppResourceServiceCreateManuallyManagedAppResourceResponse](../../models/operations/c1apiappv1appresourceservicecreatemanuallymanagedappresourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_manually_managed_app_resource

Invokes the c1.api.app.v1.AppResourceService.DeleteManuallyManagedAppResource method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceService.DeleteManuallyManagedAppResource" method="delete" path="/api/v1/apps/{app_id}/resource_types/{app_resource_type_id}/resources/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource.delete_manually_managed_app_resource(request={
        "app_id": "<id>",
        "app_resource_type_id": "<id>",
        "id": "<id>",
    })

    assert res.delete_manually_managed_app_resource_response is not None

    # Handle response
    print(res.delete_manually_managed_app_resource_response)

```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                        | [operations.C1APIAppV1AppResourceServiceDeleteManuallyManagedAppResourceRequest](../../models/operations/c1apiappv1appresourceservicedeletemanuallymanagedappresourcerequest.md) | :heavy_check_mark:                                                                                                                                                               | The request object to use for the request.                                                                                                                                       |
| `retries`                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                              |

### Response

**[operations.C1APIAppV1AppResourceServiceDeleteManuallyManagedAppResourceResponse](../../models/operations/c1apiappv1appresourceservicedeletemanuallymanagedappresourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Invokes the c1.api.app.v1.AppResourceService.Get method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceService.Get" method="get" path="/api/v1/apps/{app_id}/resource_types/{app_resource_type_id}/resources/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource.get(request={
        "app_id": "<id>",
        "app_resource_type_id": "<id>",
        "id": "<id>",
    })

    assert res.app_resource_service_get_response is not None

    # Handle response
    print(res.app_resource_service_get_response)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.C1APIAppV1AppResourceServiceGetRequest](../../models/operations/c1apiappv1appresourceservicegetrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[operations.C1APIAppV1AppResourceServiceGetResponse](../../models/operations/c1apiappv1appresourceservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

Invokes the c1.api.app.v1.AppResourceService.List method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceService.List" method="get" path="/api/v1/apps/{app_id}/resource_types/{app_resource_type_id}/resources" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource.list(request={
        "app_id": "<id>",
        "app_resource_type_id": "<id>",
    })

    assert res.app_resource_service_list_response is not None

    # Handle response
    print(res.app_resource_service_list_response)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.C1APIAppV1AppResourceServiceListRequest](../../models/operations/c1apiappv1appresourceservicelistrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[operations.C1APIAppV1AppResourceServiceListResponse](../../models/operations/c1apiappv1appresourceservicelistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Invokes the c1.api.app.v1.AppResourceService.Update method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceService.Update" method="post" path="/api/v1/apps/{app_id}/resource_types/{app_resource_type_id}/resources/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_resource.update(request={
        "app_id": "<id>",
        "app_resource_type_id": "<id>",
        "id": "<id>",
    })

    assert res.app_resource_service_update_response is not None

    # Handle response
    print(res.app_resource_service_update_response)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.C1APIAppV1AppResourceServiceUpdateRequest](../../models/operations/c1apiappv1appresourceserviceupdaterequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.C1APIAppV1AppResourceServiceUpdateResponse](../../models/operations/c1apiappv1appresourceserviceupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |