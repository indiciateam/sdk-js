# Ssh

## Example Usage

```typescript
import { Ssh } from "@indiciaosint/sdk/models/operations";

let value: Ssh = {
  cipher: "<value>",
  fingerprint: "<value>",
  hassh: "<value>",
  kex: {
    compressionAlgorithms: [
      "<value 1>",
    ],
    encryptionAlgorithms: [
      "<value 1>",
      "<value 2>",
    ],
    kexAlgorithms: [
      "<value 1>",
    ],
    keyFollows: false,
    languages: [
      "<value 1>",
    ],
    macAlgorithms: [
      "<value 1>",
      "<value 2>",
      "<value 3>",
    ],
    serverHostKeyAlgorithms: [],
    unused: 1137.36,
  },
  key: "<key>",
  mac: "c6:6b:71:ec:03:4a",
  type: "<value>",
};
```

## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `cipher`                                         | *string*                                         | :heavy_check_mark:                               | N/A                                              |
| `fingerprint`                                    | *string*                                         | :heavy_check_mark:                               | N/A                                              |
| `hassh`                                          | *string*                                         | :heavy_check_mark:                               | N/A                                              |
| `kex`                                            | [operations.Kex](../../models/operations/kex.md) | :heavy_check_mark:                               | N/A                                              |
| `key`                                            | *string*                                         | :heavy_check_mark:                               | N/A                                              |
| `mac`                                            | *string*                                         | :heavy_check_mark:                               | N/A                                              |
| `type`                                           | *string*                                         | :heavy_check_mark:                               | N/A                                              |