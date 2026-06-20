# PostV1SearchSocialsGithubResponse

Search successful

## Example Usage

```typescript
import { PostV1SearchSocialsGithubResponse } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchSocialsGithubResponse = {
  data: {
    avatarUrl: "https://wealthy-pomelo.info",
    bio: null,
    commitEmails: {
      "key": [
        "<value 1>",
        "<value 2>",
      ],
      "key1": [
        "<value 1>",
        "<value 2>",
      ],
    },
    commitRepoCount: 9696.76,
    commits: 4484.66,
    company: "Schiller, Osinski and Frami",
    createdAt: "1735585178845",
    followers: 2121.23,
    following: 7914.91,
    id: 4839.35,
    lastSeen: "<value>",
    location: "<value>",
    name: "<value>",
    publicGists: 955.46,
    publicRepos: 7228.21,
    username: "Sarai_Tromp75",
  },
  success: false,
};
```

## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                    | [operations.PostV1SearchSocialsGithubData](../../models/operations/post-v1-search-socials-github-data.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `success`                                                                                                 | *boolean*                                                                                                 | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `error`                                                                                                   | *string*                                                                                                  | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |