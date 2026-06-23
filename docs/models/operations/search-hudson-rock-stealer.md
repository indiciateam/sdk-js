# SearchHudsonRockStealer

## Example Usage

```typescript
import { SearchHudsonRockStealer } from "@indiciaosint/sdk/models/operations";

let value: SearchHudsonRockStealer = {
  computerName: "<value>",
  dateCompromised: "<value>",
  ip: "ffaa:a9ef:376a:d631:c73f:fdcc:4cd7:e04f",
  malwarePath: "<value>",
  operatingSystem: "Linux",
  topLogins: [],
  topPasswords: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
  totalCorporateServices: 2903.46,
  totalUserServices: 4493.5,
};
```

## Fields

| Field                    | Type                     | Required                 | Description              |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `computerName`           | *string*                 | :heavy_check_mark:       | N/A                      |
| `dateCompromised`        | *string*                 | :heavy_check_mark:       | N/A                      |
| `ip`                     | *string*                 | :heavy_check_mark:       | N/A                      |
| `malwarePath`            | *string*                 | :heavy_check_mark:       | N/A                      |
| `operatingSystem`        | *string*                 | :heavy_check_mark:       | N/A                      |
| `topLogins`              | *string*[]               | :heavy_check_mark:       | N/A                      |
| `topPasswords`           | *string*[]               | :heavy_check_mark:       | N/A                      |
| `totalCorporateServices` | *number*                 | :heavy_check_mark:       | N/A                      |
| `totalUserServices`      | *number*                 | :heavy_check_mark:       | N/A                      |
| `stealerFamily`          | *string*                 | :heavy_minus_sign:       | N/A                      |