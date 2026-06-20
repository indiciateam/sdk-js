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
      country: "Venezuela",
      countryCode: "JE",
      ip: "51ae:ea5b:e6dd:c4e8:377d:04bc:df91:12ef",
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