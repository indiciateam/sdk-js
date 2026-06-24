# OsintResult

A single service's username lookup result.

## Example Usage

```typescript
import { OsintResult } from "@indiciaosint/sdk/models/operations";

let value: OsintResult = {
  durationMs: 410.39,
  exists: false,
  service: "<value>",
  type: "username",
};
```

## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `durationMs`                                                                     | *number*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `exists`                                                                         | *boolean*                                                                        | :heavy_check_mark:                                                               | N/A                                                                              |
| `service`                                                                        | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `type`                                                                           | [operations.SearchUsernameType](../../models/operations/search-username-type.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `data`                                                                           | [operations.SearchUsernameData](../../models/operations/search-username-data.md) | :heavy_minus_sign:                                                               | N/A                                                                              |
| `error`                                                                          | *string*                                                                         | :heavy_minus_sign:                                                               | N/A                                                                              |