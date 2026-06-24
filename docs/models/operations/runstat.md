# Runstat

## Example Usage

```typescript
import { Runstat } from "@indiciaosint/sdk/models/operations";

let value: Runstat = {
  finished: [
    {
      dollar: {
        time: "<value>",
        timestr: "<value>",
        summary: "<value>",
        elapsed: "<value>",
        exit: "<value>",
      },
    },
  ],
  hosts: [],
};
```

## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `finished`                                                          | [operations.Finished](../../models/operations/finished.md)[]        | :heavy_check_mark:                                                  | N/A                                                                 |
| `hosts`                                                             | [operations.RunstatHost](../../models/operations/runstat-host.md)[] | :heavy_check_mark:                                                  | N/A                                                                 |