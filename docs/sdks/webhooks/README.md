# Webhooks
(*webhooks*)

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

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.webhooks.create(request=shared.WebhooksServiceCreateRequest())

if res.webhooks_service_create_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.WebhooksServiceCreateRequest](../../models/shared/webhooksservicecreaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.C1APIWebhooksV1WebhooksServiceCreateResponse](../../models/operations/c1apiwebhooksv1webhooksservicecreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete

Invokes the c1.api.webhooks.v1.WebhooksService.Delete method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.webhooks.delete(request=operations.C1APIWebhooksV1WebhooksServiceDeleteRequest(
    id='<id>',
))

if res.webhooks_service_delete_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIWebhooksV1WebhooksServiceDeleteRequest](../../models/operations/c1apiwebhooksv1webhooksservicedeleterequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.C1APIWebhooksV1WebhooksServiceDeleteResponse](../../models/operations/c1apiwebhooksv1webhooksservicedeleteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get

Invokes the c1.api.webhooks.v1.WebhooksService.Get method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.webhooks.get(request=operations.C1APIWebhooksV1WebhooksServiceGetRequest(
    id='<id>',
))

if res.webhooks_service_get_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.C1APIWebhooksV1WebhooksServiceGetRequest](../../models/operations/c1apiwebhooksv1webhooksservicegetrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.C1APIWebhooksV1WebhooksServiceGetResponse](../../models/operations/c1apiwebhooksv1webhooksservicegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list

Invokes the c1.api.webhooks.v1.WebhooksService.List method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.webhooks.list(request=operations.C1APIWebhooksV1WebhooksServiceListRequest())

if res.webhooks_service_list_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.C1APIWebhooksV1WebhooksServiceListRequest](../../models/operations/c1apiwebhooksv1webhooksservicelistrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.C1APIWebhooksV1WebhooksServiceListResponse](../../models/operations/c1apiwebhooksv1webhooksservicelistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## test

Invokes the c1.api.webhooks.v1.WebhooksService.Test method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.webhooks.test(request=operations.C1APIWebhooksV1WebhooksServiceTestRequest(
    id='<id>',
))

if res.webhooks_service_test_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.C1APIWebhooksV1WebhooksServiceTestRequest](../../models/operations/c1apiwebhooksv1webhooksservicetestrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.C1APIWebhooksV1WebhooksServiceTestResponse](../../models/operations/c1apiwebhooksv1webhooksservicetestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update

Invokes the c1.api.webhooks.v1.WebhooksService.Update method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.webhooks.update(request=operations.C1APIWebhooksV1WebhooksServiceUpdateRequest(
    id='<id>',
))

if res.webhooks_service_update_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIWebhooksV1WebhooksServiceUpdateRequest](../../models/operations/c1apiwebhooksv1webhooksserviceupdaterequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.C1APIWebhooksV1WebhooksServiceUpdateResponse](../../models/operations/c1apiwebhooksv1webhooksserviceupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
