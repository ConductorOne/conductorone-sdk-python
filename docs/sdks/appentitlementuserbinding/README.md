# AppEntitlementUserBinding
(*app_entitlement_user_binding*)

### Available Operations

* [list_app_users_for_identity_with_grant](#list_app_users_for_identity_with_grant) - List App Users For Identity With Grant

## list_app_users_for_identity_with_grant

Returns a list of app users for the identity in the app. If that app user also has a grant to the entitlement from the request, data about the grant is also returned. It will always return ALL app users for this identity, but only SOME may have grant data.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.app_entitlement_user_binding.list_app_users_for_identity_with_grant(request=operations.C1APIAppV1AppEntitlementUserBindingServiceListAppUsersForIdentityWithGrantRequest(
    app_entitlement_id='<value>',
    app_id='<value>',
    identity_user_id='<value>',
))

if res.list_app_users_for_identity_with_grant_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                    | [operations.C1APIAppV1AppEntitlementUserBindingServiceListAppUsersForIdentityWithGrantRequest](../../models/operations/c1apiappv1appentitlementuserbindingservicelistappusersforidentitywithgrantrequest.md) | :heavy_check_mark:                                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                                   |


### Response

**[operations.C1APIAppV1AppEntitlementUserBindingServiceListAppUsersForIdentityWithGrantResponse](../../models/operations/c1apiappv1appentitlementuserbindingservicelistappusersforidentitywithgrantresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
