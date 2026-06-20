# AIp

## Example Usage

```typescript
import { AIp } from "@indiciaosint/sdk/models/operations";

let value: AIp = {
  asn: "<value>",
  asnName: "<value>",
  asnRange: "<value>",
  country: "Brunei Darussalam",
  countryCode: "OM",
  ip: "158.98.30.93",
  ptr: "<value>",
};
```

## Fields

| Field                      | Type                       | Required                   | Description                |
| -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| `asn`                      | *string*                   | :heavy_check_mark:         | N/A                        |
| `asnName`                  | *string*                   | :heavy_check_mark:         | N/A                        |
| `asnRange`                 | *string*                   | :heavy_check_mark:         | N/A                        |
| `country`                  | *string*                   | :heavy_check_mark:         | N/A                        |
| `countryCode`              | *string*                   | :heavy_check_mark:         | N/A                        |
| `ip`                       | *string*                   | :heavy_check_mark:         | N/A                        |
| `ptr`                      | *string*                   | :heavy_check_mark:         | N/A                        |
| `banners`                  | *operations.ABannersUnion* | :heavy_minus_sign:         | N/A                        |