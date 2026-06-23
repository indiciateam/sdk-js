# Server

## Example Usage

```typescript
import { Server } from "@indiciaosint/sdk/models/operations";

let value: Server = {
  banner: null,
  description: "shirk um uh-huh diagram on valley ew yowza",
  icon: "<value>",
  id: "<id>",
  invite: "<value>",
  membersOnline: 202.01,
  name: "<value>",
  nickname: "<value>",
  totalMembers: 9982.48,
};
```

## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `banner`                                                                         | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `description`                                                                    | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `icon`                                                                           | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `id`                                                                             | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `invite`                                                                         | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `membersOnline`                                                                  | *number*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `name`                                                                           | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `nickname`                                                                       | *string*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `totalMembers`                                                                   | *number*                                                                         | :heavy_check_mark:                                                               | N/A                                                                              |
| `roles`                                                                          | [operations.SearchDiscordRole](../../models/operations/search-discord-role.md)[] | :heavy_minus_sign:                                                               | N/A                                                                              |