# AppEntitlements

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
    app_id='sapiente',
    id='c2ddf7cc-78ca-41ba-928f-c816742cb739',
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
    app_id='aspernatur',
    page_size=187.89,
    page_token='ad',
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
    app_id='natus',
    app_resource_id='sed',
    app_resource_type_id='iste',
    page_size=2223.21,
    page_token='natus',
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
    app_id='laboriosam',
    app_user_id='hic',
    page_size=9025.99,
    page_token='fuga',
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
    app_entitlement_id='in',
    app_id='corporis',
    page_size=6130.64,
    page_token='iure',
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
                    app_id='saepe',
                    entitlement_id='quidem',
                ),
                manual_provision=shared.ManualProvision(
                    instructions='architecto',
                    user_ids=[
                        'ipsa',
                    ],
                ),
            ),
            app_id='reiciendis',
            app_resource_id='est',
            app_resource_type_id='mollitia',
            certify_policy_id='laborum',
            compliance_framework_value_ids=[
                'dolores',
            ],
            description='dolorem',
            display_name='corporis',
            duration_grant='explicabo',
            duration_unset=shared.AppEntitlementDurationUnset(),
            emergency_grant_enabled=False,
            emergency_grant_policy_id='nobis',
            grant_policy_id='enim',
            revoke_policy_id='omnis',
            risk_level_value_id='nemo',
            slug='minima',
        ),
        app_entitlement_expand_mask=shared.AppEntitlementExpandMask(
            paths=[
                'excepturi',
            ],
        ),
        update_mask='accusantium',
    ),
    app_id='iure',
    id='aff1a3a2-fa94-4677-b925-1aa52c3f5ad0',
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

