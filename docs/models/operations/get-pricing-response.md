# GetPricingResponse

Successful response

## Example Usage

```typescript
import { GetPricingResponse } from "@indiciaosint/sdk/models/operations";

let value: GetPricingResponse = {
  current: 725.11,
  prices: {
    "key": 3378.04,
    "key1": 3824.11,
  },
  success: true,
};
```

## Fields

| Field                    | Type                     | Required                 | Description              |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `current`                | *number*                 | :heavy_check_mark:       | N/A                      |
| `prices`                 | Record<string, *number*> | :heavy_check_mark:       | N/A                      |
| `success`                | *boolean*                | :heavy_check_mark:       | N/A                      |