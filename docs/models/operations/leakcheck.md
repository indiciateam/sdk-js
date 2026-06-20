# Leakcheck

## Example Usage

```typescript
import { Leakcheck } from "@indiciaosint/sdk/models/operations";

let value: Leakcheck = {
  found: 7627.93,
  result: [
    {
      fields: [],
    },
  ],
  success: true,
};
```

## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `found`                                                                     | *number*                                                                    | :heavy_check_mark:                                                          | N/A                                                                         |
| `result`                                                                    | [operations.LeakcheckResult](../../models/operations/leakcheck-result.md)[] | :heavy_check_mark:                                                          | N/A                                                                         |
| `success`                                                                   | *boolean*                                                                   | :heavy_check_mark:                                                          | N/A                                                                         |
| `error`                                                                     | *string*                                                                    | :heavy_minus_sign:                                                          | N/A                                                                         |