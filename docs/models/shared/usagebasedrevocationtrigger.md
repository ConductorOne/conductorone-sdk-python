# UsageBasedRevocationTrigger

The UsageBasedRevocationTrigger message.

This message contains a oneof named cold_start_schedule. Only a single field of the following list may be set at a time:
  - runImmediately
  - runDelayed



## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `run_delayed`                                                                    | [OptionalNullable[shared.RunDelayed]](../../models/shared/rundelayed.md)         | :heavy_minus_sign:                                                               | The RunDelayed message.                                                          |
| `run_immediately`                                                                | [OptionalNullable[shared.RunImmediately]](../../models/shared/runimmediately.md) | :heavy_minus_sign:                                                               | No fields needed; this just indicates the trigger should run immediately         |
| `app_id`                                                                         | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | The appId field.                                                                 |
| `enabled_at`                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)             | :heavy_minus_sign:                                                               | N/A                                                                              |
| `excluded_group_refs`                                                            | List[[shared.AppEntitlementRef](../../models/shared/appentitlementref.md)]       | :heavy_minus_sign:                                                               | The excludedGroupRefs field.                                                     |
| `excluded_user_refs`                                                             | List[[shared.UserRef](../../models/shared/userref.md)]                           | :heavy_minus_sign:                                                               | The excludedUserRefs field.                                                      |
| `include_users_with_no_activity`                                                 | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | The includeUsersWithNoActivity field.                                            |
| `targeted_app_user_types`                                                        | List[[shared.TargetedAppUserTypes](../../models/shared/targetedappusertypes.md)] | :heavy_minus_sign:                                                               | The targetedAppUserTypes field.                                                  |
| `targeted_entitlement_refs`                                                      | List[[shared.AppEntitlementRef](../../models/shared/appentitlementref.md)]       | :heavy_minus_sign:                                                               | The targetedEntitlementRefs field.                                               |
| `unused_for_days`                                                                | *Optional[int]*                                                                  | :heavy_minus_sign:                                                               | The unusedForDays field.                                                         |