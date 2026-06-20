# FrontSchema

## Example Usage

```typescript
import { FrontSchema } from "@indiciaosint/sdk/models/operations";

let value: FrontSchema = {
  body: {},
  image: "https://picsum.photos/seed/FyXCsDih/2774/1116",
  module: "<value>",
  tags: [
    "<value 1>",
    "<value 2>",
  ],
  timeline: {
    groupItems: {
      "key": "<value>",
    },
    groupYears: {},
    groups: {},
    lastSeen: true,
    lastSeenDate: "<value>",
    registered: false,
    registeredDate: "<value>",
  },
};
```

## Fields

| Field                                                                                                                        | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                       | [operations.Body](../../models/operations/body.md)                                                                           | :heavy_check_mark:                                                                                                           | N/A                                                                                                                          |
| `image`                                                                                                                      | *string*                                                                                                                     | :heavy_check_mark:                                                                                                           | N/A                                                                                                                          |
| `module`                                                                                                                     | *string*                                                                                                                     | :heavy_check_mark:                                                                                                           | N/A                                                                                                                          |
| `tags`                                                                                                                       | *string*[]                                                                                                                   | :heavy_check_mark:                                                                                                           | N/A                                                                                                                          |
| `timeline`                                                                                                                   | [operations.PostV1SearchIntelligenceWebDbsTimeline](../../models/operations/post-v1-search-intelligence-web-dbs-timeline.md) | :heavy_check_mark:                                                                                                           | N/A                                                                                                                          |