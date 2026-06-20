# SearchGmailLocation

## Example Usage

```typescript
import { SearchGmailLocation } from "@indiciaosint/sdk/models/operations";

let value: SearchGmailLocation = {
  address: "89616 Antonia Roads",
  costLevel: 1993.32,
  id: "<id>",
  name: "<value>",
  position: {
    latitude: 9315.93,
    longitude: 1296.15,
  },
  tags: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
  types: [
    "<value 1>",
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