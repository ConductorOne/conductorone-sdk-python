# AccessConflict
(*access_conflict*)

## Overview

### Available Operations

* [create_monitor](#create_monitor) - Create Monitor
* [delete_monitor](#delete_monitor) - Delete Monitor
* [get_monitor](#get_monitor) - Get Monitor
* [update_monitor](#update_monitor) - Update Monitor

## create_monitor

Invokes the c1.api.accessconflict.v1.AccessConflictService.CreateMonitor method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.accessconflict.v1.AccessConflictService.CreateMonitor" method="post" path="/api/v1/accessconflict" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.access_conflict.create_monitor()

    assert res.conflict_monitor is not None

    # Handle response
    print(res.conflict_monitor)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.ConflictMonitorCreateRequest](../../models/shared/conflictmonitorcreaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.C1APIAccessconflictV1AccessConflictServiceCreateMonitorResponse](../../models/operations/c1apiaccessconflictv1accessconflictservicecreatemonitorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_monitor

Invokes the c1.api.accessconflict.v1.AccessConflictService.DeleteMonitor method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.accessconflict.v1.AccessConflictService.DeleteMonitor" method="delete" path="/api/v1/accessconflict/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.access_conflict.delete_monitor(request={
        "id": "<id>",
    })

    assert res.conflict_monitor_delete_response is not None

    # Handle response
    print(res.conflict_monitor_delete_response)

```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.C1APIAccessconflictV1AccessConflictServiceDeleteMonitorRequest](../../models/operations/c1apiaccessconflictv1accessconflictservicedeletemonitorrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |
| `retries`                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                    |

### Response

**[operations.C1APIAccessconflictV1AccessConflictServiceDeleteMonitorResponse](../../models/operations/c1apiaccessconflictv1accessconflictservicedeletemonitorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_monitor

Invokes the c1.api.accessconflict.v1.AccessConflictService.GetMonitor method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.accessconflict.v1.AccessConflictService.GetMonitor" method="get" path="/api/v1/accessconflict/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.access_conflict.get_monitor(request={
        "id": "<id>",
    })

    assert res.conflict_monitor is not None

    # Handle response
    print(res.conflict_monitor)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                        | [operations.C1APIAccessconflictV1AccessConflictServiceGetMonitorRequest](../../models/operations/c1apiaccessconflictv1accessconflictservicegetmonitorrequest.md) | :heavy_check_mark:                                                                                                                                               | The request object to use for the request.                                                                                                                       |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |

### Response

**[operations.C1APIAccessconflictV1AccessConflictServiceGetMonitorResponse](../../models/operations/c1apiaccessconflictv1accessconflictservicegetmonitorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_monitor

Invokes the c1.api.accessconflict.v1.AccessConflictService.UpdateMonitor method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.accessconflict.v1.AccessConflictService.UpdateMonitor" method="post" path="/api/v1/accessconflict/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.access_conflict.update_monitor(request={
        "id": "<id>",
    })

    assert res.conflict_monitor is not None

    # Handle response
    print(res.conflict_monitor)

```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.C1APIAccessconflictV1AccessConflictServiceUpdateMonitorRequest](../../models/operations/c1apiaccessconflictv1accessconflictserviceupdatemonitorrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |
| `retries`                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                    |

### Response

**[operations.C1APIAccessconflictV1AccessConflictServiceUpdateMonitorResponse](../../models/operations/c1apiaccessconflictv1accessconflictserviceupdatemonitorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |