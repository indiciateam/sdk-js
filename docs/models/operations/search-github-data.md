# SearchGithubData

## Example Usage

```typescript
import { SearchGithubData } from "@indiciaosint/sdk/models/operations";

let value: SearchGithubData = {
  avatarUrl: "https://tough-window.org/",
  bio: "<value>",
  commitEmails: {
    "key": [
      "<value 1>",
    ],
    "key1": [
      "<value 1>",
      "<value 2>",
    ],
  },
  commitRepoCount: 2862.44,
  commits: 2703.7,
  company: "Huels LLC",
  createdAt: "1734080951854",
  followers: 5967.67,
  following: 8704.78,
  id: 2879.52,
  lastSeen: "<value>",
  location: "<value>",
  name: "<value>",
  publicGists: 833.57,
  publicRepos: 3943.27,
  username: "Shad.Hermann",
};
```

## Fields

| Field                      | Type                       | Required                   | Description                |
| -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| `avatarUrl`                | *string*                   | :heavy_check_mark:         | N/A                        |
| `bio`                      | *string*                   | :heavy_check_mark:         | N/A                        |
| `commitEmails`             | Record<string, *string*[]> | :heavy_check_mark:         | N/A                        |
| `commitRepoCount`          | *number*                   | :heavy_check_mark:         | N/A                        |
| `commits`                  | *number*                   | :heavy_check_mark:         | N/A                        |
| `company`                  | *string*                   | :heavy_check_mark:         | N/A                        |
| `createdAt`                | *string*                   | :heavy_check_mark:         | N/A                        |
| `followers`                | *number*                   | :heavy_check_mark:         | N/A                        |
| `following`                | *number*                   | :heavy_check_mark:         | N/A                        |
| `id`                       | *number*                   | :heavy_check_mark:         | N/A                        |
| `lastSeen`                 | *string*                   | :heavy_check_mark:         | N/A                        |
| `location`                 | *string*                   | :heavy_check_mark:         | N/A                        |
| `name`                     | *string*                   | :heavy_check_mark:         | N/A                        |
| `publicGists`              | *number*                   | :heavy_check_mark:         | N/A                        |
| `publicRepos`              | *number*                   | :heavy_check_mark:         | N/A                        |
| `username`                 | *string*                   | :heavy_check_mark:         | N/A                        |