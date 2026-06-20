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

| Field                                                                                                                | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                               | [operations.PostV1SearchIntelligenceWebDbsData](../../models/operations/post-v1-search-intelligence-web-dbs-data.md) | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  |
| `duration`                                                                                                           | *number*                                                                                                             | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  |
| `success`                                                                                                            | *boolean*                                                                                                            | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  |