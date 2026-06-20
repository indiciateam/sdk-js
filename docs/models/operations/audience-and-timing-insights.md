# AudienceAndTimingInsights

## Example Usage

```typescript
import { AudienceAndTimingInsights } from "@indiciaosint/sdk/models/operations";

let value: AudienceAndTimingInsights = {
  geoIndicators: {
    top10LanguagesInDescription: [],
    top10RegionsFromVideos: [
      "<value 1>",
    ],
  },
  postingSchedule: {
    mostActiveDay: "<value>",
    mostActiveHourUtc: "<value>",
    optimalPostingDay: "<value>",
    optimalPostingHourUtc: "<value>",
    performanceByDay: {
      "key": {
        avgViews: 8251.88,
        posts: 6023.58,
        totalEngagement: 828.19,
        totalViews: 9707.08,
      },
    },
    performanceByHour: {
      "key": {
        avgViews: 1551.22,
        posts: 7149.59,
        totalEngagement: 2396.05,
        totalViews: 8525.03,
      },
    },
    postingHeatmapDayVsHourUtc: {
      "key": {
        "key": 1904.79,
        "key1": 297.64,
      },
    },
  },
};
```

## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `geoIndicators`                                                           | [operations.GeoIndicators](../../models/operations/geo-indicators.md)     | :heavy_check_mark:                                                        | N/A                                                                       |
| `postingSchedule`                                                         | [operations.PostingSchedule](../../models/operations/posting-schedule.md) | :heavy_check_mark:                                                        | N/A                                                                       |