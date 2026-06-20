# Cert

## Example Usage

```typescript
import { Cert } from "@indiciaosint/sdk/models/operations";

let value: Cert = {
  expired: true,
  expires: "<value>",
  extensions: [],
  fingerprint: {
    "key": "<value>",
    "key1": "<value>",
  },
  issued: "<value>",
  issuer: {},
  pubkey: {
    bits: 3376.33,
    type: "<value>",
  },
  serial: 8628.55,
  sigAlg: "<value>",
  subject: {},
  version: 3283.73,
};
```

## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `expired`                                                      | *boolean*                                                      | :heavy_check_mark:                                             | N/A                                                            |
| `expires`                                                      | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `extensions`                                                   | [operations.Extension](../../models/operations/extension.md)[] | :heavy_check_mark:                                             | N/A                                                            |
| `fingerprint`                                                  | Record<string, *string*>                                       | :heavy_check_mark:                                             | N/A                                                            |
| `issued`                                                       | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `issuer`                                                       | [operations.Issuer](../../models/operations/issuer.md)         | :heavy_check_mark:                                             | N/A                                                            |
| `pubkey`                                                       | [operations.Pubkey](../../models/operations/pubkey.md)         | :heavy_check_mark:                                             | N/A                                                            |
| `serial`                                                       | *number*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `sigAlg`                                                       | *string*                                                       | :heavy_check_mark:                                             | N/A                                                            |
| `subject`                                                      | [operations.Subject](../../models/operations/subject.md)       | :heavy_check_mark:                                             | N/A                                                            |
| `version`                                                      | *number*                                                       | :heavy_check_mark:                                             | N/A                                                            |