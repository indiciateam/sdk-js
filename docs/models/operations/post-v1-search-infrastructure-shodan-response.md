# PostV1SearchInfrastructureShodanResponse

Search successful

## Example Usage

```typescript
import { PostV1SearchInfrastructureShodanResponse } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchInfrastructureShodanResponse = {
  data: {
    matches: [],
    total: 8811.99,
  },
  success: false,
};
```

## Fields

| Field                                                                                                                   | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                                  | [operations.PostV1SearchInfrastructureShodanData](../../models/operations/post-v1-search-infrastructure-shodan-data.md) | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `success`                                                                                                               | *boolean*                                                                                                               | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `error`                                                                                                                 | *string*                                                                                                                | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |