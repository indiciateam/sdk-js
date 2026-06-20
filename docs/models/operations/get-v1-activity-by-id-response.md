# GetV1ActivityByIdResponse

Successful response with the activity details.

## Example Usage

```typescript
import { GetV1ActivityByIdResponse } from "@indiciaosint/sdk/models/operations";

let value: GetV1ActivityByIdResponse = {
  activity: {
    agent: null,
    apiKey: "<value>",
    case: "<value>",
    detail: "<value>",
    id: "<id>",
    query: "<value>",
    result: 9689.91,
    time: 516096,
    type: "username",
    user: "Louvenia_OReilly59",
  },
  success: true,
};
```

## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `activity`                                                                                        | [operations.GetV1ActivityByIdActivity](../../models/operations/get-v1-activity-by-id-activity.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `success`                                                                                         | *boolean*                                                                                         | :heavy_check_mark:                                                                                | N/A                                                                                               |