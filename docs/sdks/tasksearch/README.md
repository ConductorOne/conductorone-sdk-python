# task_search

### Available Operations

* [search](#search) - Search

## search

Search tasks based on filters specified in the request body.

### Example Usage

```python
import sdk
import dateutil.parser
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = shared.TaskSearchRequestInput(
    task_expand_mask=shared.TaskExpandMask(
        paths=[
            'aliquid',
        ],
    ),
    access_review_ids=[
        'accusantium',
    ],
    account_owner_ids=[
        'repellat',
    ],
    actor_id='doloribus',
    app_entitlement_ids=[
        'ullam',
    ],
    app_resource_ids=[
        'in',
    ],
    app_resource_type_ids=[
        'nam',
    ],
    app_user_subject_ids=[
        'earum',
    ],
    application_ids=[
        'officia',
    ],
    assignees_in_ids=[
        'laborum',
    ],
    created_after=dateutil.parser.isoparse('2022-03-14T23:12:21.252Z'),
    created_before=dateutil.parser.isoparse('2021-04-23T08:23:19.189Z'),
    current_step=shared.TaskSearchRequestCurrentStep.TASK_SEARCH_CURRENT_STEP_PROVISION,
    emergency_status=shared.TaskSearchRequestEmergencyStatus.EMERGENCY,
    exclude_app_entitlement_ids=[
        'cumque',
    ],
    exclude_ids=[
        'vitae',
    ],
    include_deleted=False,
    my_work_user_ids=[
        'rerum',
    ],
    opener_ids=[
        'tempora',
    ],
    page_size=3354.98,
    page_token='inventore',
    previously_acted_on_ids=[
        'fugit',
    ],
    query='cumque',
    refs=[
        shared.TaskRef(
            id='1032648d-c2f6-4151-99eb-fd0e9fe6c632',
        ),
    ],
    sort_by=shared.TaskSearchRequestSortBy.TASK_SEARCH_SORT_BY_ACCOUNT_OWNER,
    subject_ids=[
        'fuga',
    ],
    task_states=[
        shared.TaskSearchRequestTaskStates.TASK_STATE_UNSPECIFIED,
    ],
    task_types=[
        shared.TaskTypeInput(
            task_type_certify=shared.TaskTypeCertifyInput(),
            task_type_grant=shared.TaskTypeGrantInput(
                task_grant_source=shared.TaskGrantSource(
                    external_url='animi',
                    integration_id='necessitatibus',
                ),
            ),
            task_type_revoke=shared.TaskTypeRevokeInput(
                task_revoke_source=shared.TaskRevokeSource(
                    task_revoke_source_expired=shared.TaskRevokeSourceExpired(
                        expired_at=dateutil.parser.isoparse('2022-12-22T05:17:09.936Z'),
                    ),
                    task_revoke_source_non_usage=shared.TaskRevokeSourceNonUsage(
                        expires_at=dateutil.parser.isoparse('2022-11-29T01:33:31.768Z'),
                        last_login=dateutil.parser.isoparse('2022-05-19T23:57:30.950Z'),
                    ),
                    task_revoke_source_request=shared.TaskRevokeSourceRequest(
                        request_user_id='occaecati',
                    ),
                    task_revoke_source_review=shared.TaskRevokeSourceReview(
                        access_review_id='suscipit',
                        cert_ticket_id='adipisci',
                    ),
                ),
            ),
        ),
    ],
)

res = s.task_search.search(req)

if res.task_search_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.TaskSearchRequestInput](../../models/shared/tasksearchrequestinput.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.C1APITaskV1TaskSearchServiceSearchResponse](../../models/operations/c1apitaskv1tasksearchservicesearchresponse.md)**

