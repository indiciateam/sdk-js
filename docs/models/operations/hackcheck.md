# Hackcheck

## Example Usage

```typescript
import { Hackcheck } from "@indiciaosint/sdk/models/operations";

let value: Hackcheck = {
  results: {
    databases: 953.04,
    firstSeen: "<value>",
    found: 7648.74,
    lastSeen: "<value>",
    results: {
      id: "<id>",
      source: {},
    },
  },
};
```

## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `results`                                                | [operations.Results](../../models/operations/results.md) | :heavy_check_mark:                                       | N/A                                                      |