# AWSExternalIDSettings
(*aws_external_id_settings*)

### Available Operations

* [get](#get) - Get

## get

Invokes the c1.api.settings.v1.AWSExternalIDSettings.Get method.

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


res = s.aws_external_id_settings.get()

if res.get_aws_external_id_response is not None:
    # handle response
    pass
```


### Response

**[operations.C1APISettingsV1AWSExternalIDSettingsGetResponse](../../models/operations/c1apisettingsv1awsexternalidsettingsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
