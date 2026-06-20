# Antiviruses

## Example Usage

```typescript
import { Antiviruses } from "@indiciaosint/sdk/models/operations";

let value: Antiviruses = {
  list: [],
};
```

## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `list`                                               | [operations.List](../../models/operations/list.md)[] | :heavy_check_mark:                                   | N/A                                                  |
| `found`                                              | *number*                                             | :heavy_minus_sign:                                   | N/A                                                  |
| `free`                                               | *operations.Free*                                    | :heavy_minus_sign:                                   | N/A                                                  |
| `notFound`                                           | *string*                                             | :heavy_minus_sign:                                   | N/A                                                  |
| `total`                                              | *number*                                             | :heavy_minus_sign:                                   | N/A                                                  |