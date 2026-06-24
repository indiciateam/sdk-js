# GeolocateMediaErrorEvent

Terminal event indicating the analysis failed.

## Example Usage

```typescript
import { GeolocateMediaErrorEvent } from "@indiciaosint/sdk/models/operations";

let value: GeolocateMediaErrorEvent = {
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