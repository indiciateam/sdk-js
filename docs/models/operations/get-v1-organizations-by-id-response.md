# GetV1OrganizationsByIdResponse

Organization details.

## Example Usage

```typescript
import { GetV1OrganizationsByIdResponse } from "@indiciaosint/sdk/models/operations";

let value: GetV1OrganizationsByIdResponse = {
  organization: {
    createdAt: 343634,
    defaultCaseVisibility: "<value>",
    description:
      "millet the nectarine as miserably knowledgeable compassionate awkwardly continually",
    id: "<id>",
    logo: "<value>",
    memberCount: 4875.21,
    myRole: "<value>",
    name: "<value>",
    slug: "<value>",
  },
  success: true,
};
```

## Fields

| Field                                                                                                               | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `organization`                                                                                                      | [operations.GetV1OrganizationsByIdOrganization](../../models/operations/get-v1-organizations-by-id-organization.md) | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `success`                                                                                                           | *boolean*                                                                                                           | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |