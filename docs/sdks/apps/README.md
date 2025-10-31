# Apps
(*apps*)

## Overview

### Available Operations

* [create](#create) - Create
* [delete](#delete) - Delete
* [get](#get) - Get
* [list](#list) - List
* [update](#update) - Update

## create

Create a new manual app without a connector.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.Apps.Create" method="post" path="/api/v1/apps" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.apps.create(request={
        "display_name": "Ciara.Goyette89",
    })

    assert res.create_app_response is not None

    # Handle response
    print(res.create_app_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.CreateAppRequest](../../models/shared/createapprequest.md)  | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.C1APIAppV1AppsCreateResponse](../../models/operations/c1apiappv1appscreateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Delete an app.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.Apps.Delete" method="delete" path="/api/v1/apps/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.apps.delete(request={
        "delete_app_request": {},
        "id": "<id>",
    })

    assert res.delete_app_response is not None

    # Handle response
    print(res.delete_app_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.C1APIAppV1AppsDeleteRequest](../../models/operations/c1apiappv1appsdeleterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.C1APIAppV1AppsDeleteResponse](../../models/operations/c1apiappv1appsdeleteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Get an app by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.Apps.Get" method="get" path="/api/v1/apps/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.apps.get(request={
        "id": "<id>",
    })

    assert res.get_app_response is not None

    # Handle response
    print(res.get_app_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.C1APIAppV1AppsGetRequest](../../models/operations/c1apiappv1appsgetrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.C1APIAppV1AppsGetResponse](../../models/operations/c1apiappv1appsgetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

List all apps.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.Apps.List" method="get" path="/api/v1/apps" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.apps.list()

    assert res.list_apps_response is not None

    # Handle response
    print(res.list_apps_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.C1APIAppV1AppsListRequest](../../models/operations/c1apiappv1appslistrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.C1APIAppV1AppsListResponse](../../models/operations/c1apiappv1appslistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Update an existing app.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.Apps.Update" method="post" path="/api/v1/apps/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.apps.update(request={
        "update_app_request": {},
        "id": "<id>",
    })

    assert res.update_app_response is not None

    # Handle response
    print(res.update_app_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.C1APIAppV1AppsUpdateRequest](../../models/operations/c1apiappv1appsupdaterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.C1APIAppV1AppsUpdateResponse](../../models/operations/c1apiappv1appsupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |