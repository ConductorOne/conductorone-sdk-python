# RequestSchema
(*request_schema*)

## Overview

### Available Operations

* [create](#create) - Create
* [create_entitlement_binding](#create_entitlement_binding) - Create Entitlement Binding
* [delete](#delete) - Delete
* [find_binding_for_app_entitlement](#find_binding_for_app_entitlement) - Find Binding For App Entitlement
* [get](#get) - Get
* [remove_entitlement_binding](#remove_entitlement_binding) - Remove Entitlement Binding
* [update](#update) - Update

## create

Invokes the c1.api.request_schema.v1.RequestSchemaService.Create method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.request_schema.v1.RequestSchemaService.Create" method="post" path="/api/v1/request_schemas" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.request_schema.create(request={})

    assert res.request_schema_service_create_response is not None

    # Handle response
    print(res.request_schema_service_create_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.RequestSchemaServiceCreateRequest](../../models/shared/requestschemaservicecreaterequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.C1APIRequestSchemaV1RequestSchemaServiceCreateResponse](../../models/operations/c1apirequestschemav1requestschemaservicecreateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_entitlement_binding

Invokes the c1.api.request_schema.v1.RequestSchemaService.CreateEntitlementBinding method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.request_schema.v1.RequestSchemaService.CreateEntitlementBinding" method="post" path="/api/v1/request_schema_entitlement_binding" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.request_schema.create_entitlement_binding(request={})

    assert res.request_schema_service_create_entitlement_binding_response is not None

    # Handle response
    print(res.request_schema_service_create_entitlement_binding_response)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [shared.RequestSchemaServiceCreateEntitlementBindingRequest](../../models/shared/requestschemaservicecreateentitlementbindingrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |

### Response

**[operations.C1APIRequestSchemaV1RequestSchemaServiceCreateEntitlementBindingResponse](../../models/operations/c1apirequestschemav1requestschemaservicecreateentitlementbindingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Invokes the c1.api.request_schema.v1.RequestSchemaService.Delete method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.request_schema.v1.RequestSchemaService.Delete" method="delete" path="/api/v1/request_schemas/{request_schema_id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.request_schema.delete(request={
        "request_schema_service_delete_request": {},
        "request_schema_id": "<id>",
    })

    assert res.request_schema_service_delete_response is not None

    # Handle response
    print(res.request_schema_service_delete_response)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.C1APIRequestSchemaV1RequestSchemaServiceDeleteRequest](../../models/operations/c1apirequestschemav1requestschemaservicedeleterequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |

### Response

**[operations.C1APIRequestSchemaV1RequestSchemaServiceDeleteResponse](../../models/operations/c1apirequestschemav1requestschemaservicedeleteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## find_binding_for_app_entitlement

Invokes the c1.api.request_schema.v1.RequestSchemaService.FindBindingForAppEntitlement method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.request_schema.v1.RequestSchemaService.FindBindingForAppEntitlement" method="put" path="/api/v1/request_schema_entitlement_binding" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.request_schema.find_binding_for_app_entitlement(request={})

    assert res.request_schema_service_find_binding_for_app_entitlement_response is not None

    # Handle response
    print(res.request_schema_service_find_binding_for_app_entitlement_response)

```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [shared.RequestSchemaServiceFindBindingForAppEntitlementRequest](../../models/shared/requestschemaservicefindbindingforappentitlementrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |
| `retries`                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                 | :heavy_minus_sign:                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                              |

### Response

**[operations.C1APIRequestSchemaV1RequestSchemaServiceFindBindingForAppEntitlementResponse](../../models/operations/c1apirequestschemav1requestschemaservicefindbindingforappentitlementresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Invokes the c1.api.request_schema.v1.RequestSchemaService.Get method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.request_schema.v1.RequestSchemaService.Get" method="get" path="/api/v1/request_schemas/{request_schema_id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.request_schema.get(request={
        "request_schema_id": "<id>",
    })

    assert res.request_schema_service_get_response is not None

    # Handle response
    print(res.request_schema_service_get_response)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.C1APIRequestSchemaV1RequestSchemaServiceGetRequest](../../models/operations/c1apirequestschemav1requestschemaservicegetrequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |

### Response

**[operations.C1APIRequestSchemaV1RequestSchemaServiceGetResponse](../../models/operations/c1apirequestschemav1requestschemaservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_entitlement_binding

Invokes the c1.api.request_schema.v1.RequestSchemaService.RemoveEntitlementBinding method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.request_schema.v1.RequestSchemaService.RemoveEntitlementBinding" method="delete" path="/api/v1/request_schema_entitlement_binding" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.request_schema.remove_entitlement_binding(request={})

    assert res.request_schema_service_remove_entitlement_binding_response is not None

    # Handle response
    print(res.request_schema_service_remove_entitlement_binding_response)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [shared.RequestSchemaServiceRemoveEntitlementBindingRequest](../../models/shared/requestschemaserviceremoveentitlementbindingrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |

### Response

**[operations.C1APIRequestSchemaV1RequestSchemaServiceRemoveEntitlementBindingResponse](../../models/operations/c1apirequestschemav1requestschemaserviceremoveentitlementbindingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Invokes the c1.api.request_schema.v1.RequestSchemaService.Update method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.request_schema.v1.RequestSchemaService.Update" method="post" path="/api/v1/request_schemas/{request_schema_id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.request_schema.update(request={
        "request_schema_service_update_request": {},
        "request_schema_id": "<id>",
    })

    assert res.request_schema_service_update_response is not None

    # Handle response
    print(res.request_schema_service_update_response)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.C1APIRequestSchemaV1RequestSchemaServiceUpdateRequest](../../models/operations/c1apirequestschemav1requestschemaserviceupdaterequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |

### Response

**[operations.C1APIRequestSchemaV1RequestSchemaServiceUpdateResponse](../../models/operations/c1apirequestschemav1requestschemaserviceupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |