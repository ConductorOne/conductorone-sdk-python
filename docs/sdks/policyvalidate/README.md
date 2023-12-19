# PolicyValidate
(*policy_validate*)

### Available Operations

* [validate_cel](#validate_cel) - Validate Cel

## validate_cel

Validate policies

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

req = shared.ValidatePolicyCELRequest()

res = s.policy_validate.validate_cel(req)

if res.validate_policy_cel_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.ValidatePolicyCELRequest](../../models/shared/validatepolicycelrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.C1APIPolicyV1PolicyValidateValidateCELResponse](../../models/operations/c1apipolicyv1policyvalidatevalidatecelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
