# AnalyzeCryptoAddressData

## Example Usage

```typescript
import { AnalyzeCryptoAddressData } from "@indiciaosint/sdk/models/operations";

let value: AnalyzeCryptoAddressData = {
  address: "14521 Ash Grove",
  balance: "<value>",
  balanceUsd: 3819.98,
  coin: "<value>",
  explorerUrl: "https://stingy-help.net/",
  label: "<value>",
  network: "<value>",
  priceUsd: 4070.12,
  tokens: [
    {
      amount: "39.52",
      contract: "<value>",
      icon: "<value>",
      name: "<value>",
      symbol: "<value>",
      valueUsd: 3462.73,
    },
  ],
  totalReceived: "<value>",
  totalSent: "<value>",
  transactions: [],
  txCount: 1485.84,
};
```

## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `address`                                                          | *string*                                                           | :heavy_check_mark:                                                 | N/A                                                                |
| `balance`                                                          | *string*                                                           | :heavy_check_mark:                                                 | N/A                                                                |
| `balanceUsd`                                                       | *number*                                                           | :heavy_check_mark:                                                 | N/A                                                                |
| `coin`                                                             | *string*                                                           | :heavy_check_mark:                                                 | N/A                                                                |
| `explorerUrl`                                                      | *string*                                                           | :heavy_check_mark:                                                 | N/A                                                                |
| `label`                                                            | *string*                                                           | :heavy_check_mark:                                                 | N/A                                                                |
| `network`                                                          | *string*                                                           | :heavy_check_mark:                                                 | N/A                                                                |
| `priceUsd`                                                         | *number*                                                           | :heavy_check_mark:                                                 | N/A                                                                |
| `tokens`                                                           | [operations.Token](../../models/operations/token.md)[]             | :heavy_check_mark:                                                 | N/A                                                                |
| `totalReceived`                                                    | *string*                                                           | :heavy_check_mark:                                                 | N/A                                                                |
| `totalSent`                                                        | *string*                                                           | :heavy_check_mark:                                                 | N/A                                                                |
| `transactions`                                                     | [operations.Transaction](../../models/operations/transaction.md)[] | :heavy_check_mark:                                                 | N/A                                                                |
| `txCount`                                                          | *number*                                                           | :heavy_check_mark:                                                 | N/A                                                                |