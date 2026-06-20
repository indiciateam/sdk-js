# SearchUsernameData

## Example Usage

```typescript
import { SearchUsernameData } from "@indiciaosint/sdk/models/operations";

let value: SearchUsernameData = {
  durationMs: 5119.71,
  exists: true,
  service: "<value>",
  type: "username",
};
```

## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `durationMs`                                                                              | *number*                                                                                  | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `exists`                                                                                  | *boolean*                                                                                 | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `service`                                                                                 | *string*                                                                                  | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `type`                                                                                    | [operations.SearchUsernameType](../../models/operations/search-username-type.md)          | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `data`                                                                                    | [operations.SearchUsernameDataData](../../models/operations/search-username-data-data.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `error`                                                                                   | *string*                                                                                  | :heavy_minus_sign:                                                                        | N/A                                                                                       |