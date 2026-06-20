# GetV1ActivityByIdActivity

## Example Usage

```typescript
import { GetV1ActivityByIdActivity } from "@indiciaosint/sdk/models/operations";

let value: GetV1ActivityByIdActivity = {
  agent: false,
  apiKey: "<value>",
  case: "<value>",
  detail: "<value>",
  id: "<id>",
  query: "<value>",
  result: false,
  time: 960346,
  type: "pimeyes",
  user: "Elmo36",
};
```

## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `agent`                                                                                   | *boolean*                                                                                 | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `apiKey`                                                                                  | *string*                                                                                  | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `case`                                                                                    | *string*                                                                                  | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `detail`                                                                                  | *string*                                                                                  | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `id`                                                                                      | *string*                                                                                  | :heavy_check_mark:                                                                        | a RFC-4122-compliant UUID                                                                 |
| `query`                                                                                   | *string*                                                                                  | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `result`                                                                                  | *operations.GetV1ActivityByIdResultUnion*                                                 | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `time`                                                                                    | *number*                                                                                  | :heavy_check_mark:                                                                        | an integer representing a safe Unix timestamp                                             |
| `type`                                                                                    | [operations.GetV1ActivityByIdType](../../models/operations/get-v1-activity-by-id-type.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `user`                                                                                    | *string*                                                                                  | :heavy_check_mark:                                                                        | N/A                                                                                       |