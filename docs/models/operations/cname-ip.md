# CnameIp

## Example Usage

```typescript
import { CnameIp } from "@indiciaosint/sdk/models/operations";

let value: CnameIp = {
  asn: "<value>",
  asnName: "<value>",
  asnRange: "<value>",
  country: "Saint Lucia",
  countryCode: "BA",
  ip: "67.174.216.66",
  ptr: "<value>",
};
```

## Fields

| Field                          | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `asn`                          | *string*                       | :heavy_check_mark:             | N/A                            |
| `asnName`                      | *string*                       | :heavy_check_mark:             | N/A                            |
| `asnRange`                     | *string*                       | :heavy_check_mark:             | N/A                            |
| `country`                      | *string*                       | :heavy_check_mark:             | N/A                            |
| `countryCode`                  | *string*                       | :heavy_check_mark:             | N/A                            |
| `ip`                           | *string*                       | :heavy_check_mark:             | N/A                            |
| `ptr`                          | *string*                       | :heavy_check_mark:             | N/A                            |
| `banners`                      | *operations.CnameBannersUnion* | :heavy_minus_sign:             | N/A                            |