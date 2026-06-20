# PostV1SearchIntelligenceWebDbsData

## Example Usage

```typescript
import { PostV1SearchIntelligenceWebDbsData } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligenceWebDbsData = {
  breaches: [
    {
      email: "Devon84@gmail.com",
      id: "<id>",
      importedAt: "<value>",
      password: "Dh7luMiWThrASOL",
      source: "<value>",
      sourceDate: "<value>",
      sourceName: "<value>",
      url: "https://triangular-premeditation.net",
      username: "Declan38",
    },
  ],
  query: "<value>",
  totalMatches: 9924.52,
  type: "discordid",
};
```

## Fields

| Field                                                                                                                      | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `breaches`                                                                                                                 | [operations.PostV1SearchIntelligenceWebDbsBreach](../../models/operations/post-v1-search-intelligence-web-dbs-breach.md)[] | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `query`                                                                                                                    | *string*                                                                                                                   | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `totalMatches`                                                                                                             | *number*                                                                                                                   | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |
| `type`                                                                                                                     | [operations.CloudsintTypeResponse](../../models/operations/cloudsint-type-response.md)                                     | :heavy_check_mark:                                                                                                         | N/A                                                                                                                        |