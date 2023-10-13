# TaskTypeInput

Task Type provides configuration for the type of task: certify, grant, or revoke

This message contains a oneof named task_type. Only a single field of the following list may be set at a time:
  - grant
  - revoke
  - certify



## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `task_type_certify`                                                                          | [Optional[TaskTypeCertifyInput]](../../models/shared/tasktypecertifyinput.md)                | :heavy_minus_sign:                                                                           | The TaskTypeCertify message indicates that a task is a certify task and all related details. |
| `task_type_grant`                                                                            | [Optional[TaskTypeGrantInput]](../../models/shared/tasktypegrantinput.md)                    | :heavy_minus_sign:                                                                           | The TaskTypeGrant message indicates that a task is a grant task and all related details.     |
| `task_type_revoke`                                                                           | [Optional[TaskTypeRevokeInput]](../../models/shared/tasktyperevokeinput.md)                  | :heavy_minus_sign:                                                                           | The TaskTypeRevoke message indicates that a task is a revoke task and all related details.   |