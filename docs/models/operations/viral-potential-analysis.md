# ViralPotentialAnalysis

## Example Usage

```typescript
import { ViralPotentialAnalysis } from "@indiciaosint/sdk/models/operations";

let value: ViralPotentialAnalysis = {
  explanation: "<value>",
  result: {
    assessment: "<value>",
    bestPerformingVideo: {
      likes: 9780.35,
      videoId: "<id>",
      views: 4520.3,
    },
    factors: [
      "<value 1>",
      "<value 2>",
    ],
    score: 8757.35,
    viralVideosCount: 1491.05,
  },
};
```

## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `explanation`                                                                                         | *string*                                                                                              | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `result`                                                                                              | [operations.ViralPotentialAnalysisResult](../../models/operations/viral-potential-analysis-result.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |