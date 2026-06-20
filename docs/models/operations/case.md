# Case

## Example Usage

```typescript
import { Case } from "@indiciaosint/sdk/models/operations";

let value: Case = {
  createdAt: 384318,
  description: null,
  id: "<id>",
  name: "<value>",
  organizationId: "<id>",
  owner: "<value>",
};
```

## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `createdAt`                                   | *number*                                      | :heavy_check_mark:                            | an integer representing a safe Unix timestamp |
| `description`                                 | *string*                                      | :heavy_check_mark:                            | N/A                                           |
| `id`                                          | *string*                                      | :heavy_check_mark:                            | N/A                                           |
| `name`                                        | *string*                                      | :heavy_check_mark:                            | N/A                                           |
| `organizationId`                              | *string*                                      | :heavy_check_mark:                            | N/A                                           |
| `owner`                                       | *string*                                      | :heavy_check_mark:                            | N/A                                           |