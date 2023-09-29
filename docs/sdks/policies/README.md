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
        bearer_auth="",
        oauth="",
    ),
)

req = shared.CreatePolicyRequestInput(
    description='Multi-tiered scalable data-warehouse',
    display_name='Markets Sausages ASCII',
    policy_steps={
        "eligendi": shared.PolicyStepsInput(
            steps=[
                shared.PolicyStepInput(
                    accept=shared.Accept(),
                    approval=shared.ApprovalInput(
                        app_group_approval=shared.AppGroupApprovalInput(),
                        app_owner_approval=shared.AppOwnerApprovalInput(),
                        entitlement_owner_approval=shared.EntitlementOwnerApprovalInput(),
                        expression_approval=shared.ExpressionApprovalInput(),
                        manager_approval=shared.ManagerApprovalInput(),
                        self_approval=shared.SelfApprovalInput(),
                        user_approval=shared.UserApprovalInput(),
                    ),
                    provision=shared.Provision(
                        provision_policy=shared.ProvisionPolicy(
                            connector_provision=shared.ConnectorProvision(),
                            delegated_provision=shared.DelegatedProvision(
                                app_id='National Lauderhill',
                                entitlement_id='overriding Latin',
                            ),
                            manual_provision=shared.ManualProvision(
                                instructions='Garden',
                                user_ids=[
                                    'Health',
                                ],
                            ),
                        ),
                        provision_target=shared.ProvisionTarget(
                            app_entitlement_id='exuding',
                            app_id='SSD',
                            app_user_id='Money mesh',
                            grant_duration='silver compressing Berkshire',
                        ),
                        assigned=False,
                    ),
                    reject=shared.Reject(),
                ),
            ],
        ),
    },
    policy_type=shared.CreatePolicyRequestPolicyType.POLICY_TYPE_REVOKE,
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
    id='<ID>',
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
    id='<ID>',
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
    page_size=6488.05,
    page_token='Southeast',
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
            description='Optimized 24/7 middleware',
            display_name='Clothing Tempe',
            policy_steps={
                "eum": shared.PolicyStepsInput(
                    steps=[
                        shared.PolicyStepInput(
                            accept=shared.Accept(),
                            approval=shared.ApprovalInput(
                                app_group_approval=shared.AppGroupApprovalInput(),
                                app_owner_approval=shared.AppOwnerApprovalInput(),
                                entitlement_owner_approval=shared.EntitlementOwnerApprovalInput(),
                                expression_approval=shared.ExpressionApprovalInput(),
                                manager_approval=shared.ManagerApprovalInput(),
                                self_approval=shared.SelfApprovalInput(),
                                user_approval=shared.UserApprovalInput(),
                            ),
                            provision=shared.Provision(
                                provision_policy=shared.ProvisionPolicy(
                                    connector_provision=shared.ConnectorProvision(),
                                    delegated_provision=shared.DelegatedProvision(
                                        app_id='Architect',
                                        entitlement_id='Oregon',
                                    ),
                                    manual_provision=shared.ManualProvision(
                                        instructions='Country alarmed',
                                        user_ids=[
                                            'North',
                                        ],
                                    ),
                                ),
                                provision_target=shared.ProvisionTarget(
                                    app_entitlement_id='Computer teal laborum',
                                    app_id='capitalize mint',
                                    app_user_id='Response HTTP',
                                    grant_duration='Sedan aw Azerbaijanian',
                                ),
                                assigned=False,
                            ),
                            reject=shared.Reject(),
                        ),
                    ],
                ),
            },
            policy_type=shared.PolicyPolicyType.POLICY_TYPE_PROVISION,
            post_actions=[
                shared.PolicyPostActions(
                    certify_remediate_immediately=False,
                ),
            ],
            reassign_tasks_to_delegates=False,
            rules=[
                shared.Rule(
                    condition='Wisconsin',
                    policy_key='Plastic generate fugit',
                ),
            ],
        ),
        update_mask='SUV',
    ),
    id='<ID>',
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

