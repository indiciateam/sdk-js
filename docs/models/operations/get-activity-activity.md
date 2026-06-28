# GetActivityActivity

## Example Usage

```typescript
import { GetActivityActivity } from "@indiciaosint/sdk/models/operations";

let value: GetActivityActivity = {
  agent: null,
  apiKey: "<value>",
  case: "<value>",
  detail: "<value>",
  id: "<id>",
  query: "<value>",
  result: "<value>",
  time: 774928,
  type: "courtrecords",
  user: "Richie.Ritchie79",
};
```

## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `agent`                                                                    | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `apiKey`                                                                   | *string*                                                                   | :heavy_check_mark:                                                         | N/A                                                                        |
| `case`                                                                     | *string*                                                                   | :heavy_check_mark:                                                         | N/A                                                                        |
| `detail`                                                                   | *string*                                                                   | :heavy_check_mark:                                                         | N/A                                                                        |
| `id`                                                                       | *string*                                                                   | :heavy_check_mark:                                                         | a RFC-4122-compliant UUID                                                  |
| `query`                                                                    | *string*                                                                   | :heavy_check_mark:                                                         | N/A                                                                        |
| `result`                                                                   | *operations.GetActivityResultUnion*                                        | :heavy_check_mark:                                                         | N/A                                                                        |
| `time`                                                                     | *number*                                                                   | :heavy_check_mark:                                                         | an integer representing a safe Unix timestamp                              |
| `type`                                                                     | [operations.GetActivityType](../../models/operations/get-activity-type.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `user`                                                                     | *string*                                                                   | :heavy_check_mark:                                                         | N/A                                                                        |