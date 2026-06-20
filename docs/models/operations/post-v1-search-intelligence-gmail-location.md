# PostV1SearchIntelligenceGmailLocation

## Example Usage

```typescript
import { PostV1SearchIntelligenceGmailLocation } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligenceGmailLocation = {
  address: "8804 Catalina Pass",
  costLevel: 1888.05,
  id: "<id>",
  name: "<value>",
  position: {
    latitude: 7861.28,
    longitude: 9974.98,
  },
  tags: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
  types: [
    "<value 1>",
    "<value 2>",
  ],
};
```

## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `address`                                                  | *string*                                                   | :heavy_check_mark:                                         | N/A                                                        |
| `costLevel`                                                | *number*                                                   | :heavy_check_mark:                                         | N/A                                                        |
| `id`                                                       | *string*                                                   | :heavy_check_mark:                                         | N/A                                                        |
| `name`                                                     | *string*                                                   | :heavy_check_mark:                                         | N/A                                                        |
| `position`                                                 | [operations.Position](../../models/operations/position.md) | :heavy_check_mark:                                         | N/A                                                        |
| `tags`                                                     | *string*[]                                                 | :heavy_check_mark:                                         | N/A                                                        |
| `types`                                                    | *string*[]                                                 | :heavy_check_mark:                                         | N/A                                                        |