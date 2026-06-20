# ResultSource

## Example Usage

```typescript
import { ResultSource } from "@indiciaosint/sdk/models/operations";

let value: ResultSource = {
  breachDate: "<value>",
  compilation: "1",
  name: "<value>",
  passwordless: "0",
  unverified: "0",
};
```

## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `breachDate`                                                       | *string*                                                           | :heavy_check_mark:                                                 | N/A                                                                |
| `compilation`                                                      | [operations.Compilation](../../models/operations/compilation.md)   | :heavy_check_mark:                                                 | N/A                                                                |
| `name`                                                             | *string*                                                           | :heavy_check_mark:                                                 | N/A                                                                |
| `passwordless`                                                     | [operations.Passwordless](../../models/operations/passwordless.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `unverified`                                                       | [operations.Unverified](../../models/operations/unverified.md)     | :heavy_check_mark:                                                 | N/A                                                                |