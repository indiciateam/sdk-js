# VirusTotalIntelligenceResponse

Search successful

## Example Usage

```typescript
import { VirusTotalIntelligenceResponse } from "@indiciaosint/sdk/models/operations";

let value: VirusTotalIntelligenceResponse = {
  data: {
    entity: "<value>",
    files: [],
    query: "<value>",
    totalResults: 5350.14,
  },
  success: false,
};
```

## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `data`                                                                                            | [operations.VirusTotalIntelligenceData](../../models/operations/virus-total-intelligence-data.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `success`                                                                                         | *boolean*                                                                                         | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `error`                                                                                           | *string*                                                                                          | :heavy_minus_sign:                                                                                | N/A                                                                                               |