# PlatformVariable

## Example Usage

```typescript
import { PlatformVariable } from "@indiciaosint/sdk/models/operations";

let value: PlatformVariable = {
  key: "<key>",
  properKey: "<value>",
  type: "number",
  value: false,
};
```

## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `key`                                                                                | *string*                                                                             | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `properKey`                                                                          | *string*                                                                             | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `type`                                                                               | [operations.PlatformVariableType](../../models/operations/platform-variable-type.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `value`                                                                              | *operations.ValueUnion*                                                              | :heavy_check_mark:                                                                   | N/A                                                                                  |