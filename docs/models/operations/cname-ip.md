# CnameIp

## Example Usage

```typescript
import { CnameIp } from "@indiciaosint/sdk/models/operations";

let value: CnameIp = {
  asn: "<value>",
  asnName: "<value>",
  asnRange: "<value>",
  banners: {},
  country: "Colombia",
  countryCode: "ER",
  ip: "c52b:3601:b3f7:5bfe:addd:ecba:f33a:c303",
  ptr: "<value>",
};
```

## Fields

| Field                          | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `asn`                          | *string*                       | :heavy_check_mark:             | N/A                            |
| `asnName`                      | *string*                       | :heavy_check_mark:             | N/A                            |
| `asnRange`                     | *string*                       | :heavy_check_mark:             | N/A                            |
| `banners`                      | *operations.CnameBannersUnion* | :heavy_check_mark:             | N/A                            |
| `country`                      | *string*                       | :heavy_check_mark:             | N/A                            |
| `countryCode`                  | *string*                       | :heavy_check_mark:             | N/A                            |
| `ip`                           | *string*                       | :heavy_check_mark:             | N/A                            |
| `ptr`                          | *string*                       | :heavy_check_mark:             | N/A                            |