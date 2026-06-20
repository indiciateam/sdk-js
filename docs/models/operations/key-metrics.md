# KeyMetrics

## Example Usage

```typescript
import { KeyMetrics } from "@indiciaosint/sdk/models/operations";

let value: KeyMetrics = {
  accountStatistics: {
    followersCount: 5298.61,
    followingCount: 4008.45,
    totalLikesReceivedOnAllVideos: 6375.39,
  },
  averagePerformancePerVideo: {
    avgComments: 2130.95,
    avgFavorites: 9364.68,
    avgLikes: 9894.1,
    avgShares: 999.99,
    avgViews: 2700.03,
  },
  engagementRatios: {
    commentToViewRatio: "<value>",
    engagementRatePerFollower: {
      explanation: "<value>",
      value: "<value>",
    },
    engagementRatePerView: {
      explanation: "<value>",
      value: "<value>",
    },
    favoriteToViewRatio: "<value>",
    likeToViewRatio: "<value>",
    shareToViewRatio: "<value>",
  },
  performanceSummaryAcrossAnalyzedVideos: {
    totalComments: 408.43,
    totalFavorites: 7953.15,
    totalLikes: 4774.15,
    totalShares: 8240.83,
    totalVideosAnalyzed: 487.42,
    totalViews: 4471.69,
  },
};
```

## Fields

| Field                                                                                                                      | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `accountStatistics`                                                                                                        | [operations.AccountStatistics](../../models/operations/account-statistics.md)                                              | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `averagePerformancePerVideo`                                                                                               | [operations.AveragePerformancePerVideo](../../models/operations/average-performance-per-video.md)                          | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `engagementRatios`                                                                                                         | [operations.EngagementRatios](../../models/operations/engagement-ratios.md)                                                | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `performanceSummaryAcrossAnalyzedVideos`                                                                                   | [operations.PerformanceSummaryAcrossAnalyzedVideos](../../models/operations/performance-summary-across-analyzed-videos.md) | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |