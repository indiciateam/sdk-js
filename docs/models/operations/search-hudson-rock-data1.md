# SearchHudsonRockData1

## Example Usage

```typescript
import { SearchHudsonRockData1 } from "@indiciaosint/sdk/models/operations";

let value: SearchHudsonRockData1 = {
  applications: [
    {
      keyword: "<value>",
    },
  ],
  data: {
    employeesUrls: [
      {
        occurrence: 2445.89,
        type: "<value>",
        url: "https://slimy-scout.biz/",
      },
    ],
  },
  employees: 14.61,
  isShopify: false,
  lastEmployeeCompromised: "<value>",
  lastUserCompromised: "<value>",
  logo: "<value>",
  stats: {
    clientsCount: [
      8163.41,
      5166.18,
    ],
    clientsUrls: [],
    employeesCount: [
      9868.45,
    ],
    employeesUrls: [
      "<value 1>",
    ],
    totalEmployees: 3984.04,
    totalUsers: 9920.7,
  },
  thirdPartyDomains: [
    {
      domain: "only-nectarine.org",
      occurrence: 7595.59,
    },
  ],
  thirdParties: 5791.28,
  total: 5482.7,
  totalStealers: 3861.3,
  totalUrls: 449.42,
  type: "ip",
  users: 42.17,
};
```

## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `applications`                                                                                   | [operations.Application](../../models/operations/application.md)[]                               | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `data`                                                                                           | [operations.SearchHudsonRockDataData](../../models/operations/search-hudson-rock-data-data.md)   | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `employees`                                                                                      | *number*                                                                                         | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `isShopify`                                                                                      | *boolean*                                                                                        | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `lastEmployeeCompromised`                                                                        | *string*                                                                                         | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `lastUserCompromised`                                                                            | *string*                                                                                         | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `logo`                                                                                           | *string*                                                                                         | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `stats`                                                                                          | [operations.SearchHudsonRockStats](../../models/operations/search-hudson-rock-stats.md)          | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `thirdPartyDomains`                                                                              | [operations.ThirdPartyDomain](../../models/operations/third-party-domain.md)[]                   | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `thirdParties`                                                                                   | *number*                                                                                         | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `total`                                                                                          | *number*                                                                                         | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `totalStealers`                                                                                  | *number*                                                                                         | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `totalUrls`                                                                                      | *number*                                                                                         | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `type`                                                                                           | [operations.SearchHudsonRockDataType1](../../models/operations/search-hudson-rock-data-type1.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `users`                                                                                          | *number*                                                                                         | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `antiviruses`                                                                                    | [operations.Antiviruses](../../models/operations/antiviruses.md)                                 | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `employeePasswords`                                                                              | [operations.EmployeePasswords](../../models/operations/employee-passwords.md)                    | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `stealerFamilies`                                                                                | [operations.StealerFamilies](../../models/operations/stealer-families.md)                        | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `userPasswords`                                                                                  | [operations.UserPasswords](../../models/operations/user-passwords.md)                            | :heavy_minus_sign:                                                                               | N/A                                                                                              |