# GeolocateMediaCompleteEvent

Terminal event containing the geolocation result.

## Example Usage

```typescript
import { GeolocateMediaCompleteEvent } from "@indiciaosint/sdk/models/operations";

let value: GeolocateMediaCompleteEvent = {
  status: "complete",
  success: true,
  data: {
    location: "<value>",
    coordinates: "<value>",
    certainty: "<value>",
    reasoning: "<value>",
  },
};
```

## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `status`                                                                         | *"complete"*                                                                     | :heavy_check_mark:                                                               | N/A                                                                              |
| `success`                                                                        | *true*                                                                           | :heavy_check_mark:                                                               | N/A                                                                              |
| `data`                                                                           | [operations.GeolocateMediaData](../../models/operations/geolocate-media-data.md) | :heavy_check_mark:                                                               | Geolocation analysis result.                                                     |