# ResultsEvent

Emitted as the `results` event with the completed matches.

## Example Usage

```typescript
import { ResultsEvent } from "@indiciaosint/sdk/models/operations";

let value: ResultsEvent = {
  data: {
    time: 5092.5,
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
    numberOfResults: 7699.05,
  },
  event: "results",
};
```

## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `data`                                                                   | [operations.SearchFaceData](../../models/operations/search-face-data.md) | :heavy_check_mark:                                                       | Completed facial search result set.                                      |
| `event`                                                                  | *"results"*                                                              | :heavy_check_mark:                                                       | N/A                                                                      |