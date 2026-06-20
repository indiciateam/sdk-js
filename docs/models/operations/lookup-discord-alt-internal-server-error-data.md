# LookupDiscordAltInternalServerErrorData

## Example Usage

```typescript
import { LookupDiscordAltInternalServerErrorData } from "@indiciaosint/sdk/models/operations";

let value: LookupDiscordAltInternalServerErrorData = {
  first: [
    {
      avatar: "https://loremflickr.com/2747/3555?lock=6489634474108863",
      id: "<id>",
      username: "Murray.Fahey",
    },
  ],
  second: [
    {
      avatar: "https://picsum.photos/seed/Wnv5J/1595/3491",
      id: "<id>",
      username: "Teagan82",
    },
  ],
  third: [],
  tier: "<value>",
  totalalts: 3026.13,
  verifications: 6263.48,
  vpns: 4849.78,
};
```

## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `first`                                                                                           | [operations.InternalServerErrorFirst](../../models/operations/internal-server-error-first.md)[]   | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `second`                                                                                          | [operations.InternalServerErrorSecond](../../models/operations/internal-server-error-second.md)[] | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `third`                                                                                           | [operations.InternalServerErrorThird](../../models/operations/internal-server-error-third.md)[]   | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `tier`                                                                                            | *string*                                                                                          | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `totalalts`                                                                                       | *number*                                                                                          | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `verifications`                                                                                   | *number*                                                                                          | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `vpns`                                                                                            | *number*                                                                                          | :heavy_check_mark:                                                                                | N/A                                                                                               |