# PortscanEventData

JSON `data` payload of a port-scan Server-Sent Event. Discriminated by `status`.


## Supported Types

### `operations.ScanningEvent`

```typescript
const value: operations.ScanningEvent = {
  status: "scanning",
};
```

### `operations.ProgressEvent`

```typescript
const value: operations.ProgressEvent = {
  status: "progress",
  task: "<value>",
  percent: 8379.48,
};
```

### `operations.ScanPortsCompleteEvent`

```typescript
const value: operations.ScanPortsCompleteEvent = {
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

### `operations.ScanPortsErrorEvent`

```typescript
const value: operations.ScanPortsErrorEvent = {
  status: "error",
  success: false,
  error: "<value>",
};
```

