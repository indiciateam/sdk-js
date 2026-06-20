# DetailedMetrics

## Example Usage

```typescript
import { DetailedMetrics } from "@indiciaosint/sdk/models/operations";

let value: DetailedMetrics = {
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
};
```

## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `historicalPerformance`                                                               | [operations.HistoricalPerformance](../../models/operations/historical-performance.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `recentPerformance`                                                                   | [operations.RecentPerformance](../../models/operations/recent-performance.md)         | :heavy_check_mark:                                                                    | N/A                                                                                   |