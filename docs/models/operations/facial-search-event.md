# FacialSearchEvent

A Server-Sent Event. The `event:` field names the type ("faces" or "results"); errors are delivered as a data-only event.


## Supported Types

### `operations.FacesEvent`

```typescript
const value: operations.FacesEvent = {
  data: "<value>",
  event: "faces",
};
```

### `operations.ResultsEvent`

```typescript
const value: operations.ResultsEvent = {
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

### `operations.SearchFaceErrorEvent`

```typescript
const value: operations.SearchFaceErrorEvent = {
  data: {
    status: "error",
    success: false,
    error: "<value>",
  },
};
```

