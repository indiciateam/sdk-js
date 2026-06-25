# GetInfoResponse

Successful response with user information.

## Example Usage

```typescript
import { GetInfoResponse } from "@indiciaosint/sdk/models/operations";

let value: GetInfoResponse = {
  key: {
    createdAt: 947046,
    enabled: false,
    expiresAt: 11336,
    id: "<id>",
    lastRefillAt: 808345,
    lastRequest: 458446,
    metadata: {
      "key": "<value>",
      "key1": "<value>",
      "key2": "<value>",
    },
    name: "<value>",
    permissions: {},
    prefix: "<value>",
    rateLimitEnabled: true,
    rateLimitMax: 7790.75,
    rateLimitTimeWindow: 7688.14,
    refillAmount: 5501.88,
    refillInterval: null,
    remaining: 4043.37,
    requestCount: 1145.96,
    start: "<value>",
    updatedAt: 328476,
    userId: "<id>",
  },
  success: false,
  user: {
    acceptOrgInvites: false,
    acceptedLegalHash: null,
    banExpires: 967694,
    banReason: "<value>",
    banned: true,
    boughtCreditsAfterReferral: false,
    createdAt: 480036,
    displayUsername: null,
    email: "Pete90@yahoo.com",
    emailVerified: false,
    flagged: false,
    id: "<id>",
    image: "https://loremflickr.com/1437/3528?lock=5692418761134883",
    name: "<value>",
    referralLink: "<value>",
    referred: "<value>",
    restrictedFeatures: [
      "seon",
    ],
    role: "<value>",
    stripeConnectedId: "<id>",
    stripeId: null,
    taxState: "<value>",
    tokens: null,
    twoFactorEnabled: true,
    updatedAt: 740618,
    username: "Marcelino.Ratke",
  },
};
```

## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `key`                                              | [operations.Key](../../models/operations/key.md)   | :heavy_check_mark:                                 | N/A                                                |
| `success`                                          | *boolean*                                          | :heavy_check_mark:                                 | N/A                                                |
| `user`                                             | [operations.User](../../models/operations/user.md) | :heavy_check_mark:                                 | N/A                                                |