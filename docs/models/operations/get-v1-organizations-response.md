# GetV1OrganizationsResponse

List of organizations with member counts and your role.

## Example Usage

```typescript
import { GetV1OrganizationsResponse } from "@indiciaosint/sdk/models/operations";

let value: GetV1OrganizationsResponse = {
  organizations: [],
  success: false,
};
```

## Fields

| Field                                                                                                       | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `organizations`                                                                                             | [operations.GetV1OrganizationsOrganization](../../models/operations/get-v1-organizations-organization.md)[] | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `success`                                                                                                   | *boolean*                                                                                                   | :heavy_check_mark:                                                                                          | N/A                                                                                                         |