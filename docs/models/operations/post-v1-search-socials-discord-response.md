# PostV1SearchSocialsDiscordResponse

Search successful

## Example Usage

```typescript
import { PostV1SearchSocialsDiscordResponse } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchSocialsDiscordResponse = {
  data: {
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
    connectedAccounts: {},
    displayName: "Alberto95",
    internalErrors: [
      "<value 1>",
    ],
    legacyName: "<value>",
    modActions: [],
    pfp: "<value>",
    presence: "<value>",
    pronouns: "<value>",
    reviewCount: 6473.07,
    reviews: [],
    robloxProfiles: [],
    servers: [],
    userId: "<id>",
    username: "Cecelia.Skiles6",
  },
  success: true,
};
```

## Fields

| Field                                                                                                       | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                      | [operations.PostV1SearchSocialsDiscordData](../../models/operations/post-v1-search-socials-discord-data.md) | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `success`                                                                                                   | *boolean*                                                                                                   | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `error`                                                                                                     | *string*                                                                                                    | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |