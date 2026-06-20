# ExtendedData

## Example Usage

```typescript
import { ExtendedData } from "@indiciaosint/sdk/models/operations";

let value: ExtendedData = {
  dynamiteData: {
    customerId: "<id>",
    dndState: "<value>",
    entityType: "<value>",
    presence: "<value>",
  },
  gplusData: {
    contentRestriction: "<value>",
    isEntrepriseUser: true,
  },
};
```

## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dynamiteData`                                                      | [operations.DynamiteData](../../models/operations/dynamite-data.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `gplusData`                                                         | [operations.GplusData](../../models/operations/gplus-data.md)       | :heavy_check_mark:                                                  | N/A                                                                 |