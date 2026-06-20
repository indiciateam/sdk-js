# EmployeePasswords

## Example Usage

```typescript
import { EmployeePasswords } from "@indiciaosint/sdk/models/operations";

let value: EmployeePasswords = {
  hasStats: true,
  medium: {
    perc: 3964.44,
    qty: 9743.4,
  },
  strong: {
    perc: 5420.88,
    qty: 5169.34,
  },
  tooWeak: {
    perc: 3015.36,
    qty: 9455.44,
  },
  totalPass: 8626.99,
  weak: {
    perc: 5911.48,
    qty: 1321.17,
  },
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `hasStats`                                                                                    | *boolean*                                                                                     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `medium`                                                                                      | [operations.EmployeePasswordsMedium](../../models/operations/employee-passwords-medium.md)    | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `strong`                                                                                      | [operations.EmployeePasswordsStrong](../../models/operations/employee-passwords-strong.md)    | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `tooWeak`                                                                                     | [operations.EmployeePasswordsTooWeak](../../models/operations/employee-passwords-too-weak.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `totalPass`                                                                                   | *number*                                                                                      | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `weak`                                                                                        | [operations.EmployeePasswordsWeak](../../models/operations/employee-passwords-weak.md)        | :heavy_check_mark:                                                                            | N/A                                                                                           |