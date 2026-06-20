# UserPasswords

## Example Usage

```typescript
import { UserPasswords } from "@indiciaosint/sdk/models/operations";

let value: UserPasswords = {
  hasStats: true,
  medium: {
    perc: 9519.27,
    qty: 9585.4,
  },
  strong: {
    perc: 9411.22,
    qty: 6471.18,
  },
  tooWeak: {
    perc: 4112,
    qty: 2223.23,
  },
  totalPass: 9125.09,
  weak: {
    perc: 420.93,
    qty: 455.03,
  },
};
```

## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `hasStats`                                                                            | *boolean*                                                                             | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `medium`                                                                              | [operations.UserPasswordsMedium](../../models/operations/user-passwords-medium.md)    | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `strong`                                                                              | [operations.UserPasswordsStrong](../../models/operations/user-passwords-strong.md)    | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `tooWeak`                                                                             | [operations.UserPasswordsTooWeak](../../models/operations/user-passwords-too-weak.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `totalPass`                                                                           | *number*                                                                              | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `weak`                                                                                | [operations.UserPasswordsWeak](../../models/operations/user-passwords-weak.md)        | :heavy_check_mark:                                                                    | N/A                                                                                   |