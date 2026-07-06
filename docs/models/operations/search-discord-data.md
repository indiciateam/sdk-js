# SearchDiscordData

## Example Usage

```typescript
import { SearchDiscordData } from "@indiciaosint/sdk/models/operations";

let value: SearchDiscordData = {
  internalErrors: [],
};
```

## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `internalErrors`                                                        | *string*[]                                                              | :heavy_check_mark:                                                      | N/A                                                                     |
| `banner`                                                                | *string*                                                                | :heavy_minus_sign:                                                      | N/A                                                                     |
| `bio`                                                                   | *string*                                                                | :heavy_minus_sign:                                                      | N/A                                                                     |
| `clan`                                                                  | [operations.Clan](../../models/operations/clan.md)                      | :heavy_minus_sign:                                                      | N/A                                                                     |
| `connectedAccounts`                                                     | Record<string, *operations.ConnectedAccountsUnion*>                     | :heavy_minus_sign:                                                      | N/A                                                                     |
| `displayName`                                                           | *string*                                                                | :heavy_minus_sign:                                                      | N/A                                                                     |
| `legacyName`                                                            | *string*                                                                | :heavy_minus_sign:                                                      | N/A                                                                     |
| `modActions`                                                            | [operations.ModAction](../../models/operations/mod-action.md)[]         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `pfp`                                                                   | *string*                                                                | :heavy_minus_sign:                                                      | N/A                                                                     |
| `presence`                                                              | *string*                                                                | :heavy_minus_sign:                                                      | N/A                                                                     |
| `pronouns`                                                              | *string*                                                                | :heavy_minus_sign:                                                      | N/A                                                                     |
| `reviewCount`                                                           | *number*                                                                | :heavy_minus_sign:                                                      | N/A                                                                     |
| `reviews`                                                               | [operations.Review](../../models/operations/review.md)[]                | :heavy_minus_sign:                                                      | N/A                                                                     |
| `robloxProfiles`                                                        | [operations.RobloxProfile](../../models/operations/roblox-profile.md)[] | :heavy_minus_sign:                                                      | N/A                                                                     |
| `servers`                                                               | [operations.Server](../../models/operations/server.md)[]                | :heavy_minus_sign:                                                      | N/A                                                                     |
| `userId`                                                                | *string*                                                                | :heavy_minus_sign:                                                      | N/A                                                                     |
| `username`                                                              | *string*                                                                | :heavy_minus_sign:                                                      | N/A                                                                     |