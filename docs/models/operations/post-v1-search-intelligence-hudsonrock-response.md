# PostV1SearchIntelligenceHudsonrockResponse

Search successful

## Example Usage

```typescript
import { PostV1SearchIntelligenceHudsonrockResponse } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligenceHudsonrockResponse = {
  data: {
    message: "<value>",
    stealers: [
      {
        computerName: "<value>",
        dateCompromised: "<value>",
        ip: "7be7:c098:27f9:ffd5:ccad:34dd:53cf:24eb",
        malwarePath: "<value>",
        operatingSystem: "WebOS",
        topLogins: [
          "<value 1>",
        ],
        topPasswords: [
          "<value 1>",
        ],
        totalCorporateServices: 675.53,
        totalUserServices: 8711.64,
      },
    ],
    type: "username",
  },
  success: false,
};
```

## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `data`                                                   | *operations.PostV1SearchIntelligenceHudsonrockDataUnion* | :heavy_check_mark:                                       | N/A                                                      |
| `success`                                                | *boolean*                                                | :heavy_check_mark:                                       | N/A                                                      |
| `error`                                                  | *string*                                                 | :heavy_minus_sign:                                       | N/A                                                      |