# SearchPersonResponse

Search successful

## Example Usage

```typescript
import { SearchPersonResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchPersonResponse = {
  data: {
    local: [],
    web: [],
  },
  success: true,
};
```

## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `data`                                                                       | [operations.SearchPersonData](../../models/operations/search-person-data.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `success`                                                                    | *boolean*                                                                    | :heavy_check_mark:                                                           | N/A                                                                          |
| `error`                                                                      | *string*                                                                     | :heavy_minus_sign:                                                           | N/A                                                                          |