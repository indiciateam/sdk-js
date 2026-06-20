# SearchWhoisData

## Example Usage

```typescript
import { SearchWhoisData } from "@indiciaosint/sdk/models/operations";

let value: SearchWhoisData = {
  entities: [
    {
      handle: "<value>",
      links: [
        {},
      ],
      roles: [
        "<value 1>",
        "<value 2>",
      ],
      vcardArray: [
        [],
      ],
    },
  ],
  events: [
    {
      "key": "<value>",
      "key1": "<value>",
      "key2": "<value>",
    },
  ],
  ldhName: "<value>",
  nameservers: [],
  secureDNS: {
    "key": "<value>",
  },
  status: [],
};
```

## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `entities`                                                 | [operations.Entity2](../../models/operations/entity2.md)[] | :heavy_check_mark:                                         | N/A                                                        |
| `events`                                                   | Record<string, *string*>[]                                 | :heavy_check_mark:                                         | N/A                                                        |
| `ldhName`                                                  | *string*                                                   | :heavy_check_mark:                                         | N/A                                                        |
| `nameservers`                                              | Record<string, *string*>[]                                 | :heavy_check_mark:                                         | N/A                                                        |
| `secureDNS`                                                | Record<string, *string*>                                   | :heavy_check_mark:                                         | N/A                                                        |
| `status`                                                   | *string*[]                                                 | :heavy_check_mark:                                         | N/A                                                        |