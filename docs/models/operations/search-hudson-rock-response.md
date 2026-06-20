# SearchHudsonRockResponse

Search successful

## Example Usage

```typescript
import { SearchHudsonRockResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchHudsonRockResponse = {
  data: {
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
    employees: 2591.36,
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
    thirdPartyDomains: [],
    thirdParties: 1453.83,
    total: 672.04,
    totalStealers: 4423.68,
    totalUrls: 7428.22,
    type: "ip",
    users: 3675.02,
  },
  success: false,
};
```

## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `data`                                 | *operations.SearchHudsonRockDataUnion* | :heavy_check_mark:                     | N/A                                    |
| `success`                              | *boolean*                              | :heavy_check_mark:                     | N/A                                    |
| `error`                                | *string*                               | :heavy_minus_sign:                     | N/A                                    |