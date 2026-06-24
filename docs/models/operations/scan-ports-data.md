# ScanPortsData

Parsed nmap scan result.

## Example Usage

```typescript
import { ScanPortsData } from "@indiciaosint/sdk/models/operations";

let value: ScanPortsData = {
  dollar: {
    scanner: "<value>",
    args: "<value>",
    start: "<value>",
    startstr: "<value>",
    version: "<value>",
    xmloutputversion: "<value>",
  },
  scaninfo: [],
  verbose: [],
  debugging: [
    {
      dollar: {
        level: "<value>",
      },
    },
  ],
  runstats: [],
};
```

## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `dollar`                                                             | [operations.Dollar](../../models/operations/dollar.md)               | :heavy_check_mark:                                                   | N/A                                                                  |
| `scaninfo`                                                           | [operations.Scaninfo](../../models/operations/scaninfo.md)[]         | :heavy_check_mark:                                                   | N/A                                                                  |
| `verbose`                                                            | [operations.Verbose](../../models/operations/verbose.md)[]           | :heavy_check_mark:                                                   | N/A                                                                  |
| `debugging`                                                          | [operations.Debugging](../../models/operations/debugging.md)[]       | :heavy_check_mark:                                                   | N/A                                                                  |
| `taskprogress`                                                       | [operations.Taskprogress](../../models/operations/taskprogress.md)[] | :heavy_minus_sign:                                                   | N/A                                                                  |
| `host`                                                               | [operations.Host](../../models/operations/host.md)[]                 | :heavy_minus_sign:                                                   | N/A                                                                  |
| `runstats`                                                           | [operations.Runstat](../../models/operations/runstat.md)[]           | :heavy_check_mark:                                                   | N/A                                                                  |