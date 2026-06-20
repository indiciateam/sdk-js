# PostV1SearchInfrastructureDnsResponse

Search successful

## Example Usage

```typescript
import { PostV1SearchInfrastructureDnsResponse } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchInfrastructureDnsResponse = {
  data: {
    host: "yummy-trench.name",
    totalARecs: 3211.04,
  },
  success: false,
};
```

## Fields

| Field                                                                                                             | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                            | [operations.PostV1SearchInfrastructureDnsData](../../models/operations/post-v1-search-infrastructure-dns-data.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `success`                                                                                                         | *boolean*                                                                                                         | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `error`                                                                                                           | *string*                                                                                                          | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |