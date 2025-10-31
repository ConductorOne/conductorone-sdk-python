# PersonalClient
(*personal_client*)

## Overview

### Available Operations

* [create](#create) - Create
* [delete](#delete) - Delete
* [get](#get) - Get
* [list](#list) - NOTE: Only shows personal clients for the current user.
* [update](#update) - Update

## create

Create creates a new PersonalClient object for the current User.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.iam.v1.PersonalClientService.Create" method="post" path="/api/v1/iam/personal_clients" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.personal_client.create(request={})

    assert res.personal_client_service_create_response is not None

    # Handle response
    print(res.personal_client_service_create_response)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [shared.PersonalClientServiceCreateRequest](../../models/shared/personalclientservicecreaterequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.C1APIIamV1PersonalClientServiceCreateResponse](../../models/operations/c1apiiamv1personalclientservicecreateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Invokes the c1.api.iam.v1.PersonalClientService.Delete method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.iam.v1.PersonalClientService.Delete" method="delete" path="/api/v1/iam/personal_clients/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.personal_client.delete(request={
        "personal_client_service_delete_request": {},
        "id": "<id>",
    })

    assert res.personal_client_service_delete_response is not None

    # Handle response
    print(res.personal_client_service_delete_response)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.C1APIIamV1PersonalClientServiceDeleteRequest](../../models/operations/c1apiiamv1personalclientservicedeleterequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |

### Response

**[operations.C1APIIamV1PersonalClientServiceDeleteResponse](../../models/operations/c1apiiamv1personalclientservicedeleteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Invokes the c1.api.iam.v1.PersonalClientService.Get method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.iam.v1.PersonalClientService.Get" method="get" path="/api/v1/iam/personal_clients/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.personal_client.get(request={
        "id": "<id>",
    })

    assert res.personal_client_service_get_response is not None

    # Handle response
    print(res.personal_client_service_get_response)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.C1APIIamV1PersonalClientServiceGetRequest](../../models/operations/c1apiiamv1personalclientservicegetrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.C1APIIamV1PersonalClientServiceGetResponse](../../models/operations/c1apiiamv1personalclientservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

Invokes the c1.api.iam.v1.PersonalClientService.List method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.iam.v1.PersonalClientService.List" method="get" path="/api/v1/iam/personal_clients" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.personal_client.list()

    assert res.personal_client_service_list_response is not None

    # Handle response
    print(res.personal_client_service_list_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.C1APIIamV1PersonalClientServiceListResponse](../../models/operations/c1apiiamv1personalclientservicelistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Invokes the c1.api.iam.v1.PersonalClientService.Update method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.iam.v1.PersonalClientService.Update" method="post" path="/api/v1/iam/personal_clients/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.personal_client.update(request={
        "personal_client_service_update_request": {},
        "id": "<id>",
    })

    assert res.personal_client_service_update_response is not None

    # Handle response
    print(res.personal_client_service_update_response)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.C1APIIamV1PersonalClientServiceUpdateRequest](../../models/operations/c1apiiamv1personalclientserviceupdaterequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |

### Response

**[operations.C1APIIamV1PersonalClientServiceUpdateResponse](../../models/operations/c1apiiamv1personalclientserviceupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |