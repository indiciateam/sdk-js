# MxIp

## Example Usage

```typescript
import { MxIp } from "@indiciaosint/sdk/models/operations";

let value: MxIp = {
  asn: "<value>",
  asnName: "<value>",
  asnRange: "<value>",
  country: "Gabon",
  countryCode: "VI",
  ip: "3dde:25dd:5b9a:df11:4b7b:57de:dcbb:dbf8",
  ptr: "<value>",
};
```

## Fields

| Field                       | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `asn`                       | *string*                    | :heavy_check_mark:          | N/A                         |
| `asnName`                   | *string*                    | :heavy_check_mark:          | N/A                         |
| `asnRange`                  | *string*                    | :heavy_check_mark:          | N/A                         |
| `country`                   | *string*                    | :heavy_check_mark:          | N/A                         |
| `countryCode`               | *string*                    | :heavy_check_mark:          | N/A                         |
| `ip`                        | *string*                    | :heavy_check_mark:          | N/A                         |
| `ptr`                       | *string*                    | :heavy_check_mark:          | N/A                         |
| `banners`                   | *operations.MxBannersUnion* | :heavy_minus_sign:          | N/A                         |