# GetV1PricingResponse

Successful response

## Example Usage

```typescript
import { GetV1PricingResponse } from "@indiciaosint/sdk/models/operations";

let value: GetV1PricingResponse = {
  current: 2743.2,
  prices: {
    "key": 5630.08,
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