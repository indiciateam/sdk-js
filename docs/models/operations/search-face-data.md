# SearchFaceData

Completed facial search result set.

## Example Usage

```typescript
import { SearchFaceData } from "@indiciaosint/sdk/models/operations";

let value: SearchFaceData = {
  time: 7019.03,
  results: [
    {
      id: "<id>",
      hash: "<value>",
      group: 72.52,
      quality: 4432,
      imageUrl: "https://gullible-supplier.com/",
      crawledAt: 5203.06,
      sourceUrl: "https://ambitious-impact.net",
      thumbnailUrl: "https://grumpy-confusion.org/",
    },
  ],
  searchHash: "<value>",
  numberOfResults: 6304.05,
};
```

## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `time`                                                                         | *number*                                                                       | :heavy_check_mark:                                                             | Time the search took, in seconds.                                              |
| `results`                                                                      | [operations.SearchFaceResult](../../models/operations/search-face-result.md)[] | :heavy_check_mark:                                                             | Matched faces found across the internet.                                       |
| `searchHash`                                                                   | *string*                                                                       | :heavy_check_mark:                                                             | Hash identifying this search.                                                  |
| `numberOfResults`                                                              | *number*                                                                       | :heavy_check_mark:                                                             | Total number of matched faces.                                                 |