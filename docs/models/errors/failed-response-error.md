# FailedResponseError

A failed API response.

## Example Usage

```typescript
import { FailedResponseError } from "@indiciaosint/sdk/models/errors";

// No examples available for this model
```

## Fields

| Field                               | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `success`                           | *boolean*                           | :heavy_check_mark:                  | Always `false` for error responses. |
| `error`                             | *string*                            | :heavy_minus_sign:                  | Human-readable error message.       |