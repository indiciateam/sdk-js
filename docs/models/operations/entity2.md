# Entity2

## Example Usage

```typescript
import { Entity2 } from "@indiciaosint/sdk/models/operations";

let value: Entity2 = {
  handle: "<value>",
  links: [
    {
      "key": "<value>",
    },
  ],
  roles: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
  vcardArray: [
    "<value>",
  ],
};
```

## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `handle`                                                   | *string*                                                   | :heavy_check_mark:                                         | N/A                                                        |
| `links`                                                    | Record<string, *string*>[]                                 | :heavy_check_mark:                                         | N/A                                                        |
| `roles`                                                    | *string*[]                                                 | :heavy_check_mark:                                         | N/A                                                        |
| `vcardArray`                                               | *operations.VcardArrayUnion2*[]                            | :heavy_check_mark:                                         | N/A                                                        |
| `entities`                                                 | [operations.Entity1](../../models/operations/entity1.md)[] | :heavy_minus_sign:                                         | N/A                                                        |