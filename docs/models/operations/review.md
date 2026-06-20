# Review

## Example Usage

```typescript
import { Review } from "@indiciaosint/sdk/models/operations";

let value: Review = {
  comment:
    "The Apollotech B340 is an affordable wireless mouse with reliable connectivity, 12 months battery life and modern design",
  id: 5334.82,
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
  timestamp: 8581.74,
  type: 7622.63,
};
```

## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `comment`                                              | *string*                                               | :heavy_check_mark:                                     | N/A                                                    |
| `id`                                                   | *number*                                               | :heavy_check_mark:                                     | N/A                                                    |
| `sender`                                               | [operations.Sender](../../models/operations/sender.md) | :heavy_check_mark:                                     | N/A                                                    |
| `timestamp`                                            | *number*                                               | :heavy_check_mark:                                     | N/A                                                    |
| `type`                                                 | *number*                                               | :heavy_check_mark:                                     | N/A                                                    |
| `star`                                                 | *number*                                               | :heavy_minus_sign:                                     | N/A                                                    |