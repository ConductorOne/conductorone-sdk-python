# TaskRevokeSource

The TaskRevokeSource message indicates the source of the revoke task is one of expired, nonUsage, request, or review.

This message contains a oneof named origin. Only a single field of the following list may be set at a time:
  - review
  - request
  - expired
  - nonUsage



## Fields

| Field                                                                                                                 | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `task_revoke_source_expired`                                                                                          | [OptionalNullable[shared.TaskRevokeSourceExpired]](../../models/shared/taskrevokesourceexpired.md)                    | :heavy_minus_sign:                                                                                                    | The TaskRevokeSourceExpired message indicates that the source of the revoke task is due to a grant expiring.          |
| `task_revoke_source_non_usage`                                                                                        | [OptionalNullable[shared.TaskRevokeSourceNonUsage]](../../models/shared/taskrevokesourcenonusage.md)                  | :heavy_minus_sign:                                                                                                    | The TaskRevokeSourceNonUsage message indicates that the source of the revoke task is due to the grant not being used. |
| `task_revoke_source_request`                                                                                          | [OptionalNullable[shared.TaskRevokeSourceRequest]](../../models/shared/taskrevokesourcerequest.md)                    | :heavy_minus_sign:                                                                                                    | The TaskRevokeSourceRequest message indicates that the source of the revoke task was a request.                       |
| `task_revoke_source_review`                                                                                           | [OptionalNullable[shared.TaskRevokeSourceReview]](../../models/shared/taskrevokesourcereview.md)                      | :heavy_minus_sign:                                                                                                    | The TaskRevokeSourceReview message tracks which access review was the source of the specificed revoke ticket.         |