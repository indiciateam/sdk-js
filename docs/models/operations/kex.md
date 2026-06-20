# Kex

## Example Usage

```typescript
import { Kex } from "@indiciaosint/sdk/models/operations";

let value: Kex = {
  compressionAlgorithms: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
  encryptionAlgorithms: [
    "<value 1>",
  ],
  kexAlgorithms: [
    "<value 1>",
    "<value 2>",
  ],
  keyFollows: true,
  languages: [
    "<value 1>",
  ],
  macAlgorithms: [],
  serverHostKeyAlgorithms: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
  unused: 7334.6,
};
```

## Fields

| Field                     | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `compressionAlgorithms`   | *string*[]                | :heavy_check_mark:        | N/A                       |
| `encryptionAlgorithms`    | *string*[]                | :heavy_check_mark:        | N/A                       |
| `kexAlgorithms`           | *string*[]                | :heavy_check_mark:        | N/A                       |
| `keyFollows`              | *boolean*                 | :heavy_check_mark:        | N/A                       |
| `languages`               | *string*[]                | :heavy_check_mark:        | N/A                       |
| `macAlgorithms`           | *string*[]                | :heavy_check_mark:        | N/A                       |
| `serverHostKeyAlgorithms` | *string*[]                | :heavy_check_mark:        | N/A                       |
| `unused`                  | *number*                  | :heavy_check_mark:        | N/A                       |