# GetV1OrganizationsByIdMembersResponse

Member list.

## Example Usage

```typescript
import { GetV1OrganizationsByIdMembersResponse } from "@indiciaosint/sdk/models/operations";

let value: GetV1OrganizationsByIdMembersResponse = {
  members: [
    {
      createdAt: 897406,
      displayUsername: "<value>",
      id: "<id>",
      organizationId: "<id>",
      role: "<value>",
      userId: "<id>",
      username: "Ulises_Witting",
    },
  ],
  success: false,
};
```

## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `members`                                                | [operations.Member](../../models/operations/member.md)[] | :heavy_check_mark:                                       | N/A                                                      |
| `success`                                                | *boolean*                                                | :heavy_check_mark:                                       | N/A                                                      |