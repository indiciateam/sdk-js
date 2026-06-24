# Extraport

## Example Usage

```typescript
import { Extraport } from "@indiciaosint/sdk/models/operations";

let value: Extraport = {
  dollar: {
    state: "Minnesota",
    count: "<value>",
  },
  extrareasons: [
    {
      dollar: {
        reason: "<value>",
        count: "<value>",
        proto: "<value>",
        ports: "<value>",
      },
    },
  ],
};
```

## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `dollar`                                                                  | [operations.ExtraportDollar](../../models/operations/extraport-dollar.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `extrareasons`                                                            | [operations.Extrareason](../../models/operations/extrareason.md)[]        | :heavy_check_mark:                                                        | N/A                                                                       |