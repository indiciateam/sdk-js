# Results

## Example Usage

```typescript
import { Results } from "@indiciaosint/sdk/models/operations";

let value: Results = {
  databases: 9864.4,
  firstSeen: "<value>",
  found: 7221.32,
  lastSeen: "<value>",
};
```

## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `databases`                                                             | *number*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `firstSeen`                                                             | *string*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `found`                                                                 | *number*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `lastSeen`                                                              | *string*                                                                | :heavy_check_mark:                                                      | N/A                                                                     |
| `results`                                                               | [operations.ResultsResult](../../models/operations/results-result.md)[] | :heavy_minus_sign:                                                      | N/A                                                                     |