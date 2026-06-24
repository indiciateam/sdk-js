# PortscanEvent

A Server-Sent Event whose `data` field carries the event payload.

## Example Usage

```typescript
import { PortscanEvent } from "@indiciaosint/sdk/models/operations";

let value: PortscanEvent = {
  data: {
    status: "scanning",
  },
};
```

## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `data`                                                                           | *operations.PortscanEventData*                                                   | :heavy_check_mark:                                                               | JSON `data` payload of a port-scan Server-Sent Event. Discriminated by `status`. |