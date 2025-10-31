# AutomationTemplateVersion

The AutomationTemplateVersion message.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `automation_steps`                                                         | List[[shared.AutomationStep](../../models/shared/automationstep.md)]       | :heavy_minus_sign:                                                         | The automationSteps field.                                                 |
| `automation_template_id`                                                   | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The automationTemplateId field.                                            |
| `created_at`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | N/A                                                                        |
| `deleted_at`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | N/A                                                                        |
| `triggers`                                                                 | List[[shared.AutomationTrigger](../../models/shared/automationtrigger.md)] | :heavy_minus_sign:                                                         | The triggers field.                                                        |
| `updated_at`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | N/A                                                                        |
| `version`                                                                  | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | The version field.                                                         |