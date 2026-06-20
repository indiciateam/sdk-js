# SearchGmailData

## Example Usage

```typescript
import { SearchGmailData } from "@indiciaosint/sdk/models/operations";

let value: SearchGmailData = {
  profile: {
    emails: {
      "key": {
        value: "<value>",
      },
    },
    personId: "<id>",
    sourceIds: {},
  },
};
```

## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `profile`                                                                        | [operations.SearchGmailProfile](../../models/operations/search-gmail-profile.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `calendar`                                                                       | [operations.Calendar](../../models/operations/calendar.md)                       | :heavy_minus_sign:                                                               | N/A                                                                              |
| `maps`                                                                           | [operations.Maps](../../models/operations/maps.md)                               | :heavy_minus_sign:                                                               | N/A                                                                              |
| `playGames`                                                                      | [operations.PlayGames](../../models/operations/play-games.md)                    | :heavy_minus_sign:                                                               | N/A                                                                              |