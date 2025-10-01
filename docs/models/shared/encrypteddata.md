# EncryptedData

EncryptedData is a message that contains encrypted bytes and metadata.


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `description`                                         | *Optional[str]*                                       | :heavy_minus_sign:                                    | The human-readable description of the encrypted data. |
| `encrypted_bytes`                                     | *Optional[str]*                                       | :heavy_minus_sign:                                    | The encrypted bytes.                                  |
| `key_id`                                              | *Optional[str]*                                       | :heavy_minus_sign:                                    | The key ID used to encrypt the data.                  |
| `name`                                                | *Optional[str]*                                       | :heavy_minus_sign:                                    | The human-readable name of the encrypted data.        |
| `provider`                                            | *Optional[str]*                                       | :heavy_minus_sign:                                    | The encryption provider used to encrypt the data.     |
| `schema_`                                             | *Optional[str]*                                       | :heavy_minus_sign:                                    | The (optional) JSON schema of the encrypted data.     |