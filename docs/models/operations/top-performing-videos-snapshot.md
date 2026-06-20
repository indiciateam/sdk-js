# TopPerformingVideosSnapshot

## Example Usage

```typescript
import { TopPerformingVideosSnapshot } from "@indiciaosint/sdk/models/operations";

let value: TopPerformingVideosSnapshot = {
  byComments: [
    {
      createdDate: "<value>",
      description: "providence meh live frightfully",
      engagementRate: "<value>",
      value: 4526.87,
      videoId: "<id>",
      videoUrl: "https://bulky-tool.info",
    },
  ],
  byLikes: [
    {
      createdDate: "<value>",
      description: "hm unexpectedly circumnavigate",
      engagementRate: "<value>",
      value: 8302.56,
      videoId: "<id>",
      videoUrl: "https://bustling-stock.com/",
    },
  ],
  byShares: [],
  byViews: [
    {
      createdDate: "<value>",
      description: "nor blah free since crooked drum viability psst",
      engagementRate: "<value>",
      value: 2802.1,
      videoId: "<id>",
      videoUrl: "https://authentic-alligator.net/",
    },
  ],
};
```

## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `byComments`                                                    | [operations.ByComment](../../models/operations/by-comment.md)[] | :heavy_check_mark:                                              | N/A                                                             |
| `byLikes`                                                       | [operations.ByLike](../../models/operations/by-like.md)[]       | :heavy_check_mark:                                              | N/A                                                             |
| `byShares`                                                      | [operations.ByShare](../../models/operations/by-share.md)[]     | :heavy_check_mark:                                              | N/A                                                             |
| `byViews`                                                       | [operations.ByView](../../models/operations/by-view.md)[]       | :heavy_check_mark:                                              | N/A                                                             |