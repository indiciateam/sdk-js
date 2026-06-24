# SearchGithubErrorEvent

A data-only event indicating the search failed.

## Example Usage

```typescript
import { SearchGithubErrorEvent } from "@indiciaosint/sdk/models/operations";

let value: SearchGithubErrorEvent = {
  data: {
    status: "error",
    success: false,
    error: "<value>",
  },
};
```

## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `data`                                                                       | [operations.SearchGithubData](../../models/operations/search-github-data.md) | :heavy_check_mark:                                                           | N/A                                                                          |