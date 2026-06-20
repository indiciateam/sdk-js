# GetV1ActivityResponse

Successful response with a list of activities.

## Example Usage

```typescript
import { GetV1ActivityResponse } from "@indiciaosint/sdk/models/operations";

let value: GetV1ActivityResponse = {
  activities: [
    {
      agent: false,
      apiKey: "<value>",
      case: "<value>",
      detail: "<value>",
      id: "<id>",
      query: "<value>",
      result: "<value>",
      time: 486281,
      type: "whois",
      user: "Drake_Wuckert22",
    },
  ],
  success: true,
};
```

## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `activities`                                                                              | [operations.GetV1ActivityActivity](../../models/operations/get-v1-activity-activity.md)[] | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `success`                                                                                 | *boolean*                                                                                 | :heavy_check_mark:                                                                        | N/A                                                                                       |