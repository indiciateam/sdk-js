# PostV1SearchInfrastructureIpinfoResponse

Search successful

## Example Usage

```typescript
import { PostV1SearchInfrastructureIpinfoResponse } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchInfrastructureIpinfoResponse = {
  data: {
    continent: "Europe",
    country: "Somalia",
    hosting: false,
    lat: 1446.83,
    lon: 6535.66,
    mobile: false,
    proxy: false,
    query: "<value>",
    status: "success",
    timezone: "Asia/Vladivostok",
  },
  success: false,
};
```

## Fields

| Field                                                                                                                   | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                                  | [operations.PostV1SearchInfrastructureIpinfoData](../../models/operations/post-v1-search-infrastructure-ipinfo-data.md) | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `success`                                                                                                               | *boolean*                                                                                                               | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `error`                                                                                                                 | *string*                                                                                                                | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |