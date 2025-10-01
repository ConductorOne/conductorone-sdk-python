# Int64Field

The Int64Field message.

This message contains a oneof named view. Only a single field of the following list may be set at a time:
  - numberField


This message contains a oneof named _default_value. Only a single field of the following list may be set at a time:
  - defaultValue


This message contains a oneof named _rules. Only a single field of the following list may be set at a time:
  - rules



## Fields

| Field                                                                                                                                             | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `int64_rules`                                                                                                                                     | [OptionalNullable[shared.Int64Rules]](../../models/shared/int64rules.md)                                                                          | :heavy_minus_sign:                                                                                                                                | Int64Rules describes the constraints applied to `int64` values                                                                                    |
| `number_field`                                                                                                                                    | [OptionalNullable[shared.NumberField]](../../models/shared/numberfield.md)                                                                        | :heavy_minus_sign:                                                                                                                                | The NumberField message.                                                                                                                          |
| `default_value`                                                                                                                                   | *OptionalNullable[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                                | The defaultValue field.<br/>This field is part of the `_default_value` oneof.<br/>See the documentation for `c1.api.form.v1.Int64Field` for more details. |
| `placeholder`                                                                                                                                     | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The placeholder field.                                                                                                                            |