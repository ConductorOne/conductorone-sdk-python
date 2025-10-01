# Directory

This object indicates that an app is also a directory.

This message contains a oneof named account_filter. Only a single field of the following list may be set at a time:
  - all
  - celExpression



## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `directory_account_filter_all`                                                                         | [OptionalNullable[shared.DirectoryAccountFilterAll]](../../models/shared/directoryaccountfilterall.md) | :heavy_minus_sign:                                                                                     | The DirectoryAccountFilterAll message.                                                                 |
| `directory_account_filter_cel`                                                                         | [OptionalNullable[shared.DirectoryAccountFilterCel]](../../models/shared/directoryaccountfiltercel.md) | :heavy_minus_sign:                                                                                     | The DirectoryAccountFilterCel message.                                                                 |
| `app_id`                                                                                               | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | The ID of the app associated with the directory.                                                       |
| `created_at`                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                   | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `deleted_at`                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                   | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `updated_at`                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                   | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |