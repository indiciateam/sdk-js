# SearchIpInfoResponse

Search successful

## Example Usage

```typescript
import { SearchIpInfoResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchIpInfoResponse = {
  data: {
    continent: "Australia",
    country: "Argentina",
    hosting: true,
    lat: 7527.7,
    lon: 9998.11,
    mobile: true,
    proxy: true,
    query: "<value>",
    status: "success",
    timezone: "Asia/Chita",
  },
  success: true,
};
```

## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `data`                                                                        | [operations.SearchIpInfoData](../../models/operations/search-ip-info-data.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `success`                                                                     | *boolean*                                                                     | :heavy_check_mark:                                                            | N/A                                                                           |
| `error`                                                                       | *string*                                                                      | :heavy_minus_sign:                                                            | N/A                                                                           |