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
        oauth="",
    ),
)

req = shared.CreatePolicyRequestInput(
    description='consequatur',
    display_name='minus',
    policy_steps={
        "sapiente": shared.PolicyStepsInput(
            steps=[
                shared.PolicyStepInput(
                    approval=shared.ApprovalInput(
                        app_group_approval=shared.AppGroupApproval1(),
                        app_owner_approval=shared.AppOwnerApproval1(),
                        entitlement_owner_approval=shared.EntitlementOwnerApproval1(),
                        manager_approval=shared.ManagerApproval1(),
                        self_approval=shared.SelfApproval1(),
                        user_approval=shared.UserApproval1(),
                    ),
                    provision=shared.Provision(
                        provision_policy=shared.ProvisionPolicy(
                            connector_provision=shared.ConnectorProvision(),
                            delegated_provision=shared.DelegatedProvision(
                                app_id='esse',
                                entitlement_id='blanditiis',
                            ),
                            manual_provision=shared.ManualProvision(
                                instructions='provident',
                                user_ids=[
                                    'nulla',
                                    'quas',
                                    'esse',
                                    'quasi',
                                ],
                            ),
                        ),
                        assigned=False,
                    ),
                ),
            ],
        ),
        "a": shared.PolicyStepsInput(
            steps=[
                shared.PolicyStepInput(
                    approval=shared.ApprovalInput(
                        app_group_approval=shared.AppGroupApproval1(),
                        app_owner_approval=shared.AppOwnerApproval1(),
                        entitlement_owner_approval=shared.EntitlementOwnerApproval1(),
                        manager_approval=shared.ManagerApproval1(),
                        self_approval=shared.SelfApproval1(),
                        user_approval=shared.UserApproval1(),
                    ),
                    provision=shared.Provision(
                        provision_policy=shared.ProvisionPolicy(
                            connector_provision=shared.ConnectorProvision(),
                            delegated_provision=shared.DelegatedProvision(
                                app_id='sint',
                                entitlement_id='pariatur',
                            ),
                            manual_provision=shared.ManualProvision(
                                instructions='possimus',
                                user_ids=[
                                    'eveniet',
                                ],
                            ),
                        ),
                        assigned=False,
                    ),
                ),
                shared.PolicyStepInput(
                    approval=shared.ApprovalInput(
                        app_group_approval=shared.AppGroupApproval1(),
                        app_owner_approval=shared.AppOwnerApproval1(),
                        entitlement_owner_approval=shared.EntitlementOwnerApproval1(),
                        manager_approval=shared.ManagerApproval1(),
                        self_approval=shared.SelfApproval1(),
                        user_approval=shared.UserApproval1(),
                    ),
                    provision=shared.Provision(
                        provision_policy=shared.ProvisionPolicy(
                            connector_provision=shared.ConnectorProvision(),
                            delegated_provision=shared.DelegatedProvision(
                                app_id='asperiores',
                                entitlement_id='facere',
                            ),
                            manual_provision=shared.ManualProvision(
                                instructions='veritatis',
                                user_ids=[
                                    'quasi',
                                ],
                            ),
                        ),
                        assigned=False,
                    ),
                ),
                shared.PolicyStepInput(
                    approval=shared.ApprovalInput(
                        app_group_approval=shared.AppGroupApproval1(),
                        app_owner_approval=shared.AppOwnerApproval1(),
                        entitlement_owner_approval=shared.EntitlementOwnerApproval1(),
                        manager_approval=shared.ManagerApproval1(),
                        self_approval=shared.SelfApproval1(),
                        user_approval=shared.UserApproval1(),
                    ),
                    provision=shared.Provision(
                        provision_policy=shared.ProvisionPolicy(
                            connector_provision=shared.ConnectorProvision(),
                            delegated_provision=shared.DelegatedProvision(
                                app_id='similique',
                                entitlement_id='culpa',
                            ),
                            manual_provision=shared.ManualProvision(
                                instructions='aliquid',
                                user_ids=[
                                    'quae',
                                    'earum',
                                    'vel',
                                    'in',
                                ],
                            ),
                        ),
                        assigned=False,
                    ),
                ),
            ],
        ),
    },
    policy_type=shared.CreatePolicyRequestPolicyType.POLICY_TYPE_GRANT,
    post_actions=[
        shared.PolicyPostActions(
            certify_remediate_immediately=False,
        ),
        shared.PolicyPostActions(
            certify_remediate_immediately=False,
        ),
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
        oauth="",
    ),
)

req = operations.C1APIPolicyV1PoliciesDeleteRequest(
    delete_policy_request=shared.DeletePolicyRequest(),
    id='db04f157-5608-42d6-8ea1-9f1d17051339',
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
        oauth="",
    ),
)

req = operations.C1APIPolicyV1PoliciesGetRequest(
    id='d08086a1-8403-494c-a607-1f93f5f0642d',
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
        oauth="",
    ),
)

req = operations.C1APIPolicyV1PoliciesListRequest(
    page_size=6387.62,
    page_token='maxime',
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
        oauth="",
    ),
)

req = operations.C1APIPolicyV1PoliciesUpdateRequest(
    update_policy_request_input=shared.UpdatePolicyRequestInput(
        policy=shared.PolicyInput(
            description='dignissimos',
            display_name='officia',
            policy_steps={
                "nemo": shared.PolicyStepsInput(
                    steps=[
                        shared.PolicyStepInput(
                            approval=shared.ApprovalInput(
                                app_group_approval=shared.AppGroupApproval1(),
                                app_owner_approval=shared.AppOwnerApproval1(),
                                entitlement_owner_approval=shared.EntitlementOwnerApproval1(),
                                manager_approval=shared.ManagerApproval1(),
                                self_approval=shared.SelfApproval1(),
                                user_approval=shared.UserApproval1(),
                            ),
                            provision=shared.Provision(
                                provision_policy=shared.ProvisionPolicy(
                                    connector_provision=shared.ConnectorProvision(),
                                    delegated_provision=shared.DelegatedProvision(
                                        app_id='quaerat',
                                        entitlement_id='porro',
                                    ),
                                    manual_provision=shared.ManualProvision(
                                        instructions='quod',
                                        user_ids=[
                                            'ab',
                                            'adipisci',
                                        ],
                                    ),
                                ),
                                assigned=False,
                            ),
                        ),
                    ],
                ),
                "fuga": shared.PolicyStepsInput(
                    steps=[
                        shared.PolicyStepInput(
                            approval=shared.ApprovalInput(
                                app_group_approval=shared.AppGroupApproval1(),
                                app_owner_approval=shared.AppOwnerApproval1(),
                                entitlement_owner_approval=shared.EntitlementOwnerApproval1(),
                                manager_approval=shared.ManagerApproval1(),
                                self_approval=shared.SelfApproval1(),
                                user_approval=shared.UserApproval1(),
                            ),
                            provision=shared.Provision(
                                provision_policy=shared.ProvisionPolicy(
                                    connector_provision=shared.ConnectorProvision(),
                                    delegated_provision=shared.DelegatedProvision(
                                        app_id='suscipit',
                                        entitlement_id='velit',
                                    ),
                                    manual_provision=shared.ManualProvision(
                                        instructions='culpa',
                                        user_ids=[
                                            'recusandae',
                                            'totam',
                                            'fugiat',
                                        ],
                                    ),
                                ),
                                assigned=False,
                            ),
                        ),
                        shared.PolicyStepInput(
                            approval=shared.ApprovalInput(
                                app_group_approval=shared.AppGroupApproval1(),
                                app_owner_approval=shared.AppOwnerApproval1(),
                                entitlement_owner_approval=shared.EntitlementOwnerApproval1(),
                                manager_approval=shared.ManagerApproval1(),
                                self_approval=shared.SelfApproval1(),
                                user_approval=shared.UserApproval1(),
                            ),
                            provision=shared.Provision(
                                provision_policy=shared.ProvisionPolicy(
                                    connector_provision=shared.ConnectorProvision(),
                                    delegated_provision=shared.DelegatedProvision(
                                        app_id='vel',
                                        entitlement_id='ducimus',
                                    ),
                                    manual_provision=shared.ManualProvision(
                                        instructions='quos',
                                        user_ids=[
                                            'labore',
                                            'possimus',
                                        ],
                                    ),
                                ),
                                assigned=False,
                            ),
                        ),
                        shared.PolicyStepInput(
                            approval=shared.ApprovalInput(
                                app_group_approval=shared.AppGroupApproval1(),
                                app_owner_approval=shared.AppOwnerApproval1(),
                                entitlement_owner_approval=shared.EntitlementOwnerApproval1(),
                                manager_approval=shared.ManagerApproval1(),
                                self_approval=shared.SelfApproval1(),
                                user_approval=shared.UserApproval1(),
                            ),
                            provision=shared.Provision(
                                provision_policy=shared.ProvisionPolicy(
                                    connector_provision=shared.ConnectorProvision(),
                                    delegated_provision=shared.DelegatedProvision(
                                        app_id='facilis',
                                        entitlement_id='cum',
                                    ),
                                    manual_provision=shared.ManualProvision(
                                        instructions='commodi',
                                        user_ids=[
                                            'corporis',
                                            'reiciendis',
                                        ],
                                    ),
                                ),
                                assigned=False,
                            ),
                        ),
                    ],
                ),
                "assumenda": shared.PolicyStepsInput(
                    steps=[
                        shared.PolicyStepInput(
                            approval=shared.ApprovalInput(
                                app_group_approval=shared.AppGroupApproval1(),
                                app_owner_approval=shared.AppOwnerApproval1(),
                                entitlement_owner_approval=shared.EntitlementOwnerApproval1(),
                                manager_approval=shared.ManagerApproval1(),
                                self_approval=shared.SelfApproval1(),
                                user_approval=shared.UserApproval1(),
                            ),
                            provision=shared.Provision(
                                provision_policy=shared.ProvisionPolicy(
                                    connector_provision=shared.ConnectorProvision(),
                                    delegated_provision=shared.DelegatedProvision(
                                        app_id='recusandae',
                                        entitlement_id='aliquid',
                                    ),
                                    manual_provision=shared.ManualProvision(
                                        instructions='aperiam',
                                        user_ids=[
                                            'consectetur',
                                            'in',
                                            'exercitationem',
                                        ],
                                    ),
                                ),
                                assigned=False,
                            ),
                        ),
                        shared.PolicyStepInput(
                            approval=shared.ApprovalInput(
                                app_group_approval=shared.AppGroupApproval1(),
                                app_owner_approval=shared.AppOwnerApproval1(),
                                entitlement_owner_approval=shared.EntitlementOwnerApproval1(),
                                manager_approval=shared.ManagerApproval1(),
                                self_approval=shared.SelfApproval1(),
                                user_approval=shared.UserApproval1(),
                            ),
                            provision=shared.Provision(
                                provision_policy=shared.ProvisionPolicy(
                                    connector_provision=shared.ConnectorProvision(),
                                    delegated_provision=shared.DelegatedProvision(
                                        app_id='earum',
                                        entitlement_id='facere',
                                    ),
                                    manual_provision=shared.ManualProvision(
                                        instructions='numquam',
                                        user_ids=[
                                            'suscipit',
                                            'reiciendis',
                                            'quidem',
                                            'saepe',
                                        ],
                                    ),
                                ),
                                assigned=False,
                            ),
                        ),
                    ],
                ),
                "necessitatibus": shared.PolicyStepsInput(
                    steps=[
                        shared.PolicyStepInput(
                            approval=shared.ApprovalInput(
                                app_group_approval=shared.AppGroupApproval1(),
                                app_owner_approval=shared.AppOwnerApproval1(),
                                entitlement_owner_approval=shared.EntitlementOwnerApproval1(),
                                manager_approval=shared.ManagerApproval1(),
                                self_approval=shared.SelfApproval1(),
                                user_approval=shared.UserApproval1(),
                            ),
                            provision=shared.Provision(
                                provision_policy=shared.ProvisionPolicy(
                                    connector_provision=shared.ConnectorProvision(),
                                    delegated_provision=shared.DelegatedProvision(
                                        app_id='sunt',
                                        entitlement_id='asperiores',
                                    ),
                                    manual_provision=shared.ManualProvision(
                                        instructions='adipisci',
                                        user_ids=[
                                            'amet',
                                        ],
                                    ),
                                ),
                                assigned=False,
                            ),
                        ),
                        shared.PolicyStepInput(
                            approval=shared.ApprovalInput(
                                app_group_approval=shared.AppGroupApproval1(),
                                app_owner_approval=shared.AppOwnerApproval1(),
                                entitlement_owner_approval=shared.EntitlementOwnerApproval1(),
                                manager_approval=shared.ManagerApproval1(),
                                self_approval=shared.SelfApproval1(),
                                user_approval=shared.UserApproval1(),
                            ),
                            provision=shared.Provision(
                                provision_policy=shared.ProvisionPolicy(
                                    connector_provision=shared.ConnectorProvision(),
                                    delegated_provision=shared.DelegatedProvision(
                                        app_id='beatae',
                                        entitlement_id='dignissimos',
                                    ),
                                    manual_provision=shared.ManualProvision(
                                        instructions='a',
                                        user_ids=[
                                            'consectetur',
                                            'corporis',
                                            'harum',
                                            'laboriosam',
                                        ],
                                    ),
                                ),
                                assigned=False,
                            ),
                        ),
                    ],
                ),
            },
            policy_type=shared.PolicyPolicyType.POLICY_TYPE_UNSPECIFIED,
            post_actions=[
                shared.PolicyPostActions(
                    certify_remediate_immediately=False,
                ),
                shared.PolicyPostActions(
                    certify_remediate_immediately=False,
                ),
                shared.PolicyPostActions(
                    certify_remediate_immediately=False,
                ),
                shared.PolicyPostActions(
                    certify_remediate_immediately=False,
                ),
            ],
            reassign_tasks_to_delegates=False,
        ),
        update_mask='libero',
    ),
    id='1ea42655-5ba3-4c28-b44e-d53b88f3a8d8',
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

