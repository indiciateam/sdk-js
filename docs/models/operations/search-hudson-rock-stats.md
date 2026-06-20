# SearchHudsonRockStats

## Example Usage

```typescript
import { SearchHudsonRockStats } from "@indiciaosint/sdk/models/operations";

let value: SearchHudsonRockStats = {
  clientsCount: [
    1591.99,
    4785.44,
    2259.51,
  ],
  clientsUrls: [
    "<value 1>",
    "<value 2>",
  ],
  employeesCount: [
    3515.86,
    767.33,
    4914.3,
  ],
  employeesUrls: [],
  totalEmployees: 1531.16,
  totalUsers: 3962.72,
};
```

## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `clientsCount`     | *number*[]         | :heavy_check_mark: | N/A                |
| `clientsUrls`      | *string*[]         | :heavy_check_mark: | N/A                |
| `employeesCount`   | *number*[]         | :heavy_check_mark: | N/A                |
| `employeesUrls`    | *string*[]         | :heavy_check_mark: | N/A                |
| `totalEmployees`   | *number*           | :heavy_check_mark: | N/A                |
| `totalUsers`       | *number*           | :heavy_check_mark: | N/A                |