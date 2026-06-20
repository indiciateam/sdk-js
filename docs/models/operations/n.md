# N

## Example Usage

```typescript
import { N } from "@indiciaosint/sdk/models/operations";

let value: N = {
  host: "authentic-platypus.net",
  ips: [
    {
      asn: "<value>",
      asnName: "<value>",
      asnRange: "<value>",
      banners: {},
      country: "South Africa",
      countryCode: "DZ",
      ip: "124.166.235.189",
      ptr: "<value>",
    },
  ],
};
```

## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `host`                                              | *string*                                            | :heavy_check_mark:                                  | N/A                                                 |
| `ips`                                               | [operations.NIp](../../models/operations/n-ip.md)[] | :heavy_check_mark:                                  | N/A                                                 |