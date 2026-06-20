# GetV1InfoResponse

Successful response with user information.

## Example Usage

```typescript
import { GetV1InfoResponse } from "@indiciaosint/sdk/models/operations";

let value: GetV1InfoResponse = {
  key: {
    createdAt: 270808,
    enabled: false,
    expiresAt: 360080,
    id: "<id>",
    lastRefillAt: 773093,
    lastRequest: null,
    metadata: {
      "key": "<value>",
      "key1": "<value>",
      "key2": "<value>",
    },
    name: "<value>",
    permissions: {
      "key": [
        "<value 1>",
        "<value 2>",
      ],
    },
    prefix: "<value>",
    rateLimitEnabled: true,
    rateLimitMax: 2582.74,
    rateLimitTimeWindow: 5638.93,
    refillAmount: null,
    refillInterval: 7030.89,
    remaining: null,
    requestCount: 6407.08,
    start: null,
    updatedAt: 287223,
    userId: "<id>",
  },
  success: true,
  user: {
    acceptOrgInvites: true,
    acceptedLegalHash: "<value>",
    banExpires: 728624,
    banReason: "<value>",
    banned: true,
    boughtCreditsAfterReferral: true,
    createdAt: 437257,
    displayUsername: "<value>",
    email: "Claudie_Purdy@gmail.com",
    emailVerified: true,
    flagged: null,
    id: "<id>",
    image: "https://picsum.photos/seed/rCkcjDPw8D/51/1433",
    name: "<value>",
    referralLink: "<value>",
    referred: "<value>",
    restrictedFeatures: [
      "fr",
    ],
    role: "<value>",
    stripeConnectedId: "<id>",
    stripeId: "<id>",
    taxState: "<value>",
    tokens: 12146,
    twoFactorEnabled: true,
    updatedAt: 954581,
    username: null,
  },
};
```

## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `key`                                              | [operations.Key](../../models/operations/key.md)   | :heavy_check_mark:                                 | N/A                                                |
| `success`                                          | *boolean*                                          | :heavy_check_mark:                                 | N/A                                                |
| `user`                                             | [operations.User](../../models/operations/user.md) | :heavy_check_mark:                                 | N/A                                                |