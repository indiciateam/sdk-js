# ListOrganizationsResponse

List of organizations with member counts and your role.

## Example Usage

```typescript
import { ListOrganizationsResponse } from "@indiciaosint/sdk/models/operations";

let value: ListOrganizationsResponse = {
  organizations: [
    {
      createdAt: 326110,
      defaultCaseVisibility: "<value>",
      description: "behind suckle round past",
      id: "<id>",
      logo: "<value>",
      memberCount: 6571.06,
      myRole: "<value>",
      name: "<value>",
      slug: "<value>",
    },
  ],
  success: false,
};
```

## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `organizations`                                                                                          | [operations.ListOrganizationsOrganization](../../models/operations/list-organizations-organization.md)[] | :heavy_check_mark:                                                                                       | N/A                                                                                                      |
| `success`                                                                                                | *boolean*                                                                                                | :heavy_check_mark:                                                                                       | N/A                                                                                                      |