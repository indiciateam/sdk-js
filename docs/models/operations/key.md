# Key

## Example Usage

```typescript
import { Key } from "@indiciaosint/sdk/models/operations";

let value: Key = {
  createdAt: 942383,
  enabled: false,
  expiresAt: 827140,
  id: "<id>",
  lastRefillAt: 137524,
  lastRequest: 555712,
  metadata: {
    "key": "<value>",
    "key1": "<value>",
  },
  name: "<value>",
  permissions: {
    "key": [
      "<value 1>",
    ],
  },
  prefix: "<value>",
  rateLimitEnabled: true,
  rateLimitMax: null,
  rateLimitTimeWindow: 139.12,
  refillAmount: 467.29,
  refillInterval: 8432.36,
  remaining: 1888.31,
  requestCount: 184.1,
  start: "<value>",
  updatedAt: 658390,
  userId: "<id>",
};
```

## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `createdAt`                                   | *number*                                      | :heavy_check_mark:                            | an integer representing a safe Unix timestamp |
| `enabled`                                     | *boolean*                                     | :heavy_check_mark:                            | N/A                                           |
| `expiresAt`                                   | *number*                                      | :heavy_check_mark:                            | N/A                                           |
| `id`                                          | *string*                                      | :heavy_check_mark:                            | N/A                                           |
| `lastRefillAt`                                | *number*                                      | :heavy_check_mark:                            | N/A                                           |
| `lastRequest`                                 | *number*                                      | :heavy_check_mark:                            | N/A                                           |
| `metadata`                                    | Record<string, *any*>                         | :heavy_check_mark:                            | N/A                                           |
| `name`                                        | *string*                                      | :heavy_check_mark:                            | N/A                                           |
| `permissions`                                 | Record<string, *string*[]>                    | :heavy_check_mark:                            | N/A                                           |
| `prefix`                                      | *string*                                      | :heavy_check_mark:                            | N/A                                           |
| `rateLimitEnabled`                            | *boolean*                                     | :heavy_check_mark:                            | N/A                                           |
| `rateLimitMax`                                | *number*                                      | :heavy_check_mark:                            | N/A                                           |
| `rateLimitTimeWindow`                         | *number*                                      | :heavy_check_mark:                            | N/A                                           |
| `refillAmount`                                | *number*                                      | :heavy_check_mark:                            | N/A                                           |
| `refillInterval`                              | *number*                                      | :heavy_check_mark:                            | N/A                                           |
| `remaining`                                   | *number*                                      | :heavy_check_mark:                            | N/A                                           |
| `requestCount`                                | *number*                                      | :heavy_check_mark:                            | N/A                                           |
| `start`                                       | *string*                                      | :heavy_check_mark:                            | N/A                                           |
| `updatedAt`                                   | *number*                                      | :heavy_check_mark:                            | an integer representing a safe Unix timestamp |
| `userId`                                      | *string*                                      | :heavy_check_mark:                            | N/A                                           |