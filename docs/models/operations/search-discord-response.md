# SearchDiscordResponse

Search successful

## Example Usage

```typescript
import { SearchDiscordResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchDiscordResponse = {
  data: {
    banner: "<value>",
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
      "key": {
        id: "<id>",
        link: "<value>",
        name: "<value>",
      },
    },
    displayName: "William55",
    internalErrors: [],
    legacyName: "<value>",
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
    presence: "<value>",
    pronouns: "<value>",
    reviewCount: 6987.78,
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
    username: "May.Prosacco23",
  },
  success: true,
};
```

## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `data`                                                                         | [operations.SearchDiscordData](../../models/operations/search-discord-data.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `success`                                                                      | *boolean*                                                                      | :heavy_check_mark:                                                             | N/A                                                                            |
| `error`                                                                        | *string*                                                                       | :heavy_minus_sign:                                                             | N/A                                                                            |