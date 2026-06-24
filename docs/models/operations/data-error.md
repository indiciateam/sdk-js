# DataError

## Example Usage

```typescript
import { DataError } from "@indiciaosint/sdk/models/operations";

let value: DataError = {
  status: "error",
  success: false,
  error: "<value>",
};
```

## Fields

| Field                         | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `status`                      | *"error"*                     | :heavy_check_mark:            | N/A                           |
| `success`                     | *false*                       | :heavy_check_mark:            | N/A                           |
| `error`                       | *string*                      | :heavy_check_mark:            | Human-readable error message. |