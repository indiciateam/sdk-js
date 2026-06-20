# SearchUsernameResponse

Search successful

## Example Usage

```typescript
import { SearchUsernameResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchUsernameResponse = {
  data: [
    {
      durationMs: 5996.5,
      exists: true,
      service: "<value>",
      type: "username",
    },
  ],
  success: true,
};
```

## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `data`                                                                             | [operations.SearchUsernameData](../../models/operations/search-username-data.md)[] | :heavy_check_mark:                                                                 | N/A                                                                                |
| `success`                                                                          | *boolean*                                                                          | :heavy_check_mark:                                                                 | N/A                                                                                |
| `error`                                                                            | *string*                                                                           | :heavy_minus_sign:                                                                 | N/A                                                                                |