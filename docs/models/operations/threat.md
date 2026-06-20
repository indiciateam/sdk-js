# Threat

## Example Usage

```typescript
import { Threat } from "@indiciaosint/sdk/models/operations";

let value: Threat = {
  isAnonymous: false,
  isBogon: false,
  isDatacenter: true,
  isIcloudRelay: false,
  isKnownAbuser: false,
  isKnownAttacker: false,
  isProxy: false,
  isThreat: false,
  isTor: false,
  isVpn: true,
  scores: {
    proxyScore: 55.21,
    threatScore: 4801.46,
    trustScore: 8615.58,
    vpnScore: 1742.51,
  },
};
```

## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `isAnonymous`                                                  | *boolean*                                                      | :heavy_check_mark:                                             | N/A                                                            |
| `isBogon`                                                      | *boolean*                                                      | :heavy_check_mark:                                             | N/A                                                            |
| `isDatacenter`                                                 | *boolean*                                                      | :heavy_check_mark:                                             | N/A                                                            |
| `isIcloudRelay`                                                | *boolean*                                                      | :heavy_check_mark:                                             | N/A                                                            |
| `isKnownAbuser`                                                | *boolean*                                                      | :heavy_check_mark:                                             | N/A                                                            |
| `isKnownAttacker`                                              | *boolean*                                                      | :heavy_check_mark:                                             | N/A                                                            |
| `isProxy`                                                      | *boolean*                                                      | :heavy_check_mark:                                             | N/A                                                            |
| `isThreat`                                                     | *boolean*                                                      | :heavy_check_mark:                                             | N/A                                                            |
| `isTor`                                                        | *boolean*                                                      | :heavy_check_mark:                                             | N/A                                                            |
| `isVpn`                                                        | *boolean*                                                      | :heavy_check_mark:                                             | N/A                                                            |
| `scores`                                                       | [operations.Scores](../../models/operations/scores.md)         | :heavy_check_mark:                                             | N/A                                                            |
| `blocklists`                                                   | [operations.Blocklist](../../models/operations/blocklist.md)[] | :heavy_minus_sign:                                             | N/A                                                            |