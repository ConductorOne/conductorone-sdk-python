# DirectoryServiceCreateRequest

Uplevel an app into a full directory.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `directory_expand_mask`                                                            | [Optional[shared.DirectoryExpandMask]](../../models/shared/directoryexpandmask.md) | :heavy_minus_sign:                                                                 | The fields to be included in the directory response.                               |
| `app_id`                                                                           | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The AppID to make into a directory, providing identities and more for the C1 app.  |