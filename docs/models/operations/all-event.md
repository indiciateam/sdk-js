# AllEvent

Terminal `all` event with the complete result set.

## Example Usage

```typescript
import { AllEvent } from "@indiciaosint/sdk/models/operations";

let value: AllEvent = {
  data: {
    results: [],
  },
  event: "all",
};
```

## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `data`                                                                                   | [operations.UsernameSearchComplete](../../models/operations/username-search-complete.md) | :heavy_check_mark:                                                                       | The complete result set, emitted once every service has run.                             |
| `event`                                                                                  | *"all"*                                                                                  | :heavy_check_mark:                                                                       | N/A                                                                                      |