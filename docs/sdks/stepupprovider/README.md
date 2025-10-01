# StepUpProvider
(*step_up_provider*)

## Overview

### Available Operations

* [create](#create) - Create
* [delete](#delete) - Delete
* [get](#get) - Get
* [list](#list) - List
* [search](#search) - Search
* [test](#test) - Test
* [update](#update) - Update
* [update_secret](#update_secret) - Update Secret

## create

Invokes the c1.api.stepup.v1.StepUpProviderService.Create method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.stepup.v1.StepUpProviderService.Create" method="post" path="/api/v1/step-up/providers" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.step_up_provider.create()

    assert res.create_step_up_provider_response is not None

    # Handle response
    print(res.create_step_up_provider_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.CreateStepUpProviderRequest](../../models/shared/createstepupproviderrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.C1APIStepupV1StepUpProviderServiceCreateResponse](../../models/operations/c1apistepupv1stepupproviderservicecreateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Invokes the c1.api.stepup.v1.StepUpProviderService.Delete method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.stepup.v1.StepUpProviderService.Delete" method="delete" path="/api/v1/step-up/providers/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.step_up_provider.delete(request={
        "id": "<id>",
    })

    assert res.delete_step_up_provider_response is not None

    # Handle response
    print(res.delete_step_up_provider_response)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.C1APIStepupV1StepUpProviderServiceDeleteRequest](../../models/operations/c1apistepupv1stepupproviderservicedeleterequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |

### Response

**[operations.C1APIStepupV1StepUpProviderServiceDeleteResponse](../../models/operations/c1apistepupv1stepupproviderservicedeleteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Invokes the c1.api.stepup.v1.StepUpProviderService.Get method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.stepup.v1.StepUpProviderService.Get" method="get" path="/api/v1/step-up/providers/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.step_up_provider.get(request={
        "id": "<id>",
    })

    assert res.get_step_up_provider_response is not None

    # Handle response
    print(res.get_step_up_provider_response)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.C1APIStepupV1StepUpProviderServiceGetRequest](../../models/operations/c1apistepupv1stepupproviderservicegetrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |

### Response

**[operations.C1APIStepupV1StepUpProviderServiceGetResponse](../../models/operations/c1apistepupv1stepupproviderservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

Invokes the c1.api.stepup.v1.StepUpProviderService.List method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.stepup.v1.StepUpProviderService.List" method="get" path="/api/v1/step-up/providers" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.step_up_provider.list()

    assert res.list_step_up_providers_response is not None

    # Handle response
    print(res.list_step_up_providers_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.C1APIStepupV1StepUpProviderServiceListResponse](../../models/operations/c1apistepupv1stepupproviderservicelistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## search

Search allows searching for step-up providers with various filters

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.stepup.v1.StepUpProviderService.Search" method="post" path="/api/v1/search/step-up/providers" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.step_up_provider.search()

    assert res.search_step_up_providers_response is not None

    # Handle response
    print(res.search_step_up_providers_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.SearchStepUpProvidersRequest](../../models/shared/searchstepupprovidersrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.C1APIStepupV1StepUpProviderServiceSearchResponse](../../models/operations/c1apistepupv1stepupproviderservicesearchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## test

Invokes the c1.api.stepup.v1.StepUpProviderService.Test method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.stepup.v1.StepUpProviderService.Test" method="post" path="/api/v1/step-up/providers/{id}/test" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.step_up_provider.test(request={
        "id": "<id>",
    })

    assert res.test_step_up_provider_response is not None

    # Handle response
    print(res.test_step_up_provider_response)

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.C1APIStepupV1StepUpProviderServiceTestRequest](../../models/operations/c1apistepupv1stepupproviderservicetestrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `retries`                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                     | :heavy_minus_sign:                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                  |

### Response

**[operations.C1APIStepupV1StepUpProviderServiceTestResponse](../../models/operations/c1apistepupv1stepupproviderservicetestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Invokes the c1.api.stepup.v1.StepUpProviderService.Update method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.stepup.v1.StepUpProviderService.Update" method="post" path="/api/v1/step-up/providers/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.step_up_provider.update(request={
        "id": "<id>",
    })

    assert res.update_step_up_provider_response is not None

    # Handle response
    print(res.update_step_up_provider_response)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.C1APIStepupV1StepUpProviderServiceUpdateRequest](../../models/operations/c1apistepupv1stepupproviderserviceupdaterequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |

### Response

**[operations.C1APIStepupV1StepUpProviderServiceUpdateResponse](../../models/operations/c1apistepupv1stepupproviderserviceupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_secret

Invokes the c1.api.stepup.v1.StepUpProviderService.UpdateSecret method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.stepup.v1.StepUpProviderService.UpdateSecret" method="post" path="/api/v1/step-up/providers/{id}/secret" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.step_up_provider.update_secret(request={
        "id": "<id>",
    })

    assert res.update_step_up_provider_secret_response is not None

    # Handle response
    print(res.update_step_up_provider_secret_response)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.C1APIStepupV1StepUpProviderServiceUpdateSecretRequest](../../models/operations/c1apistepupv1stepupproviderserviceupdatesecretrequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |

### Response

**[operations.C1APIStepupV1StepUpProviderServiceUpdateSecretResponse](../../models/operations/c1apistepupv1stepupproviderserviceupdatesecretresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |