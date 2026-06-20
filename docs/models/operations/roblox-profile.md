# RobloxProfile

## Example Usage

```typescript
import { RobloxProfile } from "@indiciaosint/sdk/models/operations";

let value: RobloxProfile = {
  avatarUrl: "https://good-numeric.info/",
  badges: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
  created: "<value>",
  description: "enhance or longingly boo vacantly finally",
  displayName: "Allen.Mayert",
  hasPremium: false,
  id: 9349.17,
  isAdmin: false,
  isBanned: true,
  isStarCreator: true,
  isVerified: true,
  pastUsernames: [
    "<value 1>",
  ],
  platforms: {},
  presence: {
    iconUrl: "https://another-tributary.net/",
    lastOnline: "<value>",
    text: "<value>",
    type: 9372.35,
  },
  socials: {
    "key": "<value>",
  },
  stats: {
    followers: 3536.17,
    following: 5019.47,
    friends: 7525.96,
    placeVisits: 8773.59,
  },
  username: "Leonard_Hyatt",
};
```

## Fields

| Field                                                                                                                 | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `avatarUrl`                                                                                                           | *string*                                                                                                              | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `badges`                                                                                                              | *string*[]                                                                                                            | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `created`                                                                                                             | *string*                                                                                                              | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `description`                                                                                                         | *string*                                                                                                              | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `displayName`                                                                                                         | *string*                                                                                                              | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `hasPremium`                                                                                                          | *boolean*                                                                                                             | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `id`                                                                                                                  | *number*                                                                                                              | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `isAdmin`                                                                                                             | *boolean*                                                                                                             | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `isBanned`                                                                                                            | *boolean*                                                                                                             | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `isStarCreator`                                                                                                       | *boolean*                                                                                                             | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `isVerified`                                                                                                          | *boolean*                                                                                                             | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `pastUsernames`                                                                                                       | *string*[]                                                                                                            | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `platforms`                                                                                                           | [operations.PostV1SearchSocialsDiscordPlatforms](../../models/operations/post-v1-search-socials-discord-platforms.md) | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `presence`                                                                                                            | [operations.PostV1SearchSocialsDiscordPresence](../../models/operations/post-v1-search-socials-discord-presence.md)   | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `socials`                                                                                                             | Record<string, *string*>                                                                                              | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `stats`                                                                                                               | [operations.PostV1SearchSocialsDiscordStats](../../models/operations/post-v1-search-socials-discord-stats.md)         | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `username`                                                                                                            | *string*                                                                                                              | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `error`                                                                                                               | *string*                                                                                                              | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `rolimons`                                                                                                            | [operations.PostV1SearchSocialsDiscordRolimons](../../models/operations/post-v1-search-socials-discord-rolimons.md)   | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |