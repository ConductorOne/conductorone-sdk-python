# policies

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
        bearer_auth="",
        oauth="",
    ),
)

req = shared.CreatePolicyRequestInput(
    description='nisi',
    display_name='fugit',
    policy_steps={
        "sapiente": shared.PolicyStepsInput(
            steps=[
                shared.PolicyStepInput(
                    approval=shared.ApprovalInput(
                        app_group_approval=shared.AppGroupApprovalInput(),
                        app_owner_approval=shared.AppOwnerApprovalInput(),
                        entitlement_owner_approval=shared.EntitlementOwnerApprovalInput(),
                        manager_approval=shared.ManagerApprovalInput(),
                        self_approval=shared.SelfApprovalInput(),
                        user_approval=shared.UserApprovalInput(),
                    ),
                    provision=shared.Provision(
                        provision_policy=shared.ProvisionPolicy(
                            connector_provision=shared.ConnectorProvision(),
                            delegated_provision=shared.DelegatedProvision(
                                app_id='consequuntur',
                                entitlement_id='ratione',
                            ),
                            manual_provision=shared.ManualProvision(
                                instructions='explicabo',
                                user_ids=[
                                    'saepe',
                                ],
                            ),
                        ),
                        provision_target=shared.ProvisionTarget(
                            app_entitlement_id='occaecati',
                            app_id='atque',
                            app_user_id='et',
                            grant_duration='esse',
                        ),
                        assigned=False,
                    ),
                ),
            ],
        ),
    },
    policy_type=shared.CreatePolicyRequestPolicyType.POLICY_TYPE_PROVISION,
    post_actions=[
        shared.PolicyPostActions(
            certify_remediate_immediately=False,
        ),
    ],
    reassign_tasks_to_delegates=False,
)

res = s.policies.create(req)

if res.create_policy_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.CreatePolicyRequestInput](../../models/shared/createpolicyrequestinput.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.C1APIPolicyV1PoliciesCreateResponse](../../models/operations/c1apipolicyv1policiescreateresponse.md)**


## delete

Delete a policy by ID.

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

req = operations.C1APIPolicyV1PoliciesDeleteRequest(
    delete_policy_request=shared.DeletePolicyRequest(),
    id='e17cbe61-e6b7-4b95-bc0a-b3c20c4f3789',
)

res = s.policies.delete(req)

if res.delete_policy_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.C1APIPolicyV1PoliciesDeleteRequest](../../models/operations/c1apipolicyv1policiesdeleterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.C1APIPolicyV1PoliciesDeleteResponse](../../models/operations/c1apipolicyv1policiesdeleteresponse.md)**


## get

Get a policy by ID.

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

req = operations.C1APIPolicyV1PoliciesGetRequest(
    id='fd871f99-dd2e-4fd1-a1aa-6f1e674bdb04',
)

res = s.policies.get(req)

if res.get_policy_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.C1APIPolicyV1PoliciesGetRequest](../../models/operations/c1apipolicyv1policiesgetrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.C1APIPolicyV1PoliciesGetResponse](../../models/operations/c1apipolicyv1policiesgetresponse.md)**


## list

List policies.

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

req = operations.C1APIPolicyV1PoliciesListRequest(
    page_size=9589.83,
    page_token='dicta',
)

res = s.policies.list(req)

if res.list_policy_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.C1APIPolicyV1PoliciesListRequest](../../models/operations/c1apipolicyv1policieslistrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.C1APIPolicyV1PoliciesListResponse](../../models/operations/c1apipolicyv1policieslistresponse.md)**


## update

Update a policy by providing a policy object and an update mask.

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

req = operations.C1APIPolicyV1PoliciesUpdateRequest(
    update_policy_request_input=shared.UpdatePolicyRequestInput(
        policy=shared.PolicyInput(
            description='ullam',
            display_name='reprehenderit',
            policy_steps={
                "ullam": shared.PolicyStepsInput(
                    steps=[
                        shared.PolicyStepInput(
                            approval=shared.ApprovalInput(
                                app_group_approval=shared.AppGroupApprovalInput(),
                                app_owner_approval=shared.AppOwnerApprovalInput(),
                                entitlement_owner_approval=shared.EntitlementOwnerApprovalInput(),
                                manager_approval=shared.ManagerApprovalInput(),
                                self_approval=shared.SelfApprovalInput(),
                                user_approval=shared.UserApprovalInput(),
                            ),
                            provision=shared.Provision(
                                provision_policy=shared.ProvisionPolicy(
                                    connector_provision=shared.ConnectorProvision(),
                                    delegated_provision=shared.DelegatedProvision(
                                        app_id='nisi',
                                        entitlement_id='aut',
                                    ),
                                    manual_provision=shared.ManualProvision(
                                        instructions='voluptatum',
                                        user_ids=[
                                            'qui',
                                        ],
                                    ),
                                ),
                                provision_target=shared.ProvisionTarget(
                                    app_entitlement_id='quibusdam',
                                    app_id='ex',
                                    app_user_id='deleniti',
                                    grant_duration='itaque',
                                ),
                                assigned=False,
                            ),
                        ),
                    ],
                ),
            },
            policy_type=shared.PolicyPolicyType.POLICY_TYPE_ACCESS_REQUEST,
            post_actions=[
                shared.PolicyPostActions(
                    certify_remediate_immediately=False,
                ),
            ],
            reassign_tasks_to_delegates=False,
        ),
        update_mask='architecto',
    ),
    id='9f1d1705-1339-4d08-886a-1840394c2607',
)

res = s.policies.update(req)

if res.update_policy_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.C1APIPolicyV1PoliciesUpdateRequest](../../models/operations/c1apipolicyv1policiesupdaterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.C1APIPolicyV1PoliciesUpdateResponse](../../models/operations/c1apipolicyv1policiesupdateresponse.md)**

