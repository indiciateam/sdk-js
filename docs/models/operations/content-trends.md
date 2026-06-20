# ContentTrends

## Example Usage

```typescript
import { ContentTrends } from "@indiciaosint/sdk/models/operations";

let value: ContentTrends = {
  contentConsistencyScore: 2789.15,
  recentPopularHashtags: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
  trendingHashtags: [],
};
```

## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `contentConsistencyScore`                                                   | *number*                                                                    | :heavy_check_mark:                                                          | N/A                                                                         |
| `recentPopularHashtags`                                                     | *string*[]                                                                  | :heavy_check_mark:                                                          | N/A                                                                         |
| `trendingHashtags`                                                          | [operations.TrendingHashtag](../../models/operations/trending-hashtag.md)[] | :heavy_check_mark:                                                          | N/A                                                                         |