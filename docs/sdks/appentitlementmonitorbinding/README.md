# AppEntitlementMonitorBinding
(*app_entitlement_monitor_binding*)

## Overview

### Available Operations

* [create_app_entitlement_monitor_binding](#create_app_entitlement_monitor_binding) - Create App Entitlement Monitor Binding
* [delete_app_entitlement_monitor_binding](#delete_app_entitlement_monitor_binding) - Delete App Entitlement Monitor Binding
* [get_app_entitlement_monitor_binding](#get_app_entitlement_monitor_binding) - Get App Entitlement Monitor Binding

## create_app_entitlement_monitor_binding

Invokes the c1.api.accessconflict.v1.AppEntitlementMonitorBindingService.CreateAppEntitlementMonitorBinding method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.accessconflict.v1.AppEntitlementMonitorBindingService.CreateAppEntitlementMonitorBinding" method="post" path="/api/v1/appentitlementmonitorbinding" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlement_monitor_binding.create_app_entitlement_monitor_binding()

    assert res.app_entitlement_monitor_binding is not None

    # Handle response
    print(res.app_entitlement_monitor_binding)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [shared.CreateAppEntitlementMonitorBindingRequest](../../models/shared/createappentitlementmonitorbindingrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.C1APIAccessconflictV1AppEntitlementMonitorBindingServiceCreateAppEntitlementMonitorBindingResponse](../../models/operations/c1apiaccessconflictv1appentitlementmonitorbindingservicecreateappentitlementmonitorbindingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_app_entitlement_monitor_binding

Invokes the c1.api.accessconflict.v1.AppEntitlementMonitorBindingService.DeleteAppEntitlementMonitorBinding method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.accessconflict.v1.AppEntitlementMonitorBindingService.DeleteAppEntitlementMonitorBinding" method="delete" path="/api/v1/appentitlementmonitorbinding" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlement_monitor_binding.delete_app_entitlement_monitor_binding()

    assert res.delete_app_entitlement_monitor_binding_response is not None

    # Handle response
    print(res.delete_app_entitlement_monitor_binding_response)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [shared.DeleteAppEntitlementMonitorBindingRequest](../../models/shared/deleteappentitlementmonitorbindingrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.C1APIAccessconflictV1AppEntitlementMonitorBindingServiceDeleteAppEntitlementMonitorBindingResponse](../../models/operations/c1apiaccessconflictv1appentitlementmonitorbindingservicedeleteappentitlementmonitorbindingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_app_entitlement_monitor_binding

Invokes the c1.api.accessconflict.v1.AppEntitlementMonitorBindingService.GetAppEntitlementMonitorBinding method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.accessconflict.v1.AppEntitlementMonitorBindingService.GetAppEntitlementMonitorBinding" method="post" path="/api/v1/appentitlementmonitorbinding/get" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlement_monitor_binding.get_app_entitlement_monitor_binding()

    assert res.app_entitlement_monitor_binding is not None

    # Handle response
    print(res.app_entitlement_monitor_binding)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [shared.GetAppEntitlementMonitorBindingRequest](../../models/shared/getappentitlementmonitorbindingrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.C1APIAccessconflictV1AppEntitlementMonitorBindingServiceGetAppEntitlementMonitorBindingResponse](../../models/operations/c1apiaccessconflictv1appentitlementmonitorbindingservicegetappentitlementmonitorbindingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |