# FunctionsInvocation
(*functions_invocation*)

## Overview

### Available Operations

* [get](#get) - Get
* [list](#list) - List

## get

Get retrieves a specific invocation by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsInvocationService.Get" method="get" path="/api/v1/functions/{function_id}/invocations/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.functions_invocation.get(request={
        "function_id": "<id>",
        "id": "<id>",
    })

    assert res.functions_invocation_service_get_response is not None

    # Handle response
    print(res.functions_invocation_service_get_response)

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.C1APIFunctionsV1FunctionsInvocationServiceGetRequest](../../models/operations/c1apifunctionsv1functionsinvocationservicegetrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[operations.C1APIFunctionsV1FunctionsInvocationServiceGetResponse](../../models/operations/c1apifunctionsv1functionsinvocationservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

List retrieves the invocation history for a function

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsInvocationService.List" method="get" path="/api/v1/functions/{function_id}/invocations" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.functions_invocation.list(request={
        "function_id": "<id>",
    })

    assert res.functions_invocation_service_list_response is not None

    # Handle response
    print(res.functions_invocation_service_list_response)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.C1APIFunctionsV1FunctionsInvocationServiceListRequest](../../models/operations/c1apifunctionsv1functionsinvocationservicelistrequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |

### Response

**[operations.C1APIFunctionsV1FunctionsInvocationServiceListResponse](../../models/operations/c1apifunctionsv1functionsinvocationservicelistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |