# ScanPortsService

## Example Usage

```typescript
import { ScanPortsService } from "@indiciaosint/sdk/models/operations";

let value: ScanPortsService = {
  dollar: {
    name: "<value>",
    method: "<value>",
    conf: "<value>",
  },
};
```

## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `dollar`                                                              | [operations.ServiceDollar](../../models/operations/service-dollar.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `cpe`                                                                 | *string*[]                                                            | :heavy_minus_sign:                                                    | N/A                                                                   |