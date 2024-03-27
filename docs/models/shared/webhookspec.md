# WebhookSpec

The WebhookSpec message.


## Fields

| Field                                                                                                          | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `destination`                                                                                                  | *Optional[str]*                                                                                                | :heavy_minus_sign:                                                                                             | The destination field.                                                                                         |
| `payload`                                                                                                      | [Optional[shared.Payload]](../../models/shared/payload.md)                                                     | :heavy_minus_sign:                                                                                             | Contains an arbitrary serialized message along with a @type that describes the type of the serialized message. |