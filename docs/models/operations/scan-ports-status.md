# ScanPortsStatus

## Example Usage

```typescript
import { ScanPortsStatus } from "@indiciaosint/sdk/models/operations";

let value: ScanPortsStatus = {
  dollar: {
    state: "Idaho",
    reason: "<value>",
    reasonTtl: "<value>",
  },
};
```

## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dollar`                                                            | [operations.StatusDollar](../../models/operations/status-dollar.md) | :heavy_check_mark:                                                  | N/A                                                                 |