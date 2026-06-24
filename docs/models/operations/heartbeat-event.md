# HeartbeatEvent

Keep-alive emitted roughly every 15s as the `heartbeat` event.

## Example Usage

```typescript
import { HeartbeatEvent } from "@indiciaosint/sdk/models/operations";

let value: HeartbeatEvent = {
  data: "<value>",
  event: "heartbeat",
};
```

## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `data`                                        | *string*                                      | :heavy_check_mark:                            | Keep-alive heartbeat. Always an empty string. |
| `event`                                       | *"heartbeat"*                                 | :heavy_check_mark:                            | N/A                                           |