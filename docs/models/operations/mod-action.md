# ModAction

## Example Usage

```typescript
import { ModAction } from "@indiciaosint/sdk/models/operations";

let value: ModAction = {
  date: 6078.6,
  description: "dreamily license plus between availability forenenst evenly",
  details: {
    ground: "<value>",
    source: "<value>",
    targetType: "<value>",
  },
  id: "<id>",
  status: "<value>",
  tags: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
  timeline: {
    application: 4058.2,
    content: 5838.86,
    created: 5441.95,
  },
  title: "<value>",
};
```

## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `date`                                                                                 | *number*                                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `description`                                                                          | *string*                                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `details`                                                                              | [operations.Details](../../models/operations/details.md)                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `id`                                                                                   | *string*                                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `status`                                                                               | *string*                                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `tags`                                                                                 | *string*[]                                                                             | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `timeline`                                                                             | [operations.SearchDiscordTimeline](../../models/operations/search-discord-timeline.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `title`                                                                                | *string*                                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |