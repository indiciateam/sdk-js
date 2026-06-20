# PostV1SearchIntelligencePhoneResponse

Search successful

## Example Usage

```typescript
import { PostV1SearchIntelligencePhoneResponse } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligencePhoneResponse = {
  data: {
    local: [],
    phone: {
      countryCode: "RU",
      nationalFormat: "<value>",
      phoneNumber: "356-326-3551 x7561",
      valid: false,
    },
    web: [],
  },
  success: false,
};
```

## Fields

| Field                                                                                                             | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                            | [operations.PostV1SearchIntelligencePhoneData](../../models/operations/post-v1-search-intelligence-phone-data.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `success`                                                                                                         | *boolean*                                                                                                         | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `error`                                                                                                           | *string*                                                                                                          | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |