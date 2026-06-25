# ListActivitiesActivity

## Example Usage

```typescript
import { ListActivitiesActivity } from "@indiciaosint/sdk/models/operations";

let value: ListActivitiesActivity = {
  agent: null,
  apiKey: "<value>",
  case: "<value>",
  detail: "<value>",
  id: "<id>",
  query: "<value>",
  result: false,
  time: 619996,
  type: "tiktok",
  user: "Yvonne_Rau66",
};
```

## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `agent`                                                                          | *boolean*                                                                        | :heavy_check_mark:                                                               | N/A                                                                              |
| `apiKey`                                                                         | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `case`                                                                           | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `detail`                                                                         | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `id`                                                                             | *string*                                                                         | :heavy_check_mark:                                                               | a RFC-4122-compliant UUID                                                        |
| `query`                                                                          | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `result`                                                                         | *operations.ListActivitiesResultUnion*                                           | :heavy_check_mark:                                                               | N/A                                                                              |
| `time`                                                                           | *number*                                                                         | :heavy_check_mark:                                                               | an integer representing a safe Unix timestamp                                    |
| `type`                                                                           | [operations.ListActivitiesType](../../models/operations/list-activities-type.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `user`                                                                           | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |