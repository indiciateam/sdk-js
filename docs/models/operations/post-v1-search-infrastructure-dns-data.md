# PostV1SearchInfrastructureDnsData

## Example Usage

```typescript
import { PostV1SearchInfrastructureDnsData } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchInfrastructureDnsData = {
  host: "alienated-glider.org",
  totalARecs: 7705.99,
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