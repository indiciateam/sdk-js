# EngagementRatios

## Example Usage

```typescript
import { EngagementRatios } from "@indiciaosint/sdk/models/operations";

let value: EngagementRatios = {
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
};
```

## Fields

| Field                                                                                           | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `commentToViewRatio`                                                                            | *string*                                                                                        | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `engagementRatePerFollower`                                                                     | [operations.EngagementRatePerFollower](../../models/operations/engagement-rate-per-follower.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `engagementRatePerView`                                                                         | [operations.EngagementRatePerView](../../models/operations/engagement-rate-per-view.md)         | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `favoriteToViewRatio`                                                                           | *string*                                                                                        | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `likeToViewRatio`                                                                               | *string*                                                                                        | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `shareToViewRatio`                                                                              | *string*                                                                                        | :heavy_check_mark:                                                                              | N/A                                                                                             |