# CloudsintData

## Example Usage

```typescript
import { CloudsintData } from "@indiciaosint/sdk/models/operations";

let value: CloudsintData = {
  breaches: [
    {
      id: "<id>",
    },
  ],
  query: "<value>",
  totalMatches: 8540.7,
};
```

## Fields

| Field                                                                                           | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `breaches`                                                                                      | [operations.SearchWebDatabasesBreach](../../models/operations/search-web-databases-breach.md)[] | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `query`                                                                                         | *string*                                                                                        | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `totalMatches`                                                                                  | *number*                                                                                        | :heavy_check_mark:                                                                              | N/A                                                                                             |