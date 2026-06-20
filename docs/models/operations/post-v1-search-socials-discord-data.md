# PostV1SearchSocialsDiscordData

## Example Usage

```typescript
import { PostV1SearchSocialsDiscordData } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchSocialsDiscordData = {
  banner: "<value>",
  bio: "<value>",
  clan: {
    badge: "<value>",
    banner: "<value>",
    boosts: 1420.11,
    description:
      "aha closed reconstitute only misjudge self-reliant qua athwart mostly shark",
    features: [],
    icon: "<value>",
    id: "<id>",
    invite: "<value>",
    memberCount: 8432.67,
    name: "<value>",
    onlineCount: 9770.71,
    tag: "<value>",
    traits: [],
  },
  connectedAccounts: {
    "key": [],
  },
  displayName: "Marina.Rolfson99",
  internalErrors: [
    "<value 1>",
  ],
  legacyName: "<value>",
  modActions: [
    {
      date: 2296.88,
      description: "outflank secularize a",
      details: {
        ground: "<value>",
        source: "<value>",
        targetType: "<value>",
      },
      id: "<id>",
      status: "<value>",
      tags: [
        "<value 1>",
        "<value 2>",
      ],
      timeline: {
        application: 4058.2,
        content: 5838.86,
        created: 5441.95,
      },
      title: "<value>",
    },
  ],
  pfp: "<value>",
  presence: "<value>",
  pronouns: null,
  reviewCount: 9239.87,
  reviews: [
    {
      comment:
        "Andy shoes are designed to keeping in mind durability as well as trends, the most stylish range of shoes & sandals",
      id: 3705.9,
      sender: {
        badges: [
          {
            description: "blah idolized trash structure off ick",
            icon: "<value>",
            name: "<value>",
            redirectURL: "https://compassionate-giggle.org",
            type: 6074.75,
          },
        ],
        discordID: "<id>",
        id: 4043.64,
        profilePhoto: "<value>",
        username: "Sadie_Connelly30",
      },
      timestamp: 267.77,
      type: 3019.01,
    },
  ],
  robloxProfiles: [],
  servers: [],
  userId: "<id>",
  username: "Marilyne.Bergnaum",
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