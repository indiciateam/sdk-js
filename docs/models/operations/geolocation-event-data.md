# GeolocationEventData

JSON `data` payload of a geolocation Server-Sent Event. Discriminated by `status`.


## Supported Types

### `operations.AnalyzingEvent`

```typescript
const value: operations.AnalyzingEvent = {
  status: "analyzing",
};
```

### `operations.GeolocateMediaCompleteEvent`

```typescript
const value: operations.GeolocateMediaCompleteEvent = {
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

### `operations.GeolocateMediaErrorEvent`

```typescript
const value: operations.GeolocateMediaErrorEvent = {
  status: "error",
  success: false,
  error: "<value>",
};
```

