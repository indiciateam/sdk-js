# GithubInfo

Completed GitHub profile, commit stats, and discovered emails.

## Example Usage

```typescript
import { GithubInfo } from "@indiciaosint/sdk/models/operations";

let value: GithubInfo = {
  avatarUrl: "https://insignificant-secrecy.info/",
  bio: "<value>",
  commitEmails: {},
  commitRepoCount: 435.69,
  commits: 3787.33,
  company: "Larson Group",
  createdAt: "1715618400747",
  followers: 7048.14,
  following: 8367.41,
  id: 5149.37,
  lastSeen: "<value>",
  location: "<value>",
  name: "<value>",
  publicGists: 503.91,
  publicRepos: 2266.67,
  username: "Valentina.Klocko15",
};
```

## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `avatarUrl`                               | *string*                                  | :heavy_check_mark:                        | N/A                                       |
| `bio`                                     | *string*                                  | :heavy_check_mark:                        | N/A                                       |
| `commitEmails`                            | Record<string, *string*[]>                | :heavy_check_mark:                        | N/A                                       |
| `commitRepoCount`                         | *number*                                  | :heavy_check_mark:                        | N/A                                       |
| `commits`                                 | *number*                                  | :heavy_check_mark:                        | N/A                                       |
| `company`                                 | *string*                                  | :heavy_check_mark:                        | N/A                                       |
| `createdAt`                               | *string*                                  | :heavy_check_mark:                        | N/A                                       |
| `followers`                               | *number*                                  | :heavy_check_mark:                        | N/A                                       |
| `following`                               | *number*                                  | :heavy_check_mark:                        | N/A                                       |
| `id`                                      | *number*                                  | :heavy_check_mark:                        | N/A                                       |
| `lastSeen`                                | *string*                                  | :heavy_check_mark:                        | N/A                                       |
| `location`                                | *string*                                  | :heavy_check_mark:                        | N/A                                       |
| `name`                                    | *string*                                  | :heavy_check_mark:                        | N/A                                       |
| `publicGists`                             | *number*                                  | :heavy_check_mark:                        | N/A                                       |
| `publicRepos`                             | *number*                                  | :heavy_check_mark:                        | N/A                                       |
| `username`                                | *string*                                  | :heavy_check_mark:                        | N/A                                       |
| `activityId`                              | *string*                                  | :heavy_minus_sign:                        | Activity log id for this search, or null. |