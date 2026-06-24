# ResultEvent

Terminal `result` event with the completed GitHub profile.

## Example Usage

```typescript
import { ResultEvent } from "@indiciaosint/sdk/models/operations";

let value: ResultEvent = {
  data: {
    avatarUrl: "https://evil-scenario.net/",
    bio: "<value>",
    commitEmails: {
      "key": [
        "<value 1>",
        "<value 2>",
      ],
    },
    commitRepoCount: 1541.96,
    commits: 4637.36,
    company: "Senger and Sons",
    createdAt: "1710065803283",
    followers: 2725.48,
    following: 6076.05,
    id: 9546.78,
    lastSeen: "<value>",
    location: "<value>",
    name: "<value>",
    publicGists: 2485.58,
    publicRepos: 7248.44,
    username: "Nellie_Fay46",
  },
  event: "result",
};
```

## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `data`                                                          | [operations.GithubInfo](../../models/operations/github-info.md) | :heavy_check_mark:                                              | Completed GitHub profile, commit stats, and discovered emails.  |
| `event`                                                         | *"result"*                                                      | :heavy_check_mark:                                              | N/A                                                             |