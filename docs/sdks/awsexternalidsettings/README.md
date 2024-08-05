# AWSExternalIDSettings
(*aws_external_id_settings*)

### Available Operations

* [get](#get) - Get

## get

Invokes the c1.api.settings.v1.AWSExternalIDSettings.Get method.

### Example Usage

```python
from openapi import SDK
from openapi.models import shared

s = SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.aws_external_id_settings.get()

if res.get_aws_external_id_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.C1APISettingsV1AWSExternalIDSettingsGetResponse](../../models/operations/c1apisettingsv1awsexternalidsettingsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
