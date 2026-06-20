# Stealer

## Example Usage

```typescript
import { Stealer } from "@indiciaosint/sdk/models/operations";

let value: Stealer = {
  computerName: "<value>",
  dateCompromised: "<value>",
  ip: "8cc2:6d70:b836:edbc:bc9c:58d2:150a:cd3d",
  malwarePath: "<value>",
  operatingSystem: "Windows",
  topLogins: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
  topPasswords: [
    "<value 1>",
    "<value 2>",
  ],
  totalCorporateServices: 9977.25,
  totalUserServices: 7805.6,
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