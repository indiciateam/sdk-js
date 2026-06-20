# ShadowBanRiskAssessment

## Example Usage

```typescript
import { ShadowBanRiskAssessment } from "@indiciaosint/sdk/models/operations";

let value: ShadowBanRiskAssessment = {
  explanation: "<value>",
  result: {
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
  },
};
```

## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `explanation`                                                                                            | *string*                                                                                                 | :heavy_check_mark:                                                                                       | N/A                                                                                                      |
| `result`                                                                                                 | [operations.ShadowBanRiskAssessmentResult](../../models/operations/shadow-ban-risk-assessment-result.md) | :heavy_check_mark:                                                                                       | N/A                                                                                                      |