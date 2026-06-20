# GetActivityResponse

Successful response with the activity details.

## Example Usage

```typescript
import { GetActivityResponse } from "@indiciaosint/sdk/models/operations";

let value: GetActivityResponse = {
  activity: {
    agent: false,
    apiKey: "<value>",
    case: "<value>",
    detail: "<value>",
    id: "<id>",
    query: "<value>",
    result: {},
    time: 609147,
    type: "vehicle",
    user: "Chad.Hilpert",
  },
  success: false,
};
```

## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `activity`                                                                         | [operations.GetActivityActivity](../../models/operations/get-activity-activity.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `success`                                                                          | *boolean*                                                                          | :heavy_check_mark:                                                                 | N/A                                                                                |