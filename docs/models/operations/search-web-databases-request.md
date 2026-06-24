# SearchWebDatabasesRequest

## Example Usage

```typescript
import { SearchWebDatabasesRequest } from "@indiciaosint/sdk/models/operations";

let value: SearchWebDatabasesRequest = {
  query: "<value>",
  services: [],
};
```

## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `query`                                                                                           | *string*                                                                                          | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `services`                                                                                        | [operations.SearchWebDatabasesService](../../models/operations/search-web-databases-service.md)[] | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `cloudsintType`                                                                                   | [operations.CloudsintType](../../models/operations/cloudsint-type.md)                             | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `intelxType`                                                                                      | [operations.IntelxType](../../models/operations/intelx-type.md)                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `leakCheckType`                                                                                   | [operations.LeakCheckType](../../models/operations/leak-check-type.md)                            | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `snusbaseType`                                                                                    | [operations.SnusbaseType](../../models/operations/snusbase-type.md)                               | :heavy_minus_sign:                                                                                | N/A                                                                                               |