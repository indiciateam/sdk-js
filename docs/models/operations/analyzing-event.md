# AnalyzingEvent

Progress heartbeat emitted while analysis is in progress. Sent immediately on connection and then roughly every 10 seconds to keep the connection alive.

## Example Usage

```typescript
import { AnalyzingEvent } from "@indiciaosint/sdk/models/operations";

let value: AnalyzingEvent = {
  status: "analyzing",
};
```

## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `status`                                  | *"analyzing"*                             | :heavy_check_mark:                        | N/A                                       |
| `timestamp`                               | *number*                                  | :heavy_minus_sign:                        | Unix epoch milliseconds of the heartbeat. |