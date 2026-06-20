# PostV1SearchIntelligenceEmailResponse

Search successful

## Example Usage

```typescript
import { PostV1SearchIntelligenceEmailResponse } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligenceEmailResponse = {
  data: [
    {
      aka: [
        "<value 1>",
        "<value 2>",
        "<value 3>",
      ],
      associates: [],
      children: 33.39,
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
      ],
      phones: [
        "<value 1>",
      ],
    },
  ],
  success: true,
};
```

## Fields

| Field                                                                                                               | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                              | [operations.PostV1SearchIntelligenceEmailData](../../models/operations/post-v1-search-intelligence-email-data.md)[] | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `success`                                                                                                           | *boolean*                                                                                                           | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `error`                                                                                                             | *string*                                                                                                            | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |