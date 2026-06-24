# GeolocateMediaData

Geolocation analysis result.

## Example Usage

```typescript
import { GeolocateMediaData } from "@indiciaosint/sdk/models/operations";

let value: GeolocateMediaData = {
  location: "<value>",
  coordinates: "<value>",
  certainty: "<value>",
  reasoning: "<value>",
};
```

## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `location`                                                          | *string*                                                            | :heavy_check_mark:                                                  | Human-readable location name, or null if undetermined.              |
| `coordinates`                                                       | *string*                                                            | :heavy_check_mark:                                                  | Comma-separated "latitude,longitude" pair, or null if undetermined. |
| `certainty`                                                         | *string*                                                            | :heavy_check_mark:                                                  | Confidence level of the geolocation result.                         |
| `reasoning`                                                         | *string*                                                            | :heavy_check_mark:                                                  | Explanation of how the location was determined.                     |
| `mapsUrl`                                                           | *string*                                                            | :heavy_minus_sign:                                                  | Google Maps URL for the determined coordinates.                     |