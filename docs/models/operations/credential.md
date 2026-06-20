# Credential

## Example Usage

```typescript
import { Credential } from "@indiciaosint/sdk/models/operations";

let value: Credential = {
  logInfo: {
    hwid: "<id>",
    name: "<value>",
    systemName: "<value>",
  },
};
```

## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `logInfo`                                                 | [operations.LogInfo](../../models/operations/log-info.md) | :heavy_check_mark:                                        | N/A                                                       |
| `date`                                                    | *string*                                                  | :heavy_minus_sign:                                        | N/A                                                       |
| `login`                                                   | *string*                                                  | :heavy_minus_sign:                                        | N/A                                                       |
| `password`                                                | *string*                                                  | :heavy_minus_sign:                                        | N/A                                                       |
| `url`                                                     | *string*                                                  | :heavy_minus_sign:                                        | N/A                                                       |