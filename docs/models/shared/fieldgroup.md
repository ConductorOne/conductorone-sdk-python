# FieldGroup

The FieldGroup message.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `display_name`                                                                       | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Nice name this group (e.g. renders as a Tab label)                                   |
| `field_names`                                                                        | List[*str*]                                                                          | :heavy_minus_sign:                                                                   | Field names are "guaranteed" to be unique, but can be repeated in and between lists. |
| `help_text`                                                                          | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Optional. User-facing help text.                                                     |
| `name`                                                                               | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Unique ID.                                                                           |