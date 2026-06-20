# Osintindustry

## Example Usage

```typescript
import { Osintindustry } from "@indiciaosint/sdk/models/operations";

let value: Osintindustry = {
  data: {
    "key": "<value>",
    "key1": "<value>",
    "key2": "<value>",
  },
  frontSchemas: [],
  module: "<value>",
  reliableSource: true,
  specFormat: [],
  status: "found",
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `data`                                                                                        | Record<string, *any*>                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `frontSchemas`                                                                                | [operations.FrontSchema](../../models/operations/front-schema.md)[]                           | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `module`                                                                                      | *string*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `reliableSource`                                                                              | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `specFormat`                                                                                  | [operations.SpecFormat](../../models/operations/spec-format.md)[]                             | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `status`                                                                                      | [operations.SearchWebDatabasesStatus](../../models/operations/search-web-databases-status.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `category`                                                                                    | [operations.Category](../../models/operations/category.md)                                    | :heavy_minus_sign:                                                                            | N/A                                                                                           |