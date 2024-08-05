# AppAccessRequestsDefaults
(*app_access_requests_defaults*)

### Available Operations

* [cancel_app_access_requests_defaults](#cancel_app_access_requests_defaults) - Cancel App Access Requests Defaults
* [create_app_access_requests_defaults](#create_app_access_requests_defaults) - Create App Access Requests Defaults
* [get_app_access_requests_defaults](#get_app_access_requests_defaults) - Get App Access Requests Defaults

## cancel_app_access_requests_defaults

Invokes the c1.api.app.v1.AppAccessRequestsDefaultsService.CancelAppAccessRequestsDefaults method.

### Example Usage

```python
from openapi import SDK
from openapi.models import shared

s = SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.app_access_requests_defaults.cancel_app_access_requests_defaults(request={
    "app_id": "<value>",
})

if res.app_access_request_defaults is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                  | Type                                                                                                                                                                                                       | Required                                                                                                                                                                                                   | Description                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                  | [operations.C1APIAppV1AppAccessRequestsDefaultsServiceCancelAppAccessRequestsDefaultsRequest](../../models/operations/c1apiappv1appaccessrequestsdefaultsservicecancelappaccessrequestsdefaultsrequest.md) | :heavy_check_mark:                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                        |


### Response

**[operations.C1APIAppV1AppAccessRequestsDefaultsServiceCancelAppAccessRequestsDefaultsResponse](../../models/operations/c1apiappv1appaccessrequestsdefaultsservicecancelappaccessrequestsdefaultsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_app_access_requests_defaults

Invokes the c1.api.app.v1.AppAccessRequestsDefaultsService.CreateAppAccessRequestsDefaults method.

### Example Usage

```python
from openapi import SDK
from openapi.models import shared

s = SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.app_access_requests_defaults.create_app_access_requests_defaults(request={
    "app_id": "<value>",
})

if res.app_access_request_defaults is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                  | Type                                                                                                                                                                                                       | Required                                                                                                                                                                                                   | Description                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                  | [operations.C1APIAppV1AppAccessRequestsDefaultsServiceCreateAppAccessRequestsDefaultsRequest](../../models/operations/c1apiappv1appaccessrequestsdefaultsservicecreateappaccessrequestsdefaultsrequest.md) | :heavy_check_mark:                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                        |


### Response

**[operations.C1APIAppV1AppAccessRequestsDefaultsServiceCreateAppAccessRequestsDefaultsResponse](../../models/operations/c1apiappv1appaccessrequestsdefaultsservicecreateappaccessrequestsdefaultsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_app_access_requests_defaults

Invokes the c1.api.app.v1.AppAccessRequestsDefaultsService.GetAppAccessRequestsDefaults method.

### Example Usage

```python
from openapi import SDK
from openapi.models import shared

s = SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.app_access_requests_defaults.get_app_access_requests_defaults(request={
    "app_id": "<value>",
})

if res.app_access_request_defaults is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                            | [operations.C1APIAppV1AppAccessRequestsDefaultsServiceGetAppAccessRequestsDefaultsRequest](../../models/operations/c1apiappv1appaccessrequestsdefaultsservicegetappaccessrequestsdefaultsrequest.md) | :heavy_check_mark:                                                                                                                                                                                   | The request object to use for the request.                                                                                                                                                           |
| `retries`                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                  |


### Response

**[operations.C1APIAppV1AppAccessRequestsDefaultsServiceGetAppAccessRequestsDefaultsResponse](../../models/operations/c1apiappv1appaccessrequestsdefaultsservicegetappaccessrequestsdefaultsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
