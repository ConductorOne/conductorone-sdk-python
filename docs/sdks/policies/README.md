# Policies
(*policies*)

### Available Operations

* [create](#create) - Create
* [delete](#delete) - Delete
* [get](#get) - Get
* [list](#list) - List
* [update](#update) - Update

## create

Create a policy.

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

req = shared.CreatePolicyRequest(
    policy_steps={
        'key': shared.PolicySteps(
            steps=[
                shared.PolicyStep(
                    accept=shared.Accept(),
                    approval=shared.Approval(
                        app_group_approval=shared.AppGroupApproval(
                            fallback_user_ids=[
                                'string',
                            ],
                        ),
                        app_owner_approval=shared.AppOwnerApproval(),
                        entitlement_owner_approval=shared.EntitlementOwnerApproval(
                            fallback_user_ids=[
                                'string',
                            ],
                        ),
                        expression_approval=shared.ExpressionApproval(
                            assigned_user_ids=[
                                'string',
                            ],
                            expressions=[
                                'string',
                            ],
                            fallback_user_ids=[
                                'string',
                            ],
                        ),
                        manager_approval=shared.ManagerApproval(
                            assigned_user_ids=[
                                'string',
                            ],
                            fallback_user_ids=[
                                'string',
                            ],
                        ),
                        self_approval=shared.SelfApproval(
                            assigned_user_ids=[
                                'string',
                            ],
                            fallback_user_ids=[
                                'string',
                            ],
                        ),
                        user_approval=shared.UserApproval(
                            user_ids=[
                                'string',
                            ],
                        ),
                    ),
                    provision=shared.Provision(
                        provision_policy=shared.ProvisionPolicy(
                            connector_provision=shared.ConnectorProvision(),
                            delegated_provision=shared.DelegatedProvision(),
                            manual_provision=shared.ManualProvision(
                                user_ids=[
                                    'string',
                                ],
                            ),
                        ),
                        provision_target=shared.ProvisionTarget(),
                    ),
                    reject=shared.Reject(),
                ),
            ],
        ),
    },
    post_actions=[
        shared.PolicyPostActions(),
    ],
)

res = s.policies.create(req)

if res.create_policy_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.CreatePolicyRequest](../../models/shared/createpolicyrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.C1APIPolicyV1PoliciesCreateResponse](../../models/operations/c1apipolicyv1policiescreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete

Delete a policy by ID.

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

req = operations.C1APIPolicyV1PoliciesDeleteRequest(
    delete_policy_request=shared.DeletePolicyRequest(),
    id='<ID>',
)

res = s.policies.delete(req)

if res.delete_policy_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.C1APIPolicyV1PoliciesDeleteRequest](../../models/operations/c1apipolicyv1policiesdeleterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.C1APIPolicyV1PoliciesDeleteResponse](../../models/operations/c1apipolicyv1policiesdeleteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get a policy by ID.

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

req = operations.C1APIPolicyV1PoliciesGetRequest(
    id='<ID>',
)

res = s.policies.get(req)

if res.get_policy_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.C1APIPolicyV1PoliciesGetRequest](../../models/operations/c1apipolicyv1policiesgetrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.C1APIPolicyV1PoliciesGetResponse](../../models/operations/c1apipolicyv1policiesgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list

List policies.

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

req = operations.C1APIPolicyV1PoliciesListRequest()

res = s.policies.list(req)

if res.list_policy_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.C1APIPolicyV1PoliciesListRequest](../../models/operations/c1apipolicyv1policieslistrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.C1APIPolicyV1PoliciesListResponse](../../models/operations/c1apipolicyv1policieslistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update a policy by providing a policy object and an update mask.

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

req = operations.C1APIPolicyV1PoliciesUpdateRequest(
    update_policy_request=shared.UpdatePolicyRequest(
        policy=shared.PolicyInput(
            policy_steps={
                'key': shared.PolicySteps(
                    steps=[
                        shared.PolicyStep(
                            accept=shared.Accept(),
                            approval=shared.Approval(
                                app_group_approval=shared.AppGroupApproval(
                                    fallback_user_ids=[
                                        'string',
                                    ],
                                ),
                                app_owner_approval=shared.AppOwnerApproval(),
                                entitlement_owner_approval=shared.EntitlementOwnerApproval(
                                    fallback_user_ids=[
                                        'string',
                                    ],
                                ),
                                expression_approval=shared.ExpressionApproval(
                                    assigned_user_ids=[
                                        'string',
                                    ],
                                    expressions=[
                                        'string',
                                    ],
                                    fallback_user_ids=[
                                        'string',
                                    ],
                                ),
                                manager_approval=shared.ManagerApproval(
                                    assigned_user_ids=[
                                        'string',
                                    ],
                                    fallback_user_ids=[
                                        'string',
                                    ],
                                ),
                                self_approval=shared.SelfApproval(
                                    assigned_user_ids=[
                                        'string',
                                    ],
                                    fallback_user_ids=[
                                        'string',
                                    ],
                                ),
                                user_approval=shared.UserApproval(
                                    user_ids=[
                                        'string',
                                    ],
                                ),
                            ),
                            provision=shared.Provision(
                                provision_policy=shared.ProvisionPolicy(
                                    connector_provision=shared.ConnectorProvision(),
                                    delegated_provision=shared.DelegatedProvision(),
                                    manual_provision=shared.ManualProvision(
                                        user_ids=[
                                            'string',
                                        ],
                                    ),
                                ),
                                provision_target=shared.ProvisionTarget(),
                            ),
                            reject=shared.Reject(),
                        ),
                    ],
                ),
            },
            post_actions=[
                shared.PolicyPostActions(),
            ],
            rules=[
                shared.Rule(),
            ],
        ),
    ),
    id='<ID>',
)

res = s.policies.update(req)

if res.update_policy_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.C1APIPolicyV1PoliciesUpdateRequest](../../models/operations/c1apipolicyv1policiesupdaterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.C1APIPolicyV1PoliciesUpdateResponse](../../models/operations/c1apipolicyv1policiesupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
