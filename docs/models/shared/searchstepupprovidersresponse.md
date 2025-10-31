# SearchStepUpProvidersResponse

Response message for searching step-up providers


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `list`                                                               | List[[shared.StepUpProvider](../../models/shared/stepupprovider.md)] | :heavy_minus_sign:                                                   | List of providers matching the search criteria                       |
| `next_page_token`                                                    | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Token for retrieving the next page of results                        |