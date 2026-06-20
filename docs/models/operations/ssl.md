# Ssl

## Example Usage

```typescript
import { Ssl } from "@indiciaosint/sdk/models/operations";

let value: Ssl = {
  acceptableCas: [
    "<value 1>",
  ],
  alpn: [
    "<value 1>",
    "<value 2>",
    "<value 3>",
  ],
  cert: {
    expired: true,
    expires: "<value>",
    extensions: [
      {
        data: "<value>",
        name: "<value>",
      },
    ],
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
    serial: 1157.95,
    sigAlg: "<value>",
    subject: {},
    version: 1337.5,
  },
  chain: [
    "<value 1>",
  ],
  chainSha256: [],
  cipher: {
    bits: 3092.41,
    name: "<value>",
    version: "<value>",
  },
  handshakeStates: [
    "<value 1>",
  ],
  ja3s: "<value>",
  jarm: "<value>",
  tlstext: [
    {
      id: 9710.88,
      name: "<value>",
    },
  ],
  trust: {
    revoked: true,
  },
  versions: "<value>",
};
```

## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `acceptableCas`                                            | *string*[]                                                 | :heavy_check_mark:                                         | N/A                                                        |
| `alpn`                                                     | *string*[]                                                 | :heavy_check_mark:                                         | N/A                                                        |
| `cert`                                                     | [operations.Cert](../../models/operations/cert.md)         | :heavy_check_mark:                                         | N/A                                                        |
| `chain`                                                    | *string*[]                                                 | :heavy_check_mark:                                         | N/A                                                        |
| `chainSha256`                                              | *string*[]                                                 | :heavy_check_mark:                                         | N/A                                                        |
| `cipher`                                                   | [operations.Cipher](../../models/operations/cipher.md)     | :heavy_check_mark:                                         | N/A                                                        |
| `handshakeStates`                                          | *string*[]                                                 | :heavy_check_mark:                                         | N/A                                                        |
| `ja3s`                                                     | *string*                                                   | :heavy_check_mark:                                         | N/A                                                        |
| `jarm`                                                     | *string*                                                   | :heavy_check_mark:                                         | N/A                                                        |
| `tlstext`                                                  | [operations.Tlstext](../../models/operations/tlstext.md)[] | :heavy_check_mark:                                         | N/A                                                        |
| `trust`                                                    | [operations.Trust](../../models/operations/trust.md)       | :heavy_check_mark:                                         | N/A                                                        |
| `versions`                                                 | *string*                                                   | :heavy_check_mark:                                         | N/A                                                        |