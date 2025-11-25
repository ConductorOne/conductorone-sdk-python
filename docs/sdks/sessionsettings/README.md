# SessionSettings
(*session_settings*)

## Overview

### Available Operations

* [get](#get) - Get
* [test_source_ip](#test_source_ip) - Test Source Ip
* [update](#update) - Update

## get

Invokes the c1.api.settings.v1.SessionSettingsService.Get method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.settings.v1.SessionSettingsService.Get" method="get" path="/api/v1/settings/session" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.session_settings.get()

    assert res.get_session_settings_response is not None

    # Handle response
    print(res.get_session_settings_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.C1APISettingsV1SessionSettingsServiceGetResponse](../../models/operations/c1apisettingsv1sessionsettingsservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## test_source_ip

Invokes the c1.api.settings.v1.SessionSettingsService.TestSourceIP method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.settings.v1.SessionSettingsService.TestSourceIP" method="post" path="/api/v1/settings/session/test-source-ip" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.session_settings.test_source_ip()

    assert res.test_source_ip_response is not None

    # Handle response
    print(res.test_source_ip_response)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.TestSourceIPRequest](../../models/shared/testsourceiprequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.C1APISettingsV1SessionSettingsServiceTestSourceIPResponse](../../models/operations/c1apisettingsv1sessionsettingsservicetestsourceipresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Invokes the c1.api.settings.v1.SessionSettingsService.Update method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.settings.v1.SessionSettingsService.Update" method="post" path="/api/v1/settings/session" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.session_settings.update()

    assert res.update_session_settings_response is not None

    # Handle response
    print(res.update_session_settings_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.UpdateSessionSettingsRequest](../../models/shared/updatesessionsettingsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.C1APISettingsV1SessionSettingsServiceUpdateResponse](../../models/operations/c1apisettingsv1sessionsettingsserviceupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |