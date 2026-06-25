# VirusTotalContentData

## Example Usage

```typescript
import { VirusTotalContentData } from "@indiciaosint/sdk/models/operations";

let value: VirusTotalContentData = {
  files: [],
  searchQuery: "<value>",
  totalResults: 4458.16,
};
```

## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `files`                                                                                   | [operations.VirusTotalContentFile](../../models/operations/virus-total-content-file.md)[] | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `searchQuery`                                                                             | *string*                                                                                  | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `totalResults`                                                                            | *number*                                                                                  | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `cleanFiles`                                                                              | *number*                                                                                  | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `contentType`                                                                             | *string*                                                                                  | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `maliciousFiles`                                                                          | *number*                                                                                  | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `suspiciousFiles`                                                                         | *number*                                                                                  | :heavy_minus_sign:                                                                        | N/A                                                                                       |