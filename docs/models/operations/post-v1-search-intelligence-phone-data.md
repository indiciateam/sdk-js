# PostV1SearchIntelligencePhoneData

## Example Usage

```typescript
import { PostV1SearchIntelligencePhoneData } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligencePhoneData = {
  local: [],
  phone: {
    countryCode: "RU",
    nationalFormat: "<value>",
    phoneNumber: "356-326-3551 x7561",
    valid: false,
  },
  web: [
    {
      aka: [
        "<value 1>",
      ],
      associates: [
        "<value 1>",
        "<value 2>",
      ],
      children: 8271.16,
      currentAddress: "<value>",
      emails: [
        "<value 1>",
        "<value 2>",
        "<value 3>",
      ],
      maritalStatus: "<value>",
      name: "<value>",
      pastAddresses: [
        "<value 1>",
        "<value 2>",
        "<value 3>",
      ],
      phones: [],
    },
  ],
};
```

## Fields

| Field                                                                                                                 | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `local`                                                                                                               | [operations.PostV1SearchIntelligencePhoneLocal](../../models/operations/post-v1-search-intelligence-phone-local.md)[] | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `phone`                                                                                                               | [operations.PostV1SearchIntelligencePhonePhone](../../models/operations/post-v1-search-intelligence-phone-phone.md)   | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `web`                                                                                                                 | [operations.PostV1SearchIntelligencePhoneWeb](../../models/operations/post-v1-search-intelligence-phone-web.md)[]     | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |