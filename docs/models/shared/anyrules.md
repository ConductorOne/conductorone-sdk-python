# AnyRules

AnyRules describe constraints applied exclusively to the
 `google.protobuf.Any` well-known type


## Fields

| Field                                                                                           | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `in_`                                                                                           | List[*str*]                                                                                     | :heavy_minus_sign:                                                                              | In specifies that this field's `type_url` must be equal to one of the<br/> specified values.    |
| `not_in`                                                                                        | List[*str*]                                                                                     | :heavy_minus_sign:                                                                              | NotIn specifies that this field's `type_url` must not be equal to any of<br/> the specified values. |
| `required`                                                                                      | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | Required specifies that this field must be set                                                  |