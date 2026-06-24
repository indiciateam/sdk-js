# ProgressEvent

Progress update emitted periodically during the scan.

## Example Usage

```typescript
import { ProgressEvent } from "@indiciaosint/sdk/models/operations";

let value: ProgressEvent = {
  status: "progress",
  task: "<value>",
  percent: 8379.48,
};
```

## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `status`                                   | *"progress"*                               | :heavy_check_mark:                         | N/A                                        |
| `task`                                     | *string*                                   | :heavy_check_mark:                         | Name of the running nmap task.             |
| `percent`                                  | *number*                                   | :heavy_check_mark:                         | Completion percentage of the current task. |