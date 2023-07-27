# app_entitlements

### Available Operations

* [get](#get) - Get
* [list](#list) - List
* [list_for_app_resource](#list_for_app_resource) - List For App Resource
* [list_for_app_user](#list_for_app_user) - List For App User
* [list_groups](#list_groups) - List Groups
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
        oauth="",
    ),
)

req = operations.C1APIAppV1AppEntitlementsGetRequest(
    app_id='iste',
    id='396fea75-96eb-410f-aaa2-352c5955907a',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1AppEntitlementsListRequest(
    app_id='doloribus',
    page_size=9589.5,
    page_token='architecto',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1AppEntitlementsListForAppResourceRequest(
    app_id='mollitia',
    app_resource_id='dolorem',
    app_resource_type_id='culpa',
    page_size=1613.09,
    page_token='repellat',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1AppEntitlementsListForAppUserRequest(
    app_id='mollitia',
    app_user_id='occaecati',
    page_size=2532.91,
    page_token='commodi',
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


## list_groups

List app groups associated with an app entitlement.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIAppV1AppEntitlementsListGroupsRequest(
    app_entitlement_id='quam',
    app_id='molestiae',
    page_size=2444.25,
    page_token='error',
)

res = s.app_entitlements.list_groups(req)

if res.list_app_entitlement_groups_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.C1APIAppV1AppEntitlementsListGroupsRequest](../../models/operations/c1apiappv1appentitlementslistgroupsrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.C1APIAppV1AppEntitlementsListGroupsResponse](../../models/operations/c1apiappv1appentitlementslistgroupsresponse.md)**


## list_users

List the users, as AppEntitlementUsers objects, of an app entitlement.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIAppV1AppEntitlementsListUsersRequest(
    app_entitlement_id='quia',
    app_id='quis',
    page_size=1103.75,
    page_token='laborum',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1AppEntitlementsUpdateRequest(
    update_app_entitlement_request_input=shared.UpdateAppEntitlementRequestInput(
        app_entitlement=shared.AppEntitlementInput(
            provision_policy=shared.ProvisionPolicy(
                connector_provision=shared.ConnectorProvision(),
                delegated_provision=shared.DelegatedProvision(
                    app_id='animi',
                    entitlement_id='enim',
                ),
                manual_provision=shared.ManualProvision(
                    instructions='odit',
                    user_ids=[
                        'sequi',
                        'tenetur',
                        'ipsam',
                        'id',
                    ],
                ),
            ),
            app_id='possimus',
            app_resource_id='aut',
            app_resource_type_id='quasi',
            certify_policy_id='error',
            compliance_framework_value_ids=[
                'laborum',
                'quasi',
                'reiciendis',
                'voluptatibus',
            ],
            description='vero',
            display_name='nihil',
            duration_grant='praesentium',
            duration_unset=shared.AppEntitlementDurationUnset(),
            emergency_grant_enabled=False,
            emergency_grant_policy_id='voluptatibus',
            grant_policy_id='ipsa',
            revoke_policy_id='omnis',
            risk_level_value_id='voluptate',
            slug='cum',
        ),
        app_entitlement_expand_mask=shared.AppEntitlementExpandMask(
            paths=[
                'doloremque',
            ],
        ),
        update_mask='reprehenderit',
    ),
    app_id='ut',
    id='f15471b5-e6e1-43b9-9d48-8e1e91e450ad',
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

