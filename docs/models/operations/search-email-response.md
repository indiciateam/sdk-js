# SearchEmailResponse

Search successful

## Example Usage

```typescript
import { SearchEmailResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchEmailResponse = {
  data: [
    {
      aka: [
        "<value 1>",
      ],
      associates: [
        "<value 1>",
        "<value 2>",
      ],
      children: 3657.77,
      currentAddress: "<value>",
      emails: [
        "<value 1>",
        "<value 2>",
        "<value 3>",
      ],
      maritalStatus: "<value>",
      name: "<value>",
      pastAddresses: [],
      phones: [
        "<value 1>",
        "<value 2>",
      ],
    },
  ],
  success: false,
};
```

## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `data`                                                                       | [operations.SearchEmailData](../../models/operations/search-email-data.md)[] | :heavy_check_mark:                                                           | N/A                                                                          |
| `success`                                                                    | *boolean*                                                                    | :heavy_check_mark:                                                           | N/A                                                                          |
| `error`                                                                      | *string*                                                                     | :heavy_minus_sign:                                                           | N/A                                                                          |