# SessionSettings
(*session_settings*)

### Available Operations

* [get](#get) - Get
* [update](#update) - Update

## get

Invokes the c1.api.settings.v1.SessionSettingsService.Get method.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)


res = s.session_settings.get()

if res.get_session_settings_response is not None:
    # handle response
    pass

```


### Response

**[operations.C1APISettingsV1SessionSettingsServiceGetResponse](../../models/operations/c1apisettingsv1sessionsettingsservicegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Invokes the c1.api.settings.v1.SessionSettingsService.Update method.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = shared.UpdateSessionSettingsRequest()

res = s.session_settings.update(req)

if res.update_session_settings_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.UpdateSessionSettingsRequest](../../models/shared/updatesessionsettingsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.C1APISettingsV1SessionSettingsServiceUpdateResponse](../../models/operations/c1apisettingsv1sessionsettingsserviceupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
