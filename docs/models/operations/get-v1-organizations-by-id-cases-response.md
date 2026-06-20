# GetV1OrganizationsByIdCasesResponse

Shared cases.

## Example Usage

```typescript
import { GetV1OrganizationsByIdCasesResponse } from "@indiciaosint/sdk/models/operations";

let value: GetV1OrganizationsByIdCasesResponse = {
  cases: [
    {
      createdAt: 591488,
      description: "chap pastel anenst confute fatally obediently CD at",
      id: "<id>",
      name: "<value>",
      organizationId: "<id>",
      owner: "<value>",
    },
  ],
  success: true,
};
```

## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `cases`                                              | [operations.Case](../../models/operations/case.md)[] | :heavy_check_mark:                                   | N/A                                                  |
| `success`                                            | *boolean*                                            | :heavy_check_mark:                                   | N/A                                                  |