# NIp

## Example Usage

```typescript
import { NIp } from "@indiciaosint/sdk/models/operations";

let value: NIp = {
  asn: "<value>",
  asnName: "<value>",
  asnRange: "<value>",
  country: "Somalia",
  countryCode: "OM",
  ip: "122.40.144.134",
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
| `banners`                  | *operations.NBannersUnion* | :heavy_minus_sign:         | N/A                        |