# PersonalClient
(*personal_client*)

### Available Operations

* [create](#create) - Create

## create

Create creates a new PersonalClient object for the current User.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = shared.PersonalClientServiceCreateRequest(
    allow_source_cidr=[
        'string',
    ],
    scoped_roles=[
        'string',
    ],
)

res = s.personal_client.create(req)

if res.personal_client_service_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [shared.PersonalClientServiceCreateRequest](../../models/shared/personalclientservicecreaterequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.C1APIIamV1PersonalClientServiceCreateResponse](../../models/operations/c1apiiamv1personalclientservicecreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
