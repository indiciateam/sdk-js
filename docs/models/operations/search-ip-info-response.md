# SearchIpInfoResponse

Search successful

## Example Usage

```typescript
import { SearchIpInfoResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchIpInfoResponse = {
  data: {
    callingCode: "<value>",
    city: null,
    company: {
      domain: null,
      name: null,
      network: "<value>",
      type: "<value>",
    },
    continentCode: "<value>",
    continentName: "<value>",
    countryCode: "HN",
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
    ip: "5.111.93.110",
    isEu: true,
    languages: [],
    latitude: null,
    longitude: 4516.31,
    postal: "<value>",
    region: "<value>",
    regionCode: "<value>",
    regionType: "<value>",
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
  },
  success: false,
};
```

## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `data`                                                                        | [operations.SearchIpInfoData](../../models/operations/search-ip-info-data.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `success`                                                                     | *boolean*                                                                     | :heavy_check_mark:                                                            | N/A                                                                           |
| `error`                                                                       | *string*                                                                      | :heavy_minus_sign:                                                            | N/A                                                                           |