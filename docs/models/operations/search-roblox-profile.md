# SearchRobloxProfile

## Example Usage

```typescript
import { SearchRobloxProfile } from "@indiciaosint/sdk/models/operations";

let value: SearchRobloxProfile = {
  avatarUrl: "https://jaunty-obesity.com",
  badges: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
  created: "<value>",
  description: "derby train posh whoa whoa why swill except militate ouch",
  displayName: "Jovani36",
  hasPremium: true,
  id: 7496.22,
  isAdmin: false,
  isBanned: false,
  isStarCreator: false,
  isVerified: true,
  pastUsernames: [
    "<value 1>",
  ],
  platforms: {},
  presence: {
    iconUrl: "https://political-scorpion.name/",
    lastOnline: "<value>",
    text: "<value>",
    type: 6967.03,
  },
  socials: {},
  stats: {
    followers: 1671.09,
    following: 355.89,
    friends: 7995.98,
    placeVisits: 733.57,
  },
  username: "Rebeka_Bernier",
};
```

## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `avatarUrl`                                                                            | *string*                                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `badges`                                                                               | *string*[]                                                                             | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `created`                                                                              | *string*                                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `description`                                                                          | *string*                                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `displayName`                                                                          | *string*                                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `hasPremium`                                                                           | *boolean*                                                                              | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `id`                                                                                   | *number*                                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `isAdmin`                                                                              | *boolean*                                                                              | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `isBanned`                                                                             | *boolean*                                                                              | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `isStarCreator`                                                                        | *boolean*                                                                              | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `isVerified`                                                                           | *boolean*                                                                              | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `pastUsernames`                                                                        | *string*[]                                                                             | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `platforms`                                                                            | [operations.SearchRobloxPlatforms](../../models/operations/search-roblox-platforms.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `presence`                                                                             | [operations.SearchRobloxPresence](../../models/operations/search-roblox-presence.md)   | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `socials`                                                                              | Record<string, *string*>                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `stats`                                                                                | [operations.SearchRobloxStats](../../models/operations/search-roblox-stats.md)         | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `username`                                                                             | *string*                                                                               | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `error`                                                                                | *string*                                                                               | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `rolimons`                                                                             | [operations.SearchRobloxRolimons](../../models/operations/search-roblox-rolimons.md)   | :heavy_minus_sign:                                                                     | N/A                                                                                    |