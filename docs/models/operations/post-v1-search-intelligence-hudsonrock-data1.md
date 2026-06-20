# PostV1SearchIntelligenceHudsonrockData1

## Example Usage

```typescript
import { PostV1SearchIntelligenceHudsonrockData1 } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligenceHudsonrockData1 = {
  applications: [
    {
      keyword: "<value>",
    },
  ],
  data: {
    employeesUrls: [
      {
        occurrence: 457.2,
        type: "<value>",
        url: "https://thick-bar.net",
      },
    ],
  },
  employees: 3856.28,
  isShopify: false,
  lastEmployeeCompromised: "<value>",
  lastUserCompromised: "<value>",
  logo: "<value>",
  stats: {
    clientsCount: [
      2323.71,
      6424.38,
    ],
    clientsUrls: [],
    employeesCount: [
      572.77,
      50.38,
    ],
    employeesUrls: [
      "<value 1>",
      "<value 2>",
      "<value 3>",
    ],
    totalEmployees: 3689.85,
    totalUsers: 6611.4,
  },
  thirdPartyDomains: [],
  thirdParties: 7983.36,
  total: 1660.07,
  totalStealers: 7109.71,
  totalUrls: 4986.9,
  type: "username",
  users: 6407.39,
};
```

## Fields

| Field                                                                                                                                  | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `applications`                                                                                                                         | [operations.Application](../../models/operations/application.md)[]                                                                     | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `data`                                                                                                                                 | [operations.PostV1SearchIntelligenceHudsonrockDataData](../../models/operations/post-v1-search-intelligence-hudsonrock-data-data.md)   | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `employees`                                                                                                                            | *number*                                                                                                                               | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `isShopify`                                                                                                                            | *boolean*                                                                                                                              | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `lastEmployeeCompromised`                                                                                                              | *string*                                                                                                                               | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `lastUserCompromised`                                                                                                                  | *string*                                                                                                                               | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `logo`                                                                                                                                 | *string*                                                                                                                               | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `stats`                                                                                                                                | [operations.PostV1SearchIntelligenceHudsonrockStats](../../models/operations/post-v1-search-intelligence-hudsonrock-stats.md)          | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `thirdPartyDomains`                                                                                                                    | [operations.ThirdPartyDomain](../../models/operations/third-party-domain.md)[]                                                         | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `thirdParties`                                                                                                                         | *number*                                                                                                                               | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `total`                                                                                                                                | *number*                                                                                                                               | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `totalStealers`                                                                                                                        | *number*                                                                                                                               | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `totalUrls`                                                                                                                            | *number*                                                                                                                               | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `type`                                                                                                                                 | [operations.PostV1SearchIntelligenceHudsonrockDataType1](../../models/operations/post-v1-search-intelligence-hudsonrock-data-type1.md) | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `users`                                                                                                                                | *number*                                                                                                                               | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `antiviruses`                                                                                                                          | [operations.Antiviruses](../../models/operations/antiviruses.md)                                                                       | :heavy_minus_sign:                                                                                                                     | N/A                                                                                                                                    |
| `employeePasswords`                                                                                                                    | [operations.EmployeePasswords](../../models/operations/employee-passwords.md)                                                          | :heavy_minus_sign:                                                                                                                     | N/A                                                                                                                                    |
| `stealerFamilies`                                                                                                                      | [operations.StealerFamilies](../../models/operations/stealer-families.md)                                                              | :heavy_minus_sign:                                                                                                                     | N/A                                                                                                                                    |
| `userPasswords`                                                                                                                        | [operations.UserPasswords](../../models/operations/user-passwords.md)                                                                  | :heavy_minus_sign:                                                                                                                     | N/A                                                                                                                                    |