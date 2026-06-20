# PostV1SearchIntelligencePhonePhone

## Example Usage

```typescript
import { PostV1SearchIntelligencePhonePhone } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligencePhonePhone = {
  countryCode: "MT",
  nationalFormat: "<value>",
  phoneNumber: "(777) 928-0038",
  valid: true,
};
```

## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `countryCode`                                                                        | *string*                                                                             | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `nationalFormat`                                                                     | *string*                                                                             | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `phoneNumber`                                                                        | *string*                                                                             | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `valid`                                                                              | *boolean*                                                                            | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `lineTypeIntelligence`                                                               | [operations.LineTypeIntelligence](../../models/operations/line-type-intelligence.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `simSwap`                                                                            | [operations.SimSwap](../../models/operations/sim-swap.md)                            | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `smsPumpingRisk`                                                                     | [operations.SmsPumpingRisk](../../models/operations/sms-pumping-risk.md)             | :heavy_minus_sign:                                                                   | N/A                                                                                  |