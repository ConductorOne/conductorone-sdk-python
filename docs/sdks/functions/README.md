# Functions
(*functions*)

## Overview

### Available Operations

* [create_function](#create_function) - Create Function
* [create_tag](#create_tag) - Create Tag
* [delete_function](#delete_function) - Delete Function
* [get_function](#get_function) - Get Function
* [get_function_secret_encryption_key](#get_function_secret_encryption_key) - Get Function Secret Encryption Key
* [invoke](#invoke) - Invoke
* [list_commits](#list_commits) - List Commits
* [list_functions](#list_functions) - List Functions
* [list_tags](#list_tags) - List Tags
* [update_function](#update_function) - Update Function

## create_function

Invokes the c1.api.functions.v1.FunctionsService.CreateFunction method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsService.CreateFunction" method="post" path="/api/v1/functions" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.functions.create_function(request={})

    assert res.functions_service_create_function_response is not None

    # Handle response
    print(res.functions_service_create_function_response)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [shared.FunctionsServiceCreateFunctionRequest](../../models/shared/functionsservicecreatefunctionrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.C1APIFunctionsV1FunctionsServiceCreateFunctionResponse](../../models/operations/c1apifunctionsv1functionsservicecreatefunctionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_tag

CreateTag creates a named reference to a specific commit

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsService.CreateTag" method="post" path="/api/v1/functions/{function_id}/tags" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.functions.create_tag(request={
        "functions_service_create_tag_request": {},
        "function_id": "<id>",
    })

    assert res.functions_service_create_tag_response is not None

    # Handle response
    print(res.functions_service_create_tag_response)

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.C1APIFunctionsV1FunctionsServiceCreateTagRequest](../../models/operations/c1apifunctionsv1functionsservicecreatetagrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |

### Response

**[operations.C1APIFunctionsV1FunctionsServiceCreateTagResponse](../../models/operations/c1apifunctionsv1functionsservicecreatetagresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_function

Delete removes a function

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsService.DeleteFunction" method="delete" path="/api/v1/functions/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.functions.delete_function(request={
        "functions_service_delete_function_request": {},
        "id": "<id>",
    })

    assert res.functions_service_delete_function_response is not None

    # Handle response
    print(res.functions_service_delete_function_response)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.C1APIFunctionsV1FunctionsServiceDeleteFunctionRequest](../../models/operations/c1apifunctionsv1functionsservicedeletefunctionrequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |

### Response

**[operations.C1APIFunctionsV1FunctionsServiceDeleteFunctionResponse](../../models/operations/c1apifunctionsv1functionsservicedeletefunctionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_function

Get retrieves a specific function by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsService.GetFunction" method="get" path="/api/v1/functions/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.functions.get_function(request={
        "id": "<id>",
    })

    assert res.functions_service_get_function_response is not None

    # Handle response
    print(res.functions_service_get_function_response)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.C1APIFunctionsV1FunctionsServiceGetFunctionRequest](../../models/operations/c1apifunctionsv1functionsservicegetfunctionrequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |

### Response

**[operations.C1APIFunctionsV1FunctionsServiceGetFunctionResponse](../../models/operations/c1apifunctionsv1functionsservicegetfunctionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_function_secret_encryption_key

GetFunctionSecretEncryptionKey retrieves or generates the public key for encrypting function secrets

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsService.GetFunctionSecretEncryptionKey" method="get" path="/api/v1/functions/{function_id}/secret-encryption-key" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.functions.get_function_secret_encryption_key(request={
        "function_id": "<id>",
    })

    assert res.functions_service_get_function_secret_encryption_key_response is not None

    # Handle response
    print(res.functions_service_get_function_secret_encryption_key_response)

```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                            | [operations.C1APIFunctionsV1FunctionsServiceGetFunctionSecretEncryptionKeyRequest](../../models/operations/c1apifunctionsv1functionsservicegetfunctionsecretencryptionkeyrequest.md) | :heavy_check_mark:                                                                                                                                                                   | The request object to use for the request.                                                                                                                                           |
| `retries`                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                  |

### Response

**[operations.C1APIFunctionsV1FunctionsServiceGetFunctionSecretEncryptionKeyResponse](../../models/operations/c1apifunctionsv1functionsservicegetfunctionsecretencryptionkeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## invoke

Invokes the c1.api.functions.v1.FunctionsService.Invoke method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsService.Invoke" method="post" path="/api/v1/functions/{function_id}/invoke" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.functions.invoke(request={
        "functions_service_invoke_request": {},
        "function_id": "<id>",
    })

    assert res.functions_service_invoke_response is not None

    # Handle response
    print(res.functions_service_invoke_response)

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.C1APIFunctionsV1FunctionsServiceInvokeRequest](../../models/operations/c1apifunctionsv1functionsserviceinvokerequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `retries`                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                     | :heavy_minus_sign:                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                  |

### Response

**[operations.C1APIFunctionsV1FunctionsServiceInvokeResponse](../../models/operations/c1apifunctionsv1functionsserviceinvokeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commits

ListCommits retrieves the commit history

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsService.ListCommits" method="get" path="/api/v1/functions/{function_id}/commits" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.functions.list_commits(request={
        "function_id": "<id>",
    })

    assert res.functions_service_list_commits_response is not None

    # Handle response
    print(res.functions_service_list_commits_response)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.C1APIFunctionsV1FunctionsServiceListCommitsRequest](../../models/operations/c1apifunctionsv1functionsservicelistcommitsrequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |

### Response

**[operations.C1APIFunctionsV1FunctionsServiceListCommitsResponse](../../models/operations/c1apifunctionsv1functionsservicelistcommitsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_functions

List retrieves all functions with pagination

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsService.ListFunctions" method="get" path="/api/v1/functions" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.functions.list_functions()

    assert res.functions_service_list_functions_response is not None

    # Handle response
    print(res.functions_service_list_functions_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.C1APIFunctionsV1FunctionsServiceListFunctionsResponse](../../models/operations/c1apifunctionsv1functionsservicelistfunctionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_tags

ListTags lists all tags for a function

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsService.ListTags" method="get" path="/api/v1/functions/{function_id}/tags" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.functions.list_tags(request={
        "function_id": "<id>",
    })

    assert res.functions_service_list_tags_response is not None

    # Handle response
    print(res.functions_service_list_tags_response)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.C1APIFunctionsV1FunctionsServiceListTagsRequest](../../models/operations/c1apifunctionsv1functionsservicelisttagsrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |

### Response

**[operations.C1APIFunctionsV1FunctionsServiceListTagsResponse](../../models/operations/c1apifunctionsv1functionsservicelisttagsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_function

Update updates an existing function's metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsService.UpdateFunction" method="post" path="/api/v1/functions/update" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.functions.update_function(request={})

    assert res.functions_service_update_function_response is not None

    # Handle response
    print(res.functions_service_update_function_response)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [shared.FunctionsServiceUpdateFunctionRequest](../../models/shared/functionsserviceupdatefunctionrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.C1APIFunctionsV1FunctionsServiceUpdateFunctionResponse](../../models/operations/c1apifunctionsv1functionsserviceupdatefunctionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |