# app_usage_controls

### Available Operations

* [get](#get) - Get
* [update](#update) - Update

## get

Get usage controls, as an AppUsageControls object which describes some peripheral configuration, for an app.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIAppV1AppUsageControlsServiceGetRequest(
    app_id='magni',
)

res = s.app_usage_controls.get(req)

if res.get_app_usage_controls_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIAppV1AppUsageControlsServiceGetRequest](../../models/operations/c1apiappv1appusagecontrolsservicegetrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.C1APIAppV1AppUsageControlsServiceGetResponse](../../models/operations/c1apiappv1appusagecontrolsservicegetresponse.md)**


## update

Update usage controls for an app.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIAppV1AppUsageControlsServiceUpdateRequest(
    update_app_usage_controls_request=shared.UpdateAppUsageControlsRequest(
        app_usage_controls=shared.AppUsageControls(
            app_id='sunt',
            notify=False,
            notify_after_days=7790.51,
            revoke=False,
            revoke_after_days=8480.09,
        ),
        update_mask='pariatur',
    ),
    app_id='maxime',
)

res = s.app_usage_controls.update(req)

if res.update_app_usage_controls_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.C1APIAppV1AppUsageControlsServiceUpdateRequest](../../models/operations/c1apiappv1appusagecontrolsserviceupdaterequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.C1APIAppV1AppUsageControlsServiceUpdateResponse](../../models/operations/c1apiappv1appusagecontrolsserviceupdateresponse.md)**

