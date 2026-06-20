# SearchWebDatabasesTimeline

## Example Usage

```typescript
import { SearchWebDatabasesTimeline } from "@indiciaosint/sdk/models/operations";

let value: SearchWebDatabasesTimeline = {
  groupItems: {
    "key": "<value>",
    "key1": "<value>",
    "key2": "<value>",
  },
  groupYears: {
    "key": "<value>",
    "key1": "<value>",
  },
  groups: {
    "key": "<value>",
    "key1": "<value>",
  },
  lastSeen: true,
  lastSeenDate: "<value>",
  registered: false,
  registeredDate: null,
};
```

## Fields

| Field                 | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `groupItems`          | Record<string, *any*> | :heavy_check_mark:    | N/A                   |
| `groupYears`          | Record<string, *any*> | :heavy_check_mark:    | N/A                   |
| `groups`              | Record<string, *any*> | :heavy_check_mark:    | N/A                   |
| `lastSeen`            | *boolean*             | :heavy_check_mark:    | N/A                   |
| `lastSeenDate`        | *string*              | :heavy_check_mark:    | N/A                   |
| `registered`          | *boolean*             | :heavy_check_mark:    | N/A                   |
| `registeredDate`      | *string*              | :heavy_check_mark:    | N/A                   |