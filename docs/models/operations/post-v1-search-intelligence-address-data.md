# PostV1SearchIntelligenceAddressData

## Example Usage

```typescript
import { PostV1SearchIntelligenceAddressData } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligenceAddressData = {
  local: [],
  web: [
    {
      aka: [],
      associates: [
        "<value 1>",
        "<value 2>",
      ],
      children: 7980.37,
      currentAddress: "<value>",
      emails: [],
      maritalStatus: "<value>",
      name: "<value>",
      pastAddresses: [
        "<value 1>",
        "<value 2>",
        "<value 3>",
      ],
      phones: [
        "<value 1>",
        "<value 2>",
        "<value 3>",
      ],
    },
  ],
};
```

## Fields

| Field                                                                                                                     | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `local`                                                                                                                   | [operations.PostV1SearchIntelligenceAddressLocal](../../models/operations/post-v1-search-intelligence-address-local.md)[] | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `web`                                                                                                                     | [operations.PostV1SearchIntelligenceAddressWeb](../../models/operations/post-v1-search-intelligence-address-web.md)[]     | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |