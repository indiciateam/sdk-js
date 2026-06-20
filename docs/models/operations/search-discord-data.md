# SearchDiscordData

## Example Usage

```typescript
import { SearchDiscordData } from "@indiciaosint/sdk/models/operations";

let value: SearchDiscordData = {
  banner: null,
  bio: "<value>",
  clan: {
    badge: "<value>",
    banner: "<value>",
    boosts: 2582.81,
    description: "of anti furthermore thread yuck",
    features: [
      "<value 1>",
    ],
    icon: "<value>",
    id: "<id>",
    invite: "<value>",
    memberCount: 3329.8,
    name: "<value>",
    onlineCount: 2084.04,
    tag: "<value>",
    traits: [],
  },
  connectedAccounts: {
    "key": [],
  },
  displayName: "Oswald_Abernathy9",
  internalErrors: [
    "<value 1>",
    "<value 2>",
  ],
  legacyName: null,
  modActions: [
    {
      date: 1491.89,
      description:
        "round though airbrush tedious clearly tedious whenever joyfully um nor",
      details: {
        ground: "<value>",
        source: "<value>",
        targetType: "<value>",
      },
      id: "<id>",
      status: "<value>",
      tags: [],
      timeline: {
        application: 4058.2,
        content: 5838.86,
        created: 5441.95,
      },
      title: "<value>",
    },
  ],
  pfp: "<value>",
  presence: null,
  pronouns: null,
  reviewCount: 3396.98,
  reviews: [],
  robloxProfiles: [
    {
      avatarUrl: "https://menacing-following.org",
      badges: [],
      created: "<value>",
      description: "lest lasting repossess firm sugary",
      displayName: "Tatum.Kub",
      hasPremium: false,
      id: 6022.55,
      isAdmin: false,
      isBanned: false,
      isStarCreator: false,
      isVerified: false,
      pastUsernames: [],
      platforms: {},
      presence: {
        iconUrl: "https://another-tributary.net/",
        lastOnline: "<value>",
        text: "<value>",
        type: 9372.35,
      },
      socials: {
        "key": "<value>",
        "key1": "<value>",
      },
      stats: {
        followers: 3536.17,
        following: 5019.47,
        friends: 7525.96,
        placeVisits: 8773.59,
      },
      username: "Florida_Grady",
    },
  ],
  servers: [
    {
      banner: "<value>",
      description: "impish stoop pluck celsius unfortunate vastly who meh",
      icon: "<value>",
      id: "<id>",
      invite: "<value>",
      membersOnline: 9715.65,
      name: "<value>",
      nickname: "<value>",
      totalMembers: 3481.95,
    },
  ],
  userId: "<id>",
  username: "Sabina_DuBuque36",
};
```

## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `banner`                                                                | *string*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `bio`                                                                   | *string*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `clan`                                                                  | [operations.Clan](../../models/operations/clan.md)                      | :heavy_check_mark:                                                      | N/A                                                                     |
| `connectedAccounts`                                                     | Record<string, *operations.ConnectedAccountsUnion*>                     | :heavy_check_mark:                                                      | N/A                                                                     |
| `displayName`                                                           | *string*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `internalErrors`                                                        | *string*[]                                                              | :heavy_check_mark:                                                      | N/A                                                                     |
| `legacyName`                                                            | *string*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `modActions`                                                            | [operations.ModAction](../../models/operations/mod-action.md)[]         | :heavy_check_mark:                                                      | N/A                                                                     |
| `pfp`                                                                   | *string*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `presence`                                                              | *string*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `pronouns`                                                              | *string*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `reviewCount`                                                           | *number*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `reviews`                                                               | [operations.Review](../../models/operations/review.md)[]                | :heavy_check_mark:                                                      | N/A                                                                     |
| `robloxProfiles`                                                        | [operations.RobloxProfile](../../models/operations/roblox-profile.md)[] | :heavy_check_mark:                                                      | N/A                                                                     |
| `servers`                                                               | [operations.Server](../../models/operations/server.md)[]                | :heavy_check_mark:                                                      | N/A                                                                     |
| `userId`                                                                | *string*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `username`                                                              | *string*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |