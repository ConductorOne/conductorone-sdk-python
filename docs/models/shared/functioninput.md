# FunctionInput

Function represents a customer-provided code extension in the API


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The description field.                                               |
| `display_name`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The displayName field.                                               |
| `encrypted_values`                                                   | Dict[str, *str*]                                                     | :heavy_minus_sign:                                                   | The encryptedValues field.                                           |
| `function_type`                                                      | [Optional[shared.FunctionType]](../../models/shared/functiontype.md) | :heavy_minus_sign:                                                   | The functionType field.                                              |
| `head`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The head field.                                                      |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The id field.                                                        |
| `is_draft`                                                           | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | The isDraft field.                                                   |
| `outbound_network_allowlist`                                         | List[*str*]                                                          | :heavy_minus_sign:                                                   | The outboundNetworkAllowlist field.                                  |
| `published_commit_id`                                                | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The publishedCommitId field.                                         |