# ContentStrategyDeepDive

## Example Usage

```typescript
import { ContentStrategyDeepDive } from "@indiciaosint/sdk/models/operations";

let value: ContentStrategyDeepDive = {
  contentTrends: {
    contentConsistencyScore: 6996.97,
    recentPopularHashtags: [
      "<value 1>",
      "<value 2>",
    ],
    trendingHashtags: [],
  },
  top10EffectsUsed: [],
  top10MusicTitlesUsed: [
    "<value 1>",
  ],
  top15HashtagsUsed: [],
  videoLengthAnalysisSeconds: {
    averageDuration: 1070.81,
    longestDuration: 9008.83,
    optimalDurationRange: "<value>",
    shortestDuration: 5594.21,
  },
};
```

## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `contentTrends`                                                                                   | [operations.ContentTrends](../../models/operations/content-trends.md)                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `top10EffectsUsed`                                                                                | *string*[]                                                                                        | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `top10MusicTitlesUsed`                                                                            | *string*[]                                                                                        | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `top15HashtagsUsed`                                                                               | *string*[]                                                                                        | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `videoLengthAnalysisSeconds`                                                                      | [operations.VideoLengthAnalysisSeconds](../../models/operations/video-length-analysis-seconds.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |