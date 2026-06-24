# Port1

## Example Usage

```typescript
import { Port1 } from "@indiciaosint/sdk/models/operations";

let value: Port1 = {
  dollar: {
    protocol: "<value>",
    portid: "<id>",
  },
  state: [
    {
      dollar: {
        state: "Colorado",
        reason: "<value>",
        reasonTtl: "<value>",
      },
    },
  ],
};
```

## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `dollar`                                                                       | [operations.PortDollar](../../models/operations/port-dollar.md)                | :heavy_check_mark:                                                             | N/A                                                                            |
| `state`                                                                        | [operations.State](../../models/operations/state.md)[]                         | :heavy_check_mark:                                                             | N/A                                                                            |
| `service`                                                                      | [operations.ScanPortsService](../../models/operations/scan-ports-service.md)[] | :heavy_minus_sign:                                                             | N/A                                                                            |