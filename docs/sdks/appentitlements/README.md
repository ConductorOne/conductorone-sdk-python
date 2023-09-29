# AppEntitlements
(*app_entitlements*)

### Available Operations

* [get](#get) - Get
* [list](#list) - List
* [list_for_app_resource](#list_for_app_resource) - List For App Resource
* [list_for_app_user](#list_for_app_user) - List For App User
* [list_users](#list_users) - List Users
* [update](#update) - Update

## get

Get an app entitlement by ID.

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

req = operations.C1APIAppV1AppEntitlementsGetRequest(
    app_id='Group Cambridgeshire',
    id='<ID>',
)

res = s.app_entitlements.get(req)

if res.get_app_entitlement_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.C1APIAppV1AppEntitlementsGetRequest](../../models/operations/c1apiappv1appentitlementsgetrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.C1APIAppV1AppEntitlementsGetResponse](../../models/operations/c1apiappv1appentitlementsgetresponse.md)**


## list

List app entitlements associated with an app.

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

req = operations.C1APIAppV1AppEntitlementsListRequest(
    app_id='Bronze Architect',
    page_size=9628.76,
    page_token='female',
)

res = s.app_entitlements.list(req)

if res.list_app_entitlements_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.C1APIAppV1AppEntitlementsListRequest](../../models/operations/c1apiappv1appentitlementslistrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.C1APIAppV1AppEntitlementsListResponse](../../models/operations/c1apiappv1appentitlementslistresponse.md)**


## list_for_app_resource

List app entitlements associated with an app resource.

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

req = operations.C1APIAppV1AppEntitlementsListForAppResourceRequest(
    app_id='SDD convergence',
    app_resource_id='quis whether',
    app_resource_type_id='Non',
    page_size=7654.99,
    page_token='Fitness Dollar Licensed',
)

res = s.app_entitlements.list_for_app_resource(req)

if res.list_app_entitlements_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.C1APIAppV1AppEntitlementsListForAppResourceRequest](../../models/operations/c1apiappv1appentitlementslistforappresourcerequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |


### Response

**[operations.C1APIAppV1AppEntitlementsListForAppResourceResponse](../../models/operations/c1apiappv1appentitlementslistforappresourceresponse.md)**


## list_for_app_user

List app entitlements associated with an app user.

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

req = operations.C1APIAppV1AppEntitlementsListForAppUserRequest(
    app_id='Gardena payment Mountain',
    app_user_id='Cruiser',
    page_size=7218.97,
    page_token='Franc Novato',
)

res = s.app_entitlements.list_for_app_user(req)

if res.list_app_entitlements_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.C1APIAppV1AppEntitlementsListForAppUserRequest](../../models/operations/c1apiappv1appentitlementslistforappuserrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.C1APIAppV1AppEntitlementsListForAppUserResponse](../../models/operations/c1apiappv1appentitlementslistforappuserresponse.md)**


## list_users

List the users, as AppEntitlementUsers objects, of an app entitlement.

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

req = operations.C1APIAppV1AppEntitlementsListUsersRequest(
    app_entitlement_id='yellow payment',
    app_id='why Electric',
    page_size=782.05,
    page_token='Metal rack whether',
)

res = s.app_entitlements.list_users(req)

if res.list_app_entitlement_users_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.C1APIAppV1AppEntitlementsListUsersRequest](../../models/operations/c1apiappv1appentitlementslistusersrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.C1APIAppV1AppEntitlementsListUsersResponse](../../models/operations/c1apiappv1appentitlementslistusersresponse.md)**


## update

Update an app entitlement by ID.

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

req = operations.C1APIAppV1AppEntitlementsUpdateRequest(
    update_app_entitlement_request_input=shared.UpdateAppEntitlementRequestInput(
        app_entitlement=shared.AppEntitlementInput(
            provision_policy=shared.ProvisionPolicy(
                connector_provision=shared.ConnectorProvision(),
                delegated_provision=shared.DelegatedProvision(
                    app_id='South complexity',
                    entitlement_id='Tempe Ruble ADP',
                ),
                manual_provision=shared.ManualProvision(
                    instructions='Holmium',
                    user_ids=[
                        'Country',
                    ],
                ),
            ),
            app_id='Albany Southeast Computer',
            app_resource_id='Towels',
            app_resource_type_id='invoice Northeast orange',
            certify_policy_id='Response HTTP',
            compliance_framework_value_ids=[
                'Hybrid',
            ],
            description='Stand-alone encompassing middleware',
            display_name='index Iran after',
            duration_grant='through',
            duration_unset=shared.AppEntitlementDurationUnset(),
            emergency_grant_enabled=False,
            emergency_grant_policy_id='Optimized',
            grant_policy_id='fugit fuchsia',
            revoke_policy_id='sternly meter experiences',
            risk_level_value_id='as Electric than',
            slug='Benz Representative',
        ),
        app_entitlement_expand_mask=shared.AppEntitlementExpandMask(
            paths=[
                'wireless',
            ],
        ),
        update_mask='index',
    ),
    app_id='Funk Small system',
    id='<ID>',
)

res = s.app_entitlements.update(req)

if res.update_app_entitlement_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.C1APIAppV1AppEntitlementsUpdateRequest](../../models/operations/c1apiappv1appentitlementsupdaterequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.C1APIAppV1AppEntitlementsUpdateResponse](../../models/operations/c1apiappv1appentitlementsupdateresponse.md)**

