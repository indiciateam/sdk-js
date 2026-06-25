# VirusTotalContentResponse

Search successful

## Example Usage

```typescript
import { VirusTotalContentResponse } from "@indiciaosint/sdk/models/operations";

let value: VirusTotalContentResponse = {
  data: {
    files: [],
    searchQuery: "<value>",
    totalResults: 4197.11,
  },
  success: true,
};
```

## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `data`                                                                                  | [operations.VirusTotalContentData](../../models/operations/virus-total-content-data.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `success`                                                                               | *boolean*                                                                               | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `error`                                                                                 | *string*                                                                                | :heavy_minus_sign:                                                                      | N/A                                                                                     |