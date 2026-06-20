# SearchWebDatabasesResult

## Example Usage

```typescript
import { SearchWebDatabasesResult } from "@indiciaosint/sdk/models/operations";

let value: SearchWebDatabasesResult = {
  address: "293 Forest Avenue",
  country: "Grenada",
  dob: "1952-06-09",
  email: "Cordia.Lowe11@gmail.com",
  fields: [
    "<value 1>",
    "<value 2>",
  ],
  firstName: "Bell",
  lastName: "Green",
  name: "<value>",
  password: "CSZXwKEkOk18l0W",
  phone: "248.517.1401 x8252",
  source: {
    breachDate: "<value>",
    compilation: "0",
    name: "<value>",
    passwordless: "1",
    unverified: "1",
  },
  state: "Texas",
  zip: "05662",
};
```

## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `address`                                                           | *string*                                                            | :heavy_check_mark:                                                  | N/A                                                                 |
| `country`                                                           | *string*                                                            | :heavy_check_mark:                                                  | N/A                                                                 |
| `dob`                                                               | *string*                                                            | :heavy_check_mark:                                                  | N/A                                                                 |
| `email`                                                             | *string*                                                            | :heavy_check_mark:                                                  | N/A                                                                 |
| `fields`                                                            | *string*[]                                                          | :heavy_check_mark:                                                  | N/A                                                                 |
| `firstName`                                                         | *string*                                                            | :heavy_check_mark:                                                  | N/A                                                                 |
| `lastName`                                                          | *string*                                                            | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *string*                                                            | :heavy_check_mark:                                                  | N/A                                                                 |
| `password`                                                          | *string*                                                            | :heavy_check_mark:                                                  | N/A                                                                 |
| `phone`                                                             | *string*                                                            | :heavy_check_mark:                                                  | N/A                                                                 |
| `source`                                                            | [operations.ResultSource](../../models/operations/result-source.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `state`                                                             | *string*                                                            | :heavy_check_mark:                                                  | N/A                                                                 |
| `zip`                                                               | *string*                                                            | :heavy_check_mark:                                                  | N/A                                                                 |