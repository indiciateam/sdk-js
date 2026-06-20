# SearchEmailResponse

Search successful

## Example Usage

```typescript
import { SearchEmailResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchEmailResponse = {
  data: {
    web: [
      {},
    ],
  },
  success: true,
};
```

## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `data`                                                                     | [operations.SearchEmailData](../../models/operations/search-email-data.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `success`                                                                  | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `error`                                                                    | *string*                                                                   | :heavy_minus_sign:                                                         | N/A                                                                        |