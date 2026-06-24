# GithubSearchEvent

A Server-Sent Event. The `event:` field names the type ("status", "heartbeat", or "result"); errors are delivered as a data-only event.


## Supported Types

### `operations.StatusEvent`

```typescript
const value: operations.StatusEvent = {
  data: "<value>",
  event: "status",
};
```

### `operations.HeartbeatEvent`

```typescript
const value: operations.HeartbeatEvent = {
  data: "<value>",
  event: "heartbeat",
};
```

### `operations.ResultEvent`

```typescript
const value: operations.ResultEvent = {
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

### `operations.SearchGithubErrorEvent`

```typescript
const value: operations.SearchGithubErrorEvent = {
  data: {
    status: "error",
    success: false,
    error: "<value>",
  },
};
```

