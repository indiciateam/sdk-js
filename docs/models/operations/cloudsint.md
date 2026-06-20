# Cloudsint

## Example Usage

```typescript
import { Cloudsint } from "@indiciaosint/sdk/models/operations";

let value: Cloudsint = {
  data: {
    breaches: [],
    query: "<value>",
    totalMatches: 1630.65,
  },
  duration: 9245.48,
  success: true,
};
```

## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `data`                                                                | [operations.CloudsintData](../../models/operations/cloudsint-data.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `duration`                                                            | *number*                                                              | :heavy_check_mark:                                                    | N/A                                                                   |
| `success`                                                             | *boolean*                                                             | :heavy_check_mark:                                                    | N/A                                                                   |