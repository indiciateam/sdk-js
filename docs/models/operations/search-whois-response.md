# SearchWhoisResponse

Search successful

## Example Usage

```typescript
import { SearchWhoisResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchWhoisResponse = {
  data: {
    dates: {},
    dnssec: {},
    domain: "free-merit.org",
    nameservers: [
      {
        "key": "<value>",
      },
    ],
    raw: {},
    registrar: {
      abuseEmail: "<value>",
      abusePhone: "<value>",
      ianaId: "<id>",
      name: "<value>",
      url: "https://busy-gloom.com",
    },
    status: [
      "<value 1>",
      "<value 2>",
      "<value 3>",
    ],
  },
  success: false,
};
```

## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `data`                                                                     | [operations.SearchWhoisData](../../models/operations/search-whois-data.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `success`                                                                  | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `error`                                                                    | *string*                                                                   | :heavy_minus_sign:                                                         | N/A                                                                        |