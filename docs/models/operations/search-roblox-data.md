# SearchRobloxData

## Example Usage

```typescript
import { SearchRobloxData } from "@indiciaosint/sdk/models/operations";

let value: SearchRobloxData = {
  type: "<value>",
};
```

## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `type`                                                                             | *string*                                                                           | :heavy_check_mark:                                                                 | N/A                                                                                |
| `altAccountThumbnails`                                                             | Record<string, *string*>                                                           | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `altAccounts`                                                                      | [operations.AltAccounts](../../models/operations/alt-accounts.md)                  | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `leaks`                                                                            | *any*                                                                              | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `profile`                                                                          | [operations.SearchRobloxProfile](../../models/operations/search-roblox-profile.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `stealers`                                                                         | *operations.Stealer*[]                                                             | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `verified`                                                                         | *boolean*                                                                          | :heavy_minus_sign:                                                                 | N/A                                                                                |