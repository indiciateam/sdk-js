# ViralPotentialAnalysisResult

## Example Usage

```typescript
import { ViralPotentialAnalysisResult } from "@indiciaosint/sdk/models/operations";

let value: ViralPotentialAnalysisResult = {
  assessment: "<value>",
  bestPerformingVideo: {
    likes: 9780.35,
    videoId: "<id>",
    views: 4520.3,
  },
  factors: [],
  score: 4201.22,
  viralVideosCount: 7430.03,
};
```

## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `assessment`                                                                       | *string*                                                                           | :heavy_check_mark:                                                                 | N/A                                                                                |
| `bestPerformingVideo`                                                              | [operations.BestPerformingVideo](../../models/operations/best-performing-video.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `factors`                                                                          | *string*[]                                                                         | :heavy_check_mark:                                                                 | N/A                                                                                |
| `score`                                                                            | *number*                                                                           | :heavy_check_mark:                                                                 | N/A                                                                                |
| `viralVideosCount`                                                                 | *number*                                                                           | :heavy_check_mark:                                                                 | N/A                                                                                |