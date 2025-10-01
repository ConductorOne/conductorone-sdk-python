# FunctionsServiceGetCommitResponse

The FunctionsServiceGetCommitResponse message.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `function_commit`                                                        | [Optional[shared.FunctionCommit]](../../models/shared/functioncommit.md) | :heavy_minus_sign:                                                       | FunctionCommit represents a single commit in a function's history        |
| `content`                                                                | Dict[str, *str*]                                                         | :heavy_minus_sign:                                                       | The content field.                                                       |