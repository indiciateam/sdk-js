# SearchWhoisData

## Example Usage

```typescript
import { SearchWhoisData } from "@indiciaosint/sdk/models/operations";

let value: SearchWhoisData = {
  dates: {},
  dnssec: {
    "key": "<value>",
    "key1": "<value>",
  },
  domain: "lone-apparatus.name",
  nameservers: [
    {
      "key": "<value>",
      "key1": "<value>",
      "key2": "<value>",
    },
    {},
    {
      "key": "<value>",
    },
  ],
  raw: {},
  registrar: {
    abuseEmail: "<value>",
    abusePhone: "<value>",
    ianaId: "<id>",
    name: "<value>",
    url: "https://busy-gloom.com",
  },
  status: [],
};
```

## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `dates`                                                      | [operations.Dates](../../models/operations/dates.md)         | :heavy_check_mark:                                           | N/A                                                          |
| `dnssec`                                                     | Record<string, *any*>                                        | :heavy_check_mark:                                           | N/A                                                          |
| `domain`                                                     | *string*                                                     | :heavy_check_mark:                                           | N/A                                                          |
| `nameservers`                                                | Record<string, *any*>[]                                      | :heavy_check_mark:                                           | N/A                                                          |
| `raw`                                                        | [operations.Raw](../../models/operations/raw.md)             | :heavy_check_mark:                                           | N/A                                                          |
| `registrar`                                                  | [operations.Registrar](../../models/operations/registrar.md) | :heavy_check_mark:                                           | N/A                                                          |
| `status`                                                     | *string*[]                                                   | :heavy_check_mark:                                           | N/A                                                          |