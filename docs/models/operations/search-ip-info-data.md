# SearchIpInfoData

## Example Usage

```typescript
import { SearchIpInfoData } from "@indiciaosint/sdk/models/operations";

let value: SearchIpInfoData = {
  callingCode: "<value>",
  city: "Bellevue",
  company: {
    domain: null,
    name: null,
    network: "<value>",
    type: "<value>",
  },
  continentCode: "<value>",
  continentName: "<value>",
  countryCode: "IE",
  countryName: "<value>",
  currency: {
    code: "<value>",
    name: "<value>",
    native: "<value>",
    plural: "<value>",
    symbol: "<value>",
  },
  emojiFlag: "<value>",
  emojiUnicode: "<value>",
  ip: "55.179.165.72",
  isEu: true,
  languages: [],
  latitude: 9270.48,
  longitude: 742.59,
  postal: "<value>",
  region: "<value>",
  regionCode: "<value>",
  regionType: null,
  threat: {
    isAnonymous: true,
    isBogon: true,
    isDatacenter: false,
    isIcloudRelay: true,
    isKnownAbuser: true,
    isKnownAttacker: true,
    isProxy: false,
    isThreat: true,
    isTor: true,
    isVpn: true,
    scores: {
      proxyScore: 55.21,
      threatScore: 4801.46,
      trustScore: 8615.58,
      vpnScore: 1742.51,
    },
  },
  timeZone: {
    abbr: "<value>",
    currentTime: "<value>",
    isDst: true,
    name: "<value>",
    offset: "<value>",
  },
};
```

## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `callingCode`                                                  | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `city`                                                         | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `company`                                                      | [operations.Company](../../models/operations/company.md)       | :heavy_check_mark:                                             | N/A                                                            |
| `continentCode`                                                | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `continentName`                                                | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `countryCode`                                                  | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `countryName`                                                  | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `currency`                                                     | [operations.Currency](../../models/operations/currency.md)     | :heavy_check_mark:                                             | N/A                                                            |
| `emojiFlag`                                                    | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `emojiUnicode`                                                 | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `ip`                                                           | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `isEu`                                                         | *boolean*                                                      | :heavy_check_mark:                                             | N/A                                                            |
| `languages`                                                    | [operations.Languages](../../models/operations/languages.md)[] | :heavy_check_mark:                                             | N/A                                                            |
| `latitude`                                                     | *number*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `longitude`                                                    | *number*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `postal`                                                       | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `region`                                                       | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `regionCode`                                                   | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `regionType`                                                   | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `threat`                                                       | [operations.Threat](../../models/operations/threat.md)         | :heavy_check_mark:                                             | N/A                                                            |
| `timeZone`                                                     | [operations.TimeZone](../../models/operations/time-zone.md)    | :heavy_check_mark:                                             | N/A                                                            |
| `asn`                                                          | [operations.Asn](../../models/operations/asn.md)               | :heavy_minus_sign:                                             | N/A                                                            |
| `carrier`                                                      | [operations.Carrier](../../models/operations/carrier.md)       | :heavy_minus_sign:                                             | N/A                                                            |
| `message`                                                      | *string*                                                       | :heavy_minus_sign:                                             | N/A                                                            |