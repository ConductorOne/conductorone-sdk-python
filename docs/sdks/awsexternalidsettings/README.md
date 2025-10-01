# AWSExternalIDSettings
(*aws_external_id_settings*)

## Overview

### Available Operations

* [get](#get) - Get

## get

Invokes the c1.api.settings.v1.AWSExternalIDSettings.Get method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.settings.v1.AWSExternalIDSettings.Get" method="get" path="/api/v1/settings/aws-external-id" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.aws_external_id_settings.get()

    assert res.get_aws_external_id_response is not None

    # Handle response
    print(res.get_aws_external_id_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.C1APISettingsV1AWSExternalIDSettingsGetResponse](../../models/operations/c1apisettingsv1awsexternalidsettingsgetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |