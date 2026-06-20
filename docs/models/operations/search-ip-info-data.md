# SearchIpInfoData

## Example Usage

```typescript
import { SearchIpInfoData } from "@indiciaosint/sdk/models/operations";

let value: SearchIpInfoData = {
  continent: "Australia",
  country: "Bulgaria",
  hosting: false,
  lat: 712.64,
  lon: 555,
  mobile: true,
  proxy: false,
  query: "<value>",
  status: "fail",
  timezone: "America/St_Lucia",
};
```

## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `continent`                                                                       | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `country`                                                                         | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `hosting`                                                                         | *boolean*                                                                         | :heavy_check_mark:                                                                | N/A                                                                               |
| `lat`                                                                             | *number*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `lon`                                                                             | *number*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `mobile`                                                                          | *boolean*                                                                         | :heavy_check_mark:                                                                | N/A                                                                               |
| `proxy`                                                                           | *boolean*                                                                         | :heavy_check_mark:                                                                | N/A                                                                               |
| `query`                                                                           | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `status`                                                                          | [operations.SearchIpInfoStatus](../../models/operations/search-ip-info-status.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `timezone`                                                                        | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `as`                                                                              | *string*                                                                          | :heavy_minus_sign:                                                                | N/A                                                                               |
| `asname`                                                                          | *string*                                                                          | :heavy_minus_sign:                                                                | N/A                                                                               |
| `city`                                                                            | *string*                                                                          | :heavy_minus_sign:                                                                | N/A                                                                               |
| `district`                                                                        | *string*                                                                          | :heavy_minus_sign:                                                                | N/A                                                                               |
| `isp`                                                                             | *string*                                                                          | :heavy_minus_sign:                                                                | N/A                                                                               |
| `message`                                                                         | *string*                                                                          | :heavy_minus_sign:                                                                | N/A                                                                               |
| `org`                                                                             | *string*                                                                          | :heavy_minus_sign:                                                                | N/A                                                                               |
| `regionName`                                                                      | *string*                                                                          | :heavy_minus_sign:                                                                | N/A                                                                               |
| `reverse`                                                                         | *string*                                                                          | :heavy_minus_sign:                                                                | N/A                                                                               |
| `zip`                                                                             | *string*                                                                          | :heavy_minus_sign:                                                                | N/A                                                                               |