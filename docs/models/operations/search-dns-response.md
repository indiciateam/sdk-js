# SearchDnsResponse

Search successful

## Example Usage

```typescript
import { SearchDnsResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchDnsResponse = {
  data: {
    host: "unconscious-intent.net",
    totalARecs: 3413.7,
  },
  success: false,
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `data`                                                                 | [operations.SearchDnsData](../../models/operations/search-dns-data.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `success`                                                              | *boolean*                                                              | :heavy_check_mark:                                                     | N/A                                                                    |
| `error`                                                                | *string*                                                               | :heavy_minus_sign:                                                     | N/A                                                                    |