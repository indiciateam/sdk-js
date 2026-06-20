# SmsPumpingRisk

## Example Usage

```typescript
import { SmsPumpingRisk } from "@indiciaosint/sdk/models/operations";

let value: SmsPumpingRisk = {
  numberBlocked: false,
  numberBlockedDate: "<value>",
  numberBlockedLast3Months: false,
};
```

## Fields

| Field                      | Type                       | Required                   | Description                |
| -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| `numberBlocked`            | *boolean*                  | :heavy_check_mark:         | N/A                        |
| `numberBlockedDate`        | *string*                   | :heavy_check_mark:         | N/A                        |
| `numberBlockedLast3Months` | *boolean*                  | :heavy_check_mark:         | N/A                        |
| `carrierRiskCategories`    | *string*                   | :heavy_minus_sign:         | N/A                        |