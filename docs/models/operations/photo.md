# Photo

## Example Usage

```typescript
import { Photo } from "@indiciaosint/sdk/models/operations";

let value: Photo = {
  date: "2024-10-23",
  id: "<id>",
  location: {
    address: "4132 Birdie Glens",
    costLevel: 3157.35,
    id: "<id>",
    name: "<value>",
    position: {
      latitude: 7861.28,
      longitude: 9974.98,
    },
    tags: [
      "<value 1>",
      "<value 2>",
    ],
    types: [],
  },
  url: "https://frank-management.org/",
};
```

## Fields

| Field                                                                                                                     | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `date`                                                                                                                    | *string*                                                                                                                  | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `id`                                                                                                                      | *string*                                                                                                                  | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `location`                                                                                                                | [operations.PostV1SearchIntelligenceGmailLocation](../../models/operations/post-v1-search-intelligence-gmail-location.md) | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `url`                                                                                                                     | *string*                                                                                                                  | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |