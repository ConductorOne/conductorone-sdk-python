# SearchStepUpTransactionsResponse

Response message for searching step-up transactions


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `list`                                                                     | List[[shared.StepUpTransaction](../../models/shared/stepuptransaction.md)] | :heavy_minus_sign:                                                         | List of transactions matching the search criteria                          |
| `next_page_token`                                                          | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Token for retrieving the next page of results                              |