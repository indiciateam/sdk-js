# SearchShodanData

## Example Usage

```typescript
import { SearchShodanData } from "@indiciaosint/sdk/models/operations";

let value: SearchShodanData = {
  matches: [
    {
      asn: "<value>",
      cpe: [
        "<value 1>",
        "<value 2>",
        "<value 3>",
      ],
      data: "<value>",
      domains: [
        "<value 1>",
      ],
      hostnames: [
        "<value 1>",
      ],
      ipStr: "<value>",
      isp: "<value>",
      location: {
        city: "South Franciscaburgh",
        countryCode: "KM",
        countryName: "<value>",
        dmaCode: 4530.13,
        latitude: 2626.55,
        longitude: 9348.34,
        regionCode: "<value>",
      },
      org: "<value>",
      os: "Windows Phone",
      port: 7082.44,
      product: "Practical Wooden Chips",
      timestamp: "<value>",
      transport: "<value>",
    },
  ],
  total: 1328.94,
};
```

## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `matches`                                              | [operations.Match](../../models/operations/match.md)[] | :heavy_check_mark:                                     | N/A                                                    |
| `total`                                                | *number*                                               | :heavy_check_mark:                                     | N/A                                                    |