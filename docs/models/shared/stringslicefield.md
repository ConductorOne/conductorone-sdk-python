# StringSliceField

The StringSliceField message.

This message contains a oneof named view. Only a single field of the following list may be set at a time:
  - chipsField


This message contains a oneof named _rules. Only a single field of the following list may be set at a time:
  - rules



## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `chips_field`                                                                  | [OptionalNullable[shared.ChipsField]](../../models/shared/chipsfield.md)       | :heavy_minus_sign:                                                             | The ChipsField message.                                                        |
| `repeated_rules`                                                               | [OptionalNullable[shared.RepeatedRules]](../../models/shared/repeatedrules.md) | :heavy_minus_sign:                                                             | RepeatedRules describe the constraints applied to `repeated` values            |
| `default_values`                                                               | List[*str*]                                                                    | :heavy_minus_sign:                                                             | The defaultValues field.                                                       |
| `placeholder`                                                                  | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The placeholder field.                                                         |