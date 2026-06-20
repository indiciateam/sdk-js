# ShadowBanRiskAssessmentResult

## Example Usage

```typescript
import { ShadowBanRiskAssessmentResult } from "@indiciaosint/sdk/models/operations";

let value: ShadowBanRiskAssessmentResult = {
  assessment: "<value>",
  confidenceLevel: "<value>",
  detailedMetrics: {
    historicalPerformance: {
      avgComments: 9393.94,
      avgLikes: 5312.57,
      avgShares: 916.92,
      avgViews: 3366.5,
      engagementRate: "<value>",
    },
    recentPerformance: {
      avgComments: 9786.01,
      avgLikes: 1623.61,
      avgShares: 9749.67,
      avgViews: 7057.14,
      engagementRate: "<value>",
    },
  },
  probabilityPercentage: "<value>",
  reasoning: "<value>",
};
```

## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `assessment`                                                              | *string*                                                                  | :heavy_check_mark:                                                        | N/A                                                                       |
| `confidenceLevel`                                                         | *string*                                                                  | :heavy_check_mark:                                                        | N/A                                                                       |
| `detailedMetrics`                                                         | [operations.DetailedMetrics](../../models/operations/detailed-metrics.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `probabilityPercentage`                                                   | *string*                                                                  | :heavy_check_mark:                                                        | N/A                                                                       |
| `reasoning`                                                               | *string*                                                                  | :heavy_check_mark:                                                        | N/A                                                                       |