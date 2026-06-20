# Maps

## Example Usage

```typescript
import { Maps } from "@indiciaosint/sdk/models/operations";

let value: Maps = {
  photos: [],
  reviews: [],
  stats: {
    "key": 5049.6,
    "key1": 3071.88,
    "key2": 169.59,
  },
};
```

## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `photos`                                               | [operations.Photo](../../models/operations/photo.md)[] | :heavy_check_mark:                                     | N/A                                                    |
| `reviews`                                              | Record<string, *any*>[]                                | :heavy_check_mark:                                     | N/A                                                    |
| `stats`                                                | Record<string, *number*>                               | :heavy_check_mark:                                     | N/A                                                    |