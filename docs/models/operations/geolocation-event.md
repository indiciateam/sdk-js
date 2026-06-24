# GeolocationEvent

A Server-Sent Event whose `data` field carries the event payload.

## Example Usage

```typescript
import { GeolocationEvent } from "@indiciaosint/sdk/models/operations";

let value: GeolocationEvent = {
  data: {
    status: "analyzing",
  },
};
```

## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `data`                                                                             | *operations.GeolocationEventData*                                                  | :heavy_check_mark:                                                                 | JSON `data` payload of a geolocation Server-Sent Event. Discriminated by `status`. |