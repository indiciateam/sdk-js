# User

## Example Usage

```typescript
import { User } from "@indiciaosint/sdk/models/operations";

let value: User = {
  acceptOrgInvites: false,
  acceptedLegalHash: "<value>",
  banExpires: 454995,
  banReason: "<value>",
  banned: false,
  boughtCreditsAfterReferral: false,
  createdAt: 340230,
  displayUsername: "<value>",
  email: "Hannah.Grant@gmail.com",
  emailVerified: false,
  flagged: false,
  id: "<id>",
  image: "https://picsum.photos/seed/0q6lk/3586/1701",
  name: "<value>",
  referralLink: null,
  referred: "<value>",
  restrictedFeatures: [
    "phonebook",
  ],
  role: "<value>",
  stripeConnectedId: "<id>",
  stripeId: "<id>",
  taxState: null,
  tokens: 49852,
  twoFactorEnabled: false,
  updatedAt: 702115,
  username: "Johnnie.Torp54",
};
```

## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `acceptOrgInvites`                                                                | *boolean*                                                                         | :heavy_check_mark:                                                                | N/A                                                                               |
| `acceptedLegalHash`                                                               | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `banExpires`                                                                      | *number*                                                                          | :heavy_check_mark:                                                                | an integer representing a safe Unix timestamp                                     |
| `banReason`                                                                       | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `banned`                                                                          | *boolean*                                                                         | :heavy_check_mark:                                                                | N/A                                                                               |
| `boughtCreditsAfterReferral`                                                      | *boolean*                                                                         | :heavy_check_mark:                                                                | N/A                                                                               |
| `createdAt`                                                                       | *number*                                                                          | :heavy_check_mark:                                                                | an integer representing a safe Unix timestamp                                     |
| `displayUsername`                                                                 | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `email`                                                                           | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `emailVerified`                                                                   | *boolean*                                                                         | :heavy_check_mark:                                                                | N/A                                                                               |
| `flagged`                                                                         | *boolean*                                                                         | :heavy_check_mark:                                                                | N/A                                                                               |
| `id`                                                                              | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `image`                                                                           | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `name`                                                                            | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `referralLink`                                                                    | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `referred`                                                                        | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `restrictedFeatures`                                                              | [operations.RestrictedFeatures](../../models/operations/restricted-features.md)[] | :heavy_check_mark:                                                                | N/A                                                                               |
| `role`                                                                            | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `stripeConnectedId`                                                               | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `stripeId`                                                                        | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `taxState`                                                                        | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `tokens`                                                                          | *number*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |
| `twoFactorEnabled`                                                                | *boolean*                                                                         | :heavy_check_mark:                                                                | N/A                                                                               |
| `updatedAt`                                                                       | *number*                                                                          | :heavy_check_mark:                                                                | an integer representing a safe Unix timestamp                                     |
| `username`                                                                        | *string*                                                                          | :heavy_check_mark:                                                                | N/A                                                                               |