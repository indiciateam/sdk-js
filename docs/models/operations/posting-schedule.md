# PostingSchedule

## Example Usage

```typescript
import { PostingSchedule } from "@indiciaosint/sdk/models/operations";

let value: PostingSchedule = {
  mostActiveDay: "<value>",
  mostActiveHourUtc: "<value>",
  optimalPostingDay: "<value>",
  optimalPostingHourUtc: "<value>",
  performanceByDay: {},
  performanceByHour: {
    "key": {
      avgViews: 1551.22,
      posts: 7149.59,
      totalEngagement: 2396.05,
      totalViews: 8525.03,
    },
  },
  postingHeatmapDayVsHourUtc: {
    "key": {},
  },
};
```

## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `mostActiveDay`                                                                                | *string*                                                                                       | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `mostActiveHourUtc`                                                                            | *string*                                                                                       | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `optimalPostingDay`                                                                            | *string*                                                                                       | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `optimalPostingHourUtc`                                                                        | *string*                                                                                       | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `performanceByDay`                                                                             | Record<string, [operations.PerformanceByDay](../../models/operations/performance-by-day.md)>   | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `performanceByHour`                                                                            | Record<string, [operations.PerformanceByHour](../../models/operations/performance-by-hour.md)> | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `postingHeatmapDayVsHourUtc`                                                                   | Record<string, Record<string, *number*>>                                                       | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `postingFrequency`                                                                             | [operations.PostingFrequency](../../models/operations/posting-frequency.md)                    | :heavy_minus_sign:                                                                             | N/A                                                                                            |