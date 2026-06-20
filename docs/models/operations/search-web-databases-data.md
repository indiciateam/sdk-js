# SearchWebDatabasesData

## Example Usage

```typescript
import { SearchWebDatabasesData } from "@indiciaosint/sdk/models/operations";

let value: SearchWebDatabasesData = {
  breaches: [
    {
      email: "Wilfredo.Cruickshank63@hotmail.com",
      id: "<id>",
      importedAt: "<value>",
      password: "Fl90nD2brYOJTnG",
      source: "<value>",
      sourceDate: "<value>",
      sourceName: "<value>",
      url: "https://gray-boyfriend.org",
      username: "Rudolph.Jacobson",
    },
  ],
  query: "<value>",
  totalMatches: 9362.92,
  type: "steamid",
};
```

## Fields

| Field                                                                                           | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `breaches`                                                                                      | [operations.SearchWebDatabasesBreach](../../models/operations/search-web-databases-breach.md)[] | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `query`                                                                                         | *string*                                                                                        | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `totalMatches`                                                                                  | *number*                                                                                        | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `type`                                                                                          | [operations.CloudsintTypeResponse](../../models/operations/cloudsint-type-response.md)          | :heavy_check_mark:                                                                              | N/A                                                                                             |