# SearchPhonePhone

## Example Usage

```typescript
import { SearchPhonePhone } from "@indiciaosint/sdk/models/operations";

let value: SearchPhonePhone = {
  countryCode: "PG",
  nationalFormat: "<value>",
  phoneNumber: "589-256-4711 x625",
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
| `smsPumpingRisk`                                                                     | [operations.SmsPumpingRisk](../../models/operations/sms-pumping-risk.md)             | :heavy_minus_sign:                                                                   | N/A                                                                                  |