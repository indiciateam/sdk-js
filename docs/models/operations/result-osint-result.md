# ResultOsintResult

A single service's username lookup result.

## Example Usage

```typescript
import { ResultOsintResult } from "@indiciaosint/sdk/models/operations";

let value: ResultOsintResult = {
  durationMs: 2335.03,
  exists: false,
  service: "<value>",
  type: "username",
};
```

## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `durationMs`                                                    | *number*                                                        | :heavy_check_mark:                                              | N/A                                                             |
| `exists`                                                        | *boolean*                                                       | :heavy_check_mark:                                              | N/A                                                             |
| `service`                                                       | *string*                                                        | :heavy_check_mark:                                              | N/A                                                             |
| `type`                                                          | [operations.ResultType](../../models/operations/result-type.md) | :heavy_check_mark:                                              | N/A                                                             |
| `data`                                                          | [operations.ResultData](../../models/operations/result-data.md) | :heavy_minus_sign:                                              | N/A                                                             |
| `error`                                                         | *string*                                                        | :heavy_minus_sign:                                              | N/A                                                             |