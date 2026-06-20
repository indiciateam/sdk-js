# PostV1SearchInfrastructureWhoisResponse

Search successful

## Example Usage

```typescript
import { PostV1SearchInfrastructureWhoisResponse } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchInfrastructureWhoisResponse = {
  data: {
    entities: [],
    events: [
      {},
    ],
    ldhName: "<value>",
    nameservers: [
      {
        "key": "<value>",
      },
      {
        "key": "<value>",
        "key1": "<value>",
      },
    ],
    secureDNS: {},
    status: [],
  },
  success: false,
};
```

## Fields

| Field                                                                                                                 | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                                | [operations.PostV1SearchInfrastructureWhoisData](../../models/operations/post-v1-search-infrastructure-whois-data.md) | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `success`                                                                                                             | *boolean*                                                                                                             | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `error`                                                                                                               | *string*                                                                                                              | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |