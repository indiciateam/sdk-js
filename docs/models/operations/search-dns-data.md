# SearchDnsData

## Example Usage

```typescript
import { SearchDnsData } from "@indiciaosint/sdk/models/operations";

let value: SearchDnsData = {
  host: "joyful-ownership.info",
  totalARecs: 4404.94,
};
```

## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `host`                                                 | *string*                                               | :heavy_check_mark:                                     | N/A                                                    |
| `totalARecs`                                           | *number*                                               | :heavy_check_mark:                                     | N/A                                                    |
| `a`                                                    | [operations.A](../../models/operations/a.md)[]         | :heavy_minus_sign:                                     | N/A                                                    |
| `cname`                                                | [operations.Cname](../../models/operations/cname.md)[] | :heavy_minus_sign:                                     | N/A                                                    |
| `error`                                                | *string*                                               | :heavy_minus_sign:                                     | N/A                                                    |
| `mx`                                                   | [operations.Mx](../../models/operations/mx.md)[]       | :heavy_minus_sign:                                     | N/A                                                    |
| `ns`                                                   | [operations.N](../../models/operations/n.md)[]         | :heavy_minus_sign:                                     | N/A                                                    |
| `txt`                                                  | *string*[]                                             | :heavy_minus_sign:                                     | N/A                                                    |