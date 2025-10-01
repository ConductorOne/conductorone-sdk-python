# FieldRelationship

FieldRelationships can be used during form validation, or they can represent
 information that is necessary to when it comes to visually rendering the form

This message contains a oneof named kind. Only a single field of the following list may be set at a time:
  - requiredTogether
  - atLeastOne
  - mutuallyExclusive



## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `at_least_one`                                                                         | [OptionalNullable[shared.AtLeastOne]](../../models/shared/atleastone.md)               | :heavy_minus_sign:                                                                     | The AtLeastOne message.                                                                |
| `mutually_exclusive`                                                                   | [OptionalNullable[shared.MutuallyExclusive]](../../models/shared/mutuallyexclusive.md) | :heavy_minus_sign:                                                                     | The MutuallyExclusive message.                                                         |
| `required_together`                                                                    | [OptionalNullable[shared.RequiredTogether]](../../models/shared/requiredtogether.md)   | :heavy_minus_sign:                                                                     | The RequiredTogether message.                                                          |
| `field_names`                                                                          | List[*str*]                                                                            | :heavy_minus_sign:                                                                     | The names of the fields that share this relationship                                   |