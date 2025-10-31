# DirectoryServiceUpdateRequest

Update a directory by app_id.

This message contains a oneof named account_filter. Only a single field of the following list may be set at a time:
  - all
  - celExpression



## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `directory_account_filter_all`                                                                         | [OptionalNullable[shared.DirectoryAccountFilterAll]](../../models/shared/directoryaccountfilterall.md) | :heavy_minus_sign:                                                                                     | The DirectoryAccountFilterAll message.                                                                 |
| `directory_account_filter_cel`                                                                         | [OptionalNullable[shared.DirectoryAccountFilterCel]](../../models/shared/directoryaccountfiltercel.md) | :heavy_minus_sign:                                                                                     | The DirectoryAccountFilterCel message.                                                                 |
| `directory_expand_mask`                                                                                | [Optional[shared.DirectoryExpandMask]](../../models/shared/directoryexpandmask.md)                     | :heavy_minus_sign:                                                                                     | The fields to be included in the directory response.                                                   |