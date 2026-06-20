# PostV1SearchInfrastructureWhoisData

## Example Usage

```typescript
import { PostV1SearchInfrastructureWhoisData } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchInfrastructureWhoisData = {
  entities: [
    {
      handle: "<value>",
      links: [
        {},
        {
          "key": "<value>",
          "key1": "<value>",
        },
        {
          "key": "<value>",
          "key1": "<value>",
        },
      ],
      roles: [
        "<value 1>",
        "<value 2>",
      ],
      vcardArray: [
        "<value>",
      ],
    },
  ],
  events: [],
  ldhName: "<value>",
  nameservers: [],
  secureDNS: {
    "key": "<value>",
  },
  status: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
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