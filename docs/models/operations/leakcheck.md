# Leakcheck

## Example Usage

```typescript
import { Leakcheck } from "@indiciaosint/sdk/models/operations";

let value: Leakcheck = {
  error: "<value>",
  found: 7480.25,
  quota: 2695.01,
  result: [
    {
      address: "16648 Purdy Crossing",
      country: "Iceland",
      dob: "1958-09-24",
      email: "Samir32@yahoo.com",
      fields: [
        "<value 1>",
        "<value 2>",
      ],
      firstName: "Viviane",
      lastName: "Kreiger",
      name: "<value>",
      password: "E9cMMaVWbDp80TQ",
      phone: "1-431-920-8034 x14564",
      source: {
        breachDate: "<value>",
        compilation: "0",
        name: "<value>",
        passwordless: "1",
        unverified: "1",
      },
      state: "New Mexico",
      zip: "61635-1136",
    },
  ],
  success: true,
};
```

## Fields

| Field                                                                                           | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `error`                                                                                         | *string*                                                                                        | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `found`                                                                                         | *number*                                                                                        | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `quota`                                                                                         | *number*                                                                                        | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `result`                                                                                        | [operations.SearchWebDatabasesResult](../../models/operations/search-web-databases-result.md)[] | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `success`                                                                                       | *boolean*                                                                                       | :heavy_check_mark:                                                                              | N/A                                                                                             |