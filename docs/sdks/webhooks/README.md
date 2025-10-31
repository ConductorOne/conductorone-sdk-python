# Webhooks
(*webhooks*)

## Overview

### Available Operations

* [create](#create) - Create
* [delete](#delete) - Delete
* [get](#get) - Get
* [list](#list) - List
* [test](#test) - Test
* [update](#update) - Update

## create

Invokes the c1.api.webhooks.v1.WebhooksService.Create method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.webhooks.v1.WebhooksService.Create" method="post" path="/api/v1/webhooks" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.webhooks.create(request={
        "display_name": "Bradley_Maggio",
        "url": "https://musty-kick.net",
    })

    assert res.webhooks_service_create_response is not None

    # Handle response
    print(res.webhooks_service_create_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.WebhooksServiceCreateRequest](../../models/shared/webhooksservicecreaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.C1APIWebhooksV1WebhooksServiceCreateResponse](../../models/operations/c1apiwebhooksv1webhooksservicecreateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Invokes the c1.api.webhooks.v1.WebhooksService.Delete method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.webhooks.v1.WebhooksService.Delete" method="delete" path="/api/v1/webhooks/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.webhooks.delete(request={
        "webhooks_service_delete_request": {},
        "id": "<id>",
    })

    assert res.webhooks_service_delete_response is not None

    # Handle response
    print(res.webhooks_service_delete_response)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIWebhooksV1WebhooksServiceDeleteRequest](../../models/operations/c1apiwebhooksv1webhooksservicedeleterequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.C1APIWebhooksV1WebhooksServiceDeleteResponse](../../models/operations/c1apiwebhooksv1webhooksservicedeleteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Invokes the c1.api.webhooks.v1.WebhooksService.Get method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.webhooks.v1.WebhooksService.Get" method="get" path="/api/v1/webhooks/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.webhooks.get(request={
        "id": "<id>",
    })

    assert res.webhooks_service_get_response is not None

    # Handle response
    print(res.webhooks_service_get_response)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.C1APIWebhooksV1WebhooksServiceGetRequest](../../models/operations/c1apiwebhooksv1webhooksservicegetrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[operations.C1APIWebhooksV1WebhooksServiceGetResponse](../../models/operations/c1apiwebhooksv1webhooksservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

Invokes the c1.api.webhooks.v1.WebhooksService.List method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.webhooks.v1.WebhooksService.List" method="get" path="/api/v1/webhooks" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.webhooks.list()

    assert res.webhooks_service_list_response is not None

    # Handle response
    print(res.webhooks_service_list_response)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.C1APIWebhooksV1WebhooksServiceListRequest](../../models/operations/c1apiwebhooksv1webhooksservicelistrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.C1APIWebhooksV1WebhooksServiceListResponse](../../models/operations/c1apiwebhooksv1webhooksservicelistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## test

Invokes the c1.api.webhooks.v1.WebhooksService.Test method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.webhooks.v1.WebhooksService.Test" method="post" path="/api/v1/webhooks/{id}/test" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.webhooks.test(request={
        "webhooks_service_test_request": {},
        "id": "<id>",
    })

    assert res.webhooks_service_test_response is not None

    # Handle response
    print(res.webhooks_service_test_response)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.C1APIWebhooksV1WebhooksServiceTestRequest](../../models/operations/c1apiwebhooksv1webhooksservicetestrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.C1APIWebhooksV1WebhooksServiceTestResponse](../../models/operations/c1apiwebhooksv1webhooksservicetestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Invokes the c1.api.webhooks.v1.WebhooksService.Update method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.webhooks.v1.WebhooksService.Update" method="post" path="/api/v1/webhooks/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.webhooks.update(request={
        "webhooks_service_update_request": {},
        "id": "<id>",
    })

    assert res.webhooks_service_update_response is not None

    # Handle response
    print(res.webhooks_service_update_response)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIWebhooksV1WebhooksServiceUpdateRequest](../../models/operations/c1apiwebhooksv1webhooksserviceupdaterequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.C1APIWebhooksV1WebhooksServiceUpdateResponse](../../models/operations/c1apiwebhooksv1webhooksserviceupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |