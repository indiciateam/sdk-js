# Ssl

## Example Usage

```typescript
import { Ssl } from "@indiciaosint/sdk/models/operations";

let value: Ssl = {};
```

## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `acceptableCas`                                            | *string*[]                                                 | :heavy_minus_sign:                                         | N/A                                                        |
| `alpn`                                                     | *string*[]                                                 | :heavy_minus_sign:                                         | N/A                                                        |
| `cert`                                                     | [operations.Cert](../../models/operations/cert.md)         | :heavy_minus_sign:                                         | N/A                                                        |
| `chain`                                                    | *string*[]                                                 | :heavy_minus_sign:                                         | N/A                                                        |
| `chainSha256`                                              | *string*[]                                                 | :heavy_minus_sign:                                         | N/A                                                        |
| `cipher`                                                   | [operations.Cipher](../../models/operations/cipher.md)     | :heavy_minus_sign:                                         | N/A                                                        |
| `handshakeStates`                                          | *string*[]                                                 | :heavy_minus_sign:                                         | N/A                                                        |
| `ja3s`                                                     | *string*                                                   | :heavy_minus_sign:                                         | N/A                                                        |
| `jarm`                                                     | *string*                                                   | :heavy_minus_sign:                                         | N/A                                                        |
| `tlstext`                                                  | [operations.Tlstext](../../models/operations/tlstext.md)[] | :heavy_minus_sign:                                         | N/A                                                        |
| `trust`                                                    | [operations.Trust](../../models/operations/trust.md)       | :heavy_minus_sign:                                         | N/A                                                        |
| `versions`                                                 | *operations.Versions*                                      | :heavy_minus_sign:                                         | N/A                                                        |