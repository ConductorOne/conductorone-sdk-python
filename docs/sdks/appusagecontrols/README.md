# AppUsageControls
(*app_usage_controls*)

## Overview

### Available Operations

* [get](#get) - Get
* [update](#update) - Update

## get

Get usage controls, as an AppUsageControls object which describes some peripheral configuration, for an app.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppUsageControlsService.Get" method="get" path="/api/v1/apps/{app_id}/usage_controls" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_usage_controls.get(request={
        "app_id": "<id>",
    })

    assert res.get_app_usage_controls_response is not None

    # Handle response
    print(res.get_app_usage_controls_response)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIAppV1AppUsageControlsServiceGetRequest](../../models/operations/c1apiappv1appusagecontrolsservicegetrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.C1APIAppV1AppUsageControlsServiceGetResponse](../../models/operations/c1apiappv1appusagecontrolsservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Update usage controls for an app.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppUsageControlsService.Update" method="post" path="/api/v1/apps/{app_id}/usage_controls" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.app_usage_controls.update(request={
        "update_app_usage_controls_request": {},
        "app_id": "<id>",
    })

    assert res.update_app_usage_controls_response is not None

    # Handle response
    print(res.update_app_usage_controls_response)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.C1APIAppV1AppUsageControlsServiceUpdateRequest](../../models/operations/c1apiappv1appusagecontrolsserviceupdaterequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[operations.C1APIAppV1AppUsageControlsServiceUpdateResponse](../../models/operations/c1apiappv1appusagecontrolsserviceupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |