# AppUser
(*app_user*)

### Available Operations

* [update](#update) - Update

## update

Update an app user by ID. Only the fields specified in the update mask are updated.
 Currently, only the appUserType, and identityUserId fields can be updated.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIAppV1AppUserServiceUpdateRequest(
    app_user_app_id='<value>',
    app_user_id='<value>',
)

res = s.app_user.update(req)

if res.app_user_service_update_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.C1APIAppV1AppUserServiceUpdateRequest](../../models/operations/c1apiappv1appuserserviceupdaterequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.C1APIAppV1AppUserServiceUpdateResponse](../../models/operations/c1apiappv1appuserserviceupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
