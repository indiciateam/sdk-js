# SearchFaceErrorEvent

A data-only event indicating the search failed.

## Example Usage

```typescript
import { SearchFaceErrorEvent } from "@indiciaosint/sdk/models/operations";

let value: SearchFaceErrorEvent = {
  data: {
    status: "error",
    success: false,
    error: "<value>",
  },
};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `data`                                                        | [operations.DataError](../../models/operations/data-error.md) | :heavy_check_mark:                                            | N/A                                                           |