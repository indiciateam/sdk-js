# SearchShodanResponse

Search successful

## Example Usage

```typescript
import { SearchShodanResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchShodanResponse = {
  data: {
    matches: [],
    total: 4169.53,
  },
  success: false,
};
```

## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `data`                                                                       | [operations.SearchShodanData](../../models/operations/search-shodan-data.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `success`                                                                    | *boolean*                                                                    | :heavy_check_mark:                                                           | N/A                                                                          |
| `error`                                                                      | *string*                                                                     | :heavy_minus_sign:                                                           | N/A                                                                          |