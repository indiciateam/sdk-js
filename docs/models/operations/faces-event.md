# FacesEvent

Emitted as the `faces` event once detection completes.

## Example Usage

```typescript
import { FacesEvent } from "@indiciaosint/sdk/models/operations";

let value: FacesEvent = {
  data: "<value>",
  event: "faces",
};
```

## Fields

| Field                                                                                                                             | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                                            | *string*                                                                                                                          | :heavy_check_mark:                                                                                                                | Number of faces detected in the uploaded image, as a decimal string (5 credits charged per face). "0" means no face was detected. |
| `event`                                                                                                                           | *"faces"*                                                                                                                         | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |