# Ghosint

## Example Usage

```typescript
import { Ghosint } from "@indiciaosint/sdk/models/operations";

let value: Ghosint = {
  count: 2002.28,
  credentials: [
    {
      logInfo: {
        hwid: "<id>",
        name: "<value>",
        systemName: "<value>",
      },
    },
  ],
  resultId: "<id>",
};
```

## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `count`                                                          | *number*                                                         | :heavy_check_mark:                                               | N/A                                                              |
| `credentials`                                                    | [operations.Credential](../../models/operations/credential.md)[] | :heavy_check_mark:                                               | N/A                                                              |
| `resultId`                                                       | *string*                                                         | :heavy_check_mark:                                               | N/A                                                              |