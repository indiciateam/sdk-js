# ListActivitiesResponse

Successful response with a list of activities.

## Example Usage

```typescript
import { ListActivitiesResponse } from "@indiciaosint/sdk/models/operations";

let value: ListActivitiesResponse = {
  activities: [
    {
      agent: true,
      apiKey: null,
      case: "<value>",
      detail: "<value>",
      id: "<id>",
      query: "<value>",
      result: "<value>",
      time: 737729,
      type: "shodan",
      user: "Lura_Cormier34",
    },
  ],
  success: false,
};
```

## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `activities`                                                                               | [operations.ListActivitiesActivity](../../models/operations/list-activities-activity.md)[] | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `success`                                                                                  | *boolean*                                                                                  | :heavy_check_mark:                                                                         | N/A                                                                                        |