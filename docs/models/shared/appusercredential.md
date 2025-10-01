# AppUserCredential

A credentials for the Application User that represents an account in the application.

This message contains a oneof named credential. Only a single field of the following list may be set at a time:
  - encryptedData



## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `encrypted_data`                                                               | [OptionalNullable[shared.EncryptedData]](../../models/shared/encrypteddata.md) | :heavy_minus_sign:                                                             | EncryptedData is a message that contains encrypted bytes and metadata.         |
| `app_id`                                                                       | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The ID of the application.                                                     |
| `app_user_id`                                                                  | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | A unique identifier of the application user.                                   |
| `created_at`                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)           | :heavy_minus_sign:                                                             | N/A                                                                            |
| `deleted_at`                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)           | :heavy_minus_sign:                                                             | N/A                                                                            |
| `expires_at`                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)           | :heavy_minus_sign:                                                             | N/A                                                                            |
| `id`                                                                           | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | A unique identifier of the credential.                                         |
| `updated_at`                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)           | :heavy_minus_sign:                                                             | N/A                                                                            |