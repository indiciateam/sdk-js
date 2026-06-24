# StatusEvent

Progress update emitted as the `status` event.

## Example Usage

```typescript
import { StatusEvent } from "@indiciaosint/sdk/models/operations";

let value: StatusEvent = {
  data: "<value>",
  event: "status",
};
```

## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `data`                                                            | *string*                                                          | :heavy_check_mark:                                                | Human-readable progress message (e.g. "Fetching commit history"). |
| `event`                                                           | *"status"*                                                        | :heavy_check_mark:                                                | N/A                                                               |