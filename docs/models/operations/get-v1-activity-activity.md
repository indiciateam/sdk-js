# GetV1ActivityActivity

## Example Usage

```typescript
import { GetV1ActivityActivity } from "@indiciaosint/sdk/models/operations";

let value: GetV1ActivityActivity = {
  agent: false,
  apiKey: "<value>",
  case: "<value>",
  detail: "<value>",
  id: "<id>",
  query: "<value>",
  result: false,
  time: 266914,
  type: "doublecounter",
  user: "Pedro_Rosenbaum-Kuhic",
};
```

## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `agent`                                                                         | *boolean*                                                                       | :heavy_check_mark:                                                              | N/A                                                                             |
| `apiKey`                                                                        | *string*                                                                        | :heavy_check_mark:                                                              | N/A                                                                             |
| `case`                                                                          | *string*                                                                        | :heavy_check_mark:                                                              | N/A                                                                             |
| `detail`                                                                        | *string*                                                                        | :heavy_check_mark:                                                              | N/A                                                                             |
| `id`                                                                            | *string*                                                                        | :heavy_check_mark:                                                              | a RFC-4122-compliant UUID                                                       |
| `query`                                                                         | *string*                                                                        | :heavy_check_mark:                                                              | N/A                                                                             |
| `result`                                                                        | *operations.GetV1ActivityResultUnion*                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `time`                                                                          | *number*                                                                        | :heavy_check_mark:                                                              | an integer representing a safe Unix timestamp                                   |
| `type`                                                                          | [operations.GetV1ActivityType](../../models/operations/get-v1-activity-type.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `user`                                                                          | *string*                                                                        | :heavy_check_mark:                                                              | N/A                                                                             |