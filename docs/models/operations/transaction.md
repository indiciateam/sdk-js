# Transaction

## Example Usage

```typescript
import { Transaction } from "@indiciaosint/sdk/models/operations";

let value: Transaction = {
  amount: "816.96",
  coin: "<value>",
  counterparty: "<value>",
  direction: "in",
  fee: "<value>",
  hash: "<value>",
  status: "<value>",
  timestamp: null,
  url: "https://tall-schedule.org/",
};
```

## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `amount`                                                     | *string*                                                     | :heavy_check_mark:                                           | N/A                                                          |
| `coin`                                                       | *string*                                                     | :heavy_check_mark:                                           | N/A                                                          |
| `counterparty`                                               | *string*                                                     | :heavy_check_mark:                                           | N/A                                                          |
| `direction`                                                  | [operations.Direction](../../models/operations/direction.md) | :heavy_check_mark:                                           | N/A                                                          |
| `fee`                                                        | *string*                                                     | :heavy_check_mark:                                           | N/A                                                          |
| `hash`                                                       | *string*                                                     | :heavy_check_mark:                                           | N/A                                                          |
| `status`                                                     | *string*                                                     | :heavy_check_mark:                                           | N/A                                                          |
| `timestamp`                                                  | *string*                                                     | :heavy_check_mark:                                           | N/A                                                          |
| `url`                                                        | *string*                                                     | :heavy_check_mark:                                           | N/A                                                          |