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
        oauth="",
    ),
)

req = shared.TaskSearchRequestInput(
    task_expand_mask=shared.TaskExpandMask(
        paths=[
            'est',
            'error',
        ],
    ),
    access_review_ids=[
        'labore',
        'veritatis',
    ],
    account_owner_ids=[
        'consectetur',
        'vitae',
        'inventore',
        'dolorem',
    ],
    actor_id='ad',
    app_entitlement_ids=[
        'iste',
    ],
    app_resource_ids=[
        'nemo',
        'soluta',
    ],
    app_resource_type_ids=[
        'rem',
        'dolorum',
        'odio',
    ],
    app_user_subject_ids=[
        'alias',
    ],
    application_ids=[
        'vel',
    ],
    assignees_in_ids=[
        'quae',
    ],
    created_after=dateutil.parser.isoparse('2022-10-16T23:42:04.526Z'),
    created_before=dateutil.parser.isoparse('2022-01-25T16:13:44.576Z'),
    current_step=shared.TaskSearchRequestCurrentStep.TASK_SEARCH_CURRENT_STEP_UNSPECIFIED,
    emergency_status=shared.TaskSearchRequestEmergencyStatus.UNSPECIFIED,
    exclude_app_entitlement_ids=[
        'nulla',
        'distinctio',
        'maxime',
    ],
    exclude_ids=[
        'quia',
    ],
    include_deleted=False,
    my_work_user_ids=[
        'omnis',
        'libero',
    ],
    opener_ids=[
        'id',
    ],
    page_size=7278.88,
    page_token='fugiat',
    previously_acted_on_ids=[
        'quos',
        'placeat',
        'sit',
    ],
    query='iusto',
    refs=[
        shared.TaskRef(
            id='e1084cb0-672d-41ad-879e-eb9665b85efb',
        ),
    ],
    sort_by=shared.TaskSearchRequestSortBy.TASK_SEARCH_SORT_BY_REVERSE_TICKET_ID,
    subject_ids=[
        'quia',
    ],
    task_states=[
        shared.TaskSearchRequestTaskStates.TASK_STATE_CLOSED,
        shared.TaskSearchRequestTaskStates.TASK_STATE_CLOSED,
        shared.TaskSearchRequestTaskStates.TASK_STATE_UNSPECIFIED,
    ],
    task_types=[
        shared.TaskTypeInput(
            task_type_certify=shared.TaskTypeCertify(),
            task_type_grant=shared.TaskTypeGrant(),
            task_type_revoke=shared.TaskTypeRevokeInput(
                task_revoke_source=shared.TaskRevokeSource(
                    task_revoke_source_expired=shared.TaskRevokeSourceExpired(
                        expired_at=dateutil.parser.isoparse('2022-06-21T04:17:16.724Z'),
                    ),
                    task_revoke_source_non_usage=shared.TaskRevokeSourceNonUsage(
                        expires_at=dateutil.parser.isoparse('2021-07-20T13:08:36.205Z'),
                        last_login=dateutil.parser.isoparse('2022-09-20T13:39:46.907Z'),
                    ),
                    task_revoke_source_request=shared.TaskRevokeSourceRequest(
                        request_user_id='explicabo',
                    ),
                    task_revoke_source_review=shared.TaskRevokeSourceReview(
                        access_review_id='corporis',
                        cert_ticket_id='error',
                    ),
                ),
            ),
        ),
        shared.TaskTypeInput(
            task_type_certify=shared.TaskTypeCertify(),
            task_type_grant=shared.TaskTypeGrant(),
            task_type_revoke=shared.TaskTypeRevokeInput(
                task_revoke_source=shared.TaskRevokeSource(
                    task_revoke_source_expired=shared.TaskRevokeSourceExpired(
                        expired_at=dateutil.parser.isoparse('2022-04-13T22:13:24.007Z'),
                    ),
                    task_revoke_source_non_usage=shared.TaskRevokeSourceNonUsage(
                        expires_at=dateutil.parser.isoparse('2021-02-09T04:42:29.895Z'),
                        last_login=dateutil.parser.isoparse('2022-04-22T18:47:14.845Z'),
                    ),
                    task_revoke_source_request=shared.TaskRevokeSourceRequest(
                        request_user_id='quis',
                    ),
                    task_revoke_source_review=shared.TaskRevokeSourceReview(
                        access_review_id='beatae',
                        cert_ticket_id='unde',
                    ),
                ),
            ),
        ),
        shared.TaskTypeInput(
            task_type_certify=shared.TaskTypeCertify(),
            task_type_grant=shared.TaskTypeGrant(),
            task_type_revoke=shared.TaskTypeRevokeInput(
                task_revoke_source=shared.TaskRevokeSource(
                    task_revoke_source_expired=shared.TaskRevokeSourceExpired(
                        expired_at=dateutil.parser.isoparse('2022-01-14T10:23:30.043Z'),
                    ),
                    task_revoke_source_non_usage=shared.TaskRevokeSourceNonUsage(
                        expires_at=dateutil.parser.isoparse('2022-09-15T02:31:13.378Z'),
                        last_login=dateutil.parser.isoparse('2022-09-29T05:24:35.816Z'),
                    ),
                    task_revoke_source_request=shared.TaskRevokeSourceRequest(
                        request_user_id='nesciunt',
                    ),
                    task_revoke_source_review=shared.TaskRevokeSourceReview(
                        access_review_id='at',
                        cert_ticket_id='officia',
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

