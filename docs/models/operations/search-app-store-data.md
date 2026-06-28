# SearchAppStoreData

## Example Usage

```typescript
import { SearchAppStoreData } from "@indiciaosint/sdk/models/operations";

let value: SearchAppStoreData = {
  apps: [],
  query: "<value>",
  store: "google",
};
```

## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `apps`                                                                | [operations.App](../../models/operations/app.md)[]                    | :heavy_check_mark:                                                    | N/A                                                                   |
| `query`                                                               | *string*                                                              | :heavy_check_mark:                                                    | N/A                                                                   |
| `store`                                                               | [operations.StoreResponse](../../models/operations/store-response.md) | :heavy_check_mark:                                                    | N/A                                                                   |