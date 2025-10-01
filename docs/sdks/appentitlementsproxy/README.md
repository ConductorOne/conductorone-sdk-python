# AppEntitlementsProxy
(*app_entitlements_proxy*)

## Overview

### Available Operations

* [create](#create) - Create
* [delete](#delete) - Delete
* [get](#get) - Get

## create

Invokes the c1.api.app.v1.AppEntitlementsProxy.Create method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementsProxy.Create" method="post" path="/api/v1/apps/{src_app_id}/{src_app_entitlement_id}/bindings/{dst_app_id}/{dst_app_entitlement_id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlements_proxy.create(request={
        "dst_app_entitlement_id": "<id>",
        "dst_app_id": "<id>",
        "src_app_entitlement_id": "<id>",
        "src_app_id": "<id>",
    })

    assert res.create_app_entitlement_proxy_response is not None

    # Handle response
    print(res.create_app_entitlement_proxy_response)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIAppV1AppEntitlementsProxyCreateRequest](../../models/operations/c1apiappv1appentitlementsproxycreaterequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.C1APIAppV1AppEntitlementsProxyCreateResponse](../../models/operations/c1apiappv1appentitlementsproxycreateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Invokes the c1.api.app.v1.AppEntitlementsProxy.Delete method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementsProxy.Delete" method="delete" path="/api/v1/apps/{src_app_id}/{src_app_entitlement_id}/bindings/{dst_app_id}/{dst_app_entitlement_id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlements_proxy.delete(request={
        "dst_app_entitlement_id": "<id>",
        "dst_app_id": "<id>",
        "src_app_entitlement_id": "<id>",
        "src_app_id": "<id>",
    })

    assert res.delete_app_entitlement_proxy_response is not None

    # Handle response
    print(res.delete_app_entitlement_proxy_response)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIAppV1AppEntitlementsProxyDeleteRequest](../../models/operations/c1apiappv1appentitlementsproxydeleterequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.C1APIAppV1AppEntitlementsProxyDeleteResponse](../../models/operations/c1apiappv1appentitlementsproxydeleteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Invokes the c1.api.app.v1.AppEntitlementsProxy.Get method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppEntitlementsProxy.Get" method="get" path="/api/v1/apps/{src_app_id}/{src_app_entitlement_id}/bindings/{dst_app_id}/{dst_app_entitlement_id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_entitlements_proxy.get(request={
        "dst_app_entitlement_id": "<id>",
        "dst_app_id": "<id>",
        "src_app_entitlement_id": "<id>",
        "src_app_id": "<id>",
    })

    assert res.get_app_entitlement_proxy_response is not None

    # Handle response
    print(res.get_app_entitlement_proxy_response)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.C1APIAppV1AppEntitlementsProxyGetRequest](../../models/operations/c1apiappv1appentitlementsproxygetrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[operations.C1APIAppV1AppEntitlementsProxyGetResponse](../../models/operations/c1apiappv1appentitlementsproxygetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |