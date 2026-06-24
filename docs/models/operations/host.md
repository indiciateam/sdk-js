# Host

## Example Usage

```typescript
import { Host } from "@indiciaosint/sdk/models/operations";

let value: Host = {
  dollar: {
    starttime: "<value>",
    endtime: "<value>",
  },
  status: [
    {
      dollar: {
        state: "Idaho",
        reason: "<value>",
        reasonTtl: "<value>",
      },
    },
  ],
  address: [],
};
```

## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `dollar`                                                                     | [operations.HostDollar](../../models/operations/host-dollar.md)              | :heavy_check_mark:                                                           | N/A                                                                          |
| `status`                                                                     | [operations.ScanPortsStatus](../../models/operations/scan-ports-status.md)[] | :heavy_check_mark:                                                           | N/A                                                                          |
| `address`                                                                    | [operations.Address](../../models/operations/address.md)[]                   | :heavy_check_mark:                                                           | N/A                                                                          |
| `hostnames`                                                                  | [operations.Hostname2](../../models/operations/hostname2.md)[]               | :heavy_minus_sign:                                                           | N/A                                                                          |
| `ports`                                                                      | [operations.Port2](../../models/operations/port2.md)[]                       | :heavy_minus_sign:                                                           | N/A                                                                          |
| `times`                                                                      | [operations.Time](../../models/operations/time.md)[]                         | :heavy_minus_sign:                                                           | N/A                                                                          |