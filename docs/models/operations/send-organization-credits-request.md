# SendOrganizationCreditsRequest

## Example Usage

```typescript
import { SendOrganizationCreditsRequest } from "@indiciaosint/sdk/models/operations";

let value: SendOrganizationCreditsRequest = {
  id: "<id>",
  body: {
    creditsEach: 5417.71,
    recipientMemberIds: [
      "<value 1>",
    ],
  },
};
```

## Fields

| Field                                                                                                              | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                               | *string*                                                                                                           | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |
| `body`                                                                                                             | [operations.SendOrganizationCreditsRequestBody](../../models/operations/send-organization-credits-request-body.md) | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |