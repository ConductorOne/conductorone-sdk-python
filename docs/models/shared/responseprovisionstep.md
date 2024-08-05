# ResponseProvisionStep

The ResponseProvisionStep message.

This message contains a oneof named outcome. Only a single field of the following list may be set at a time:
  - complete
  - errored



## Fields

| Field                                                                                                           | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `response_provision_step_complete`                                                                              | [OptionalNullable[shared.ResponseProvisionStepComplete]](../../models/shared/responseprovisionstepcomplete.md)  | :heavy_minus_sign:                                                                                              | The ResponseProvisionStepComplete message.                                                                      |
| `response_provision_step_errored`                                                                               | [OptionalNullable[shared.ResponseProvisionStepErrored]](../../models/shared/responseprovisionsteperrored.md)    | :heavy_minus_sign:                                                                                              | The ResponseProvisionStepErrored message.                                                                       |
| `version`                                                                                                       | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | version contains the constant value "v1". Future versions of the Webhook Response<br/> will use a different string. |