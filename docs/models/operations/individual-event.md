# IndividualEvent

Emitted as the `individual` event for each service checked.

## Example Usage

```typescript
import { IndividualEvent } from "@indiciaosint/sdk/models/operations";

let value: IndividualEvent = {
  data: {
    durationMs: 2893.99,
    exists: true,
    service: "<value>",
    type: "email",
  },
  event: "individual",
};
```

## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `data`                                                            | [operations.OsintResult](../../models/operations/osint-result.md) | :heavy_check_mark:                                                | A single service's username lookup result.                        |
| `event`                                                           | *"individual"*                                                    | :heavy_check_mark:                                                | N/A                                                               |