# SearchFaceResult

## Example Usage

```typescript
import { SearchFaceResult } from "@indiciaosint/sdk/models/operations";

let value: SearchFaceResult = {
  id: "<id>",
  hash: "<value>",
  group: 6419.98,
  quality: 1222.86,
  imageUrl: "https://heavenly-ice-cream.org/",
  crawledAt: 9672,
  sourceUrl: "https://brave-produce.com",
  thumbnailUrl: "https://mediocre-derby.net/",
};
```

## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `id`                                            | *string*                                        | :heavy_check_mark:                              | N/A                                             |
| `hash`                                          | *string*                                        | :heavy_check_mark:                              | N/A                                             |
| `group`                                         | *number*                                        | :heavy_check_mark:                              | N/A                                             |
| `quality`                                       | *number*                                        | :heavy_check_mark:                              | N/A                                             |
| `imageUrl`                                      | *string*                                        | :heavy_check_mark:                              | N/A                                             |
| `crawledAt`                                     | *number*                                        | :heavy_check_mark:                              | Unix epoch milliseconds the source was crawled. |
| `sourceUrl`                                     | *string*                                        | :heavy_check_mark:                              | N/A                                             |
| `thumbnailUrl`                                  | *string*                                        | :heavy_check_mark:                              | N/A                                             |