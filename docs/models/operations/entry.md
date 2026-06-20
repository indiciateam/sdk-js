# Entry

## Example Usage

```typescript
import { Entry } from "@indiciaosint/sdk/models/operations";

let value: Entry = {
  action: "<value>",
  actorName: "<value>",
  createdAt: 777025,
  detail: {},
  id: "<id>",
};
```

## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `action`                                      | *string*                                      | :heavy_check_mark:                            | N/A                                           |
| `actorName`                                   | *string*                                      | :heavy_check_mark:                            | N/A                                           |
| `createdAt`                                   | *number*                                      | :heavy_check_mark:                            | an integer representing a safe Unix timestamp |
| `detail`                                      | Record<string, *any*>                         | :heavy_check_mark:                            | N/A                                           |
| `id`                                          | *string*                                      | :heavy_check_mark:                            | N/A                                           |