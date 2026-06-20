# SearchWhoisResponse

Search successful

## Example Usage

```typescript
import { SearchWhoisResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchWhoisResponse = {
  data: {
    entities: [],
    events: [
      {
        "key": "<value>",
        "key1": "<value>",
      },
    ],
    ldhName: "<value>",
    nameservers: [
      {
        "key": "<value>",
      },
      {
        "key": "<value>",
      },
      {
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
      },
    ],
    secureDNS: {
      "key": "<value>",
      "key1": "<value>",
    },
    status: [
      "<value 1>",
      "<value 2>",
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