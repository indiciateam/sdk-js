# Leakosint

## Example Usage

```typescript
import { Leakosint } from "@indiciaosint/sdk/models/operations";

let value: Leakosint = {
  list: {
    "key": {
      data: [
        {},
      ],
      infoLeak: "<value>",
      numOfResults: 8990.14,
    },
  },
  numOfDatabase: 2695.49,
  numOfResults: 7317,
  price: 8195.39,
  searchTime: 161.66,
};
```

## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `list`                                                                                                    | Record<string, [operations.SearchWebDatabasesList](../../models/operations/search-web-databases-list.md)> | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `numOfDatabase`                                                                                           | *number*                                                                                                  | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `numOfResults`                                                                                            | *number*                                                                                                  | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `price`                                                                                                   | *number*                                                                                                  | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `searchTime`                                                                                              | *number*                                                                                                  | :heavy_check_mark:                                                                                        | N/A                                                                                                       |