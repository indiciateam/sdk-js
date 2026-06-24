# ScanPortsCompleteEvent

Terminal event containing the parsed scan result.

## Example Usage

```typescript
import { ScanPortsCompleteEvent } from "@indiciaosint/sdk/models/operations";

let value: ScanPortsCompleteEvent = {
  status: "complete",
  data: {
    dollar: {
      scanner: "<value>",
      args: "<value>",
      start: "<value>",
      startstr: "<value>",
      version: "<value>",
      xmloutputversion: "<value>",
    },
    scaninfo: [
      {
        dollar: {
          type: "<value>",
          protocol: "<value>",
          numservices: "<value>",
          services: "<value>",
        },
      },
    ],
    verbose: [
      {
        dollar: {
          level: "<value>",
        },
      },
    ],
    debugging: [
      {
        dollar: {
          level: "<value>",
        },
      },
    ],
    runstats: [],
  },
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `status`                                                               | *"complete"*                                                           | :heavy_check_mark:                                                     | N/A                                                                    |
| `data`                                                                 | [operations.ScanPortsData](../../models/operations/scan-ports-data.md) | :heavy_check_mark:                                                     | Parsed nmap scan result.                                               |