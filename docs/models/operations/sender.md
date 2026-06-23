# Sender

## Example Usage

```typescript
import { Sender } from "@indiciaosint/sdk/models/operations";

let value: Sender = {
  badges: [],
  discordID: "<id>",
  id: 4083.52,
  profilePhoto: "<value>",
  username: "Osbaldo70",
};
```

## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `badges`                                                                           | [operations.SearchDiscordBadge](../../models/operations/search-discord-badge.md)[] | :heavy_check_mark:                                                                 | N/A                                                                                |
| `discordID`                                                                        | *string*                                                                           | :heavy_check_mark:                                                                 | N/A                                                                                |
| `id`                                                                               | *number*                                                                           | :heavy_check_mark:                                                                 | N/A                                                                                |
| `profilePhoto`                                                                     | *string*                                                                           | :heavy_check_mark:                                                                 | N/A                                                                                |
| `username`                                                                         | *string*                                                                           | :heavy_check_mark:                                                                 | N/A                                                                                |
| `clientMod`                                                                        | *boolean*                                                                          | :heavy_minus_sign:                                                                 | N/A                                                                                |