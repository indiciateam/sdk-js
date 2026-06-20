# Cloudsint

## Example Usage

```typescript
import { Cloudsint } from "@indiciaosint/sdk/models/operations";

let value: Cloudsint = {
  data: {
    breaches: [],
    query: "<value>",
    totalMatches: 1630.65,
    type: "username",
  },
  duration: 2978.57,
  success: false,
};
```

## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `data`                                                                                    | [operations.SearchWebDatabasesData](../../models/operations/search-web-databases-data.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `duration`                                                                                | *number*                                                                                  | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `success`                                                                                 | *boolean*                                                                                 | :heavy_check_mark:                                                                        | N/A                                                                                       |