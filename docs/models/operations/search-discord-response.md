# SearchDiscordResponse

Search successful

## Example Usage

```typescript
import { SearchDiscordResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchDiscordResponse = {
  data: {
    internalErrors: [
      "<value 1>",
      "<value 2>",
    ],
  },
  success: false,
};
```

## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `data`                                                                         | [operations.SearchDiscordData](../../models/operations/search-discord-data.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `success`                                                                      | *boolean*                                                                      | :heavy_check_mark:                                                             | N/A                                                                            |
| `error`                                                                        | *string*                                                                       | :heavy_minus_sign:                                                             | N/A                                                                            |