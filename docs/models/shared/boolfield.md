# BoolField

The BoolField message.

This message contains a oneof named view. Only a single field of the following list may be set at a time:
  - checkboxField


This message contains a oneof named _rules. Only a single field of the following list may be set at a time:
  - rules



## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `bool_rules`                                                                   | [OptionalNullable[shared.BoolRules]](../../models/shared/boolrules.md)         | :heavy_minus_sign:                                                             | BoolRules describes the constraints applied to `bool` values                   |
| `checkbox_field`                                                               | [OptionalNullable[shared.CheckboxField]](../../models/shared/checkboxfield.md) | :heavy_minus_sign:                                                             | The CheckboxField message.                                                     |
| `default_value`                                                                | *Optional[bool]*                                                               | :heavy_minus_sign:                                                             | The defaultValue field.                                                        |