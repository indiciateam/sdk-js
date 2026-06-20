# Match

## Example Usage

```typescript
import { Match } from "@indiciaosint/sdk/models/operations";

let value: Match = {
  asn: "<value>",
  cpe: [],
  data: "<value>",
  domains: [
    "<value 1>",
  ],
  hostnames: [
    "<value 1>",
    "<value 2>",
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
  os: "WebOS",
  port: 928.78,
  product: "Incredible Metal Soap",
  timestamp: "<value>",
  transport: "<value>",
};
```

## Fields

| Field                                                                                                                           | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `asn`                                                                                                                           | *string*                                                                                                                        | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `cpe`                                                                                                                           | *string*[]                                                                                                                      | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `data`                                                                                                                          | *string*                                                                                                                        | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `domains`                                                                                                                       | *string*[]                                                                                                                      | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `hostnames`                                                                                                                     | *string*[]                                                                                                                      | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `ipStr`                                                                                                                         | *string*                                                                                                                        | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `isp`                                                                                                                           | *string*                                                                                                                        | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `location`                                                                                                                      | [operations.PostV1SearchInfrastructureShodanLocation](../../models/operations/post-v1-search-infrastructure-shodan-location.md) | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `org`                                                                                                                           | *string*                                                                                                                        | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `os`                                                                                                                            | *string*                                                                                                                        | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `port`                                                                                                                          | *number*                                                                                                                        | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `product`                                                                                                                       | *string*                                                                                                                        | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `timestamp`                                                                                                                     | *string*                                                                                                                        | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `transport`                                                                                                                     | *string*                                                                                                                        | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `http`                                                                                                                          | [operations.Http](../../models/operations/http.md)                                                                              | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `ssh`                                                                                                                           | [operations.Ssh](../../models/operations/ssh.md)                                                                                | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `ssl`                                                                                                                           | [operations.Ssl](../../models/operations/ssl.md)                                                                                | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |