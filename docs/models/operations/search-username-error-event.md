# SearchUsernameErrorEvent

A data-only event indicating the search failed.

## Example Usage

```typescript
import { SearchUsernameErrorEvent } from "@indiciaosint/sdk/models/operations";

let value: SearchUsernameErrorEvent = {
  data: {
    status: "error",
    success: false,
    error: "<value>",
  },
};
```

## Fields

| Field                                                                                       | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `data`                                                                                      | [operations.SearchUsernameDataError](../../models/operations/search-username-data-error.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |