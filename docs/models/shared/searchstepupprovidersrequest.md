# SearchStepUpProvidersRequest

Request message for searching step-up providers


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `page_size`                                                                | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | Maximum number of results to return                                        |
| `page_token`                                                               | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Token for pagination                                                       |
| `provider_type`                                                            | [Optional[shared.ProviderType]](../../models/shared/providertype.md)       | :heavy_minus_sign:                                                         | The providerType field.                                                    |
| `query`                                                                    | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Filter by name (partial match)                                             |
| `refs`                                                                     | List[[shared.StepUpProviderRef](../../models/shared/stepupproviderref.md)] | :heavy_minus_sign:                                                         | The refs field.                                                            |