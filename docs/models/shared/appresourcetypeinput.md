# AppResourceTypeInput

The AppResourceType is referenced by an app entitlement defining its resource types. Commonly things like Group or Role.


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `display_name`                             | *Optional[str]*                            | :heavy_minus_sign:                         | The display name of the app resource type. |
| `trait_ids`                                | List[*str*]                                | :heavy_minus_sign:                         | Associated trait ids                       |