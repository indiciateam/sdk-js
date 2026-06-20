# SearchGithubResponse

Search successful

## Example Usage

```typescript
import { SearchGithubResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchGithubResponse = {
  data: {
    avatarUrl: null,
    bio: "<value>",
    commitEmails: {},
    commitRepoCount: 1843.67,
    commits: 1496.53,
    company: "Abbott - Waelchi",
    createdAt: "1725698414053",
    followers: 6761.43,
    following: 6481.51,
    id: 6212.13,
    lastSeen: "<value>",
    location: "<value>",
    name: "<value>",
    publicGists: 5409.47,
    publicRepos: 1211.02,
    username: "Ana.Lebsack",
  },
  success: true,
};
```

## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `data`                                                                       | [operations.SearchGithubData](../../models/operations/search-github-data.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `success`                                                                    | *boolean*                                                                    | :heavy_check_mark:                                                           | N/A                                                                          |
| `error`                                                                      | *string*                                                                     | :heavy_minus_sign:                                                           | N/A                                                                          |