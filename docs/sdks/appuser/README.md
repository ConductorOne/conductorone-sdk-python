# AppUser

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
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIAppV1AppUserServiceUpdateRequest(
    app_user_service_update_request_input=shared.AppUserServiceUpdateRequestInput(
        app_user=shared.AppUserInput(
            app_user_status=shared.AppUserStatusInput(),
            app_user_type=shared.AppUserAppUserType.APP_USER_TYPE_SERVICE_ACCOUNT,
        ),
        app_user_expand_mask=shared.AppUserExpandMask(
            paths=[
                'deleniti',
            ],
        ),
        update_mask='sapiente',
    ),
    app_user_app_id='amet',
    app_user_id='deserunt',
)

res = s.app_user.update(req)

if res.app_user_service_update_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.C1APIAppV1AppUserServiceUpdateRequest](../../models/operations/c1apiappv1appuserserviceupdaterequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.C1APIAppV1AppUserServiceUpdateResponse](../../models/operations/c1apiappv1appuserserviceupdateresponse.md)**

