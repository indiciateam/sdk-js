# Cert

## Example Usage

```typescript
import { Cert } from "@indiciaosint/sdk/models/operations";

let value: Cert = {};
```

## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `expired`                                                      | *boolean*                                                      | :heavy_minus_sign:                                             | N/A                                                            |
| `expires`                                                      | *string*                                                       | :heavy_minus_sign:                                             | N/A                                                            |
| `extensions`                                                   | [operations.Extension](../../models/operations/extension.md)[] | :heavy_minus_sign:                                             | N/A                                                            |
| `fingerprint`                                                  | Record<string, *string*>                                       | :heavy_minus_sign:                                             | N/A                                                            |
| `issued`                                                       | *string*                                                       | :heavy_minus_sign:                                             | N/A                                                            |
| `issuer`                                                       | [operations.Issuer](../../models/operations/issuer.md)         | :heavy_minus_sign:                                             | N/A                                                            |
| `pubkey`                                                       | [operations.Pubkey](../../models/operations/pubkey.md)         | :heavy_minus_sign:                                             | N/A                                                            |
| `serial`                                                       | *number*                                                       | :heavy_minus_sign:                                             | N/A                                                            |
| `sigAlg`                                                       | *string*                                                       | :heavy_minus_sign:                                             | N/A                                                            |
| `subject`                                                      | [operations.Subject](../../models/operations/subject.md)       | :heavy_minus_sign:                                             | N/A                                                            |
| `version`                                                      | *number*                                                       | :heavy_minus_sign:                                             | N/A                                                            |