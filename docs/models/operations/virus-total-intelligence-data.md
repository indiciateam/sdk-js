# VirusTotalIntelligenceData

## Example Usage

```typescript
import { VirusTotalIntelligenceData } from "@indiciaosint/sdk/models/operations";

let value: VirusTotalIntelligenceData = {
  entity: "<value>",
  files: [],
  query: "<value>",
  totalResults: 8303.08,
};
```

## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `entity`                                                                                            | *string*                                                                                            | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `files`                                                                                             | [operations.VirusTotalIntelligenceFile](../../models/operations/virus-total-intelligence-file.md)[] | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `query`                                                                                             | *string*                                                                                            | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `totalResults`                                                                                      | *number*                                                                                            | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `searchStats`                                                                                       | [operations.SearchStats](../../models/operations/search-stats.md)                                   | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |