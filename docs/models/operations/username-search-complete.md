# UsernameSearchComplete

The complete result set, emitted once every service has run.

## Example Usage

```typescript
import { UsernameSearchComplete } from "@indiciaosint/sdk/models/operations";

let value: UsernameSearchComplete = {
  results: [
    {
      durationMs: 313.82,
      exists: false,
      service: "<value>",
      type: "email",
    },
  ],
};
```

## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `results`                                                                        | [operations.ResultOsintResult](../../models/operations/result-osint-result.md)[] | :heavy_check_mark:                                                               | All OSINT results collected across every checked service.                        |
| `activityId`                                                                     | *string*                                                                         | :heavy_minus_sign:                                                               | Activity log id for this search, or null.                                        |