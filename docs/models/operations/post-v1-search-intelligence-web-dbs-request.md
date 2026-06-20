# PostV1SearchIntelligenceWebDbsRequest

## Example Usage

```typescript
import { PostV1SearchIntelligenceWebDbsRequest } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligenceWebDbsRequest = {
  query: "<value>",
  services: [
    "snusbase",
  ],
};
```

## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `query`                                                                              | *string*                                                                             | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `services`                                                                           | [operations.Service](../../models/operations/service.md)[]                           | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `cloudsintType`                                                                      | [operations.CloudsintTypeRequest](../../models/operations/cloudsint-type-request.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `intelxType`                                                                         | [operations.IntelxType](../../models/operations/intelx-type.md)                      | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `leakCheckType`                                                                      | [operations.LeakCheckType](../../models/operations/leak-check-type.md)               | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `snusbaseType`                                                                       | [operations.SnusbaseType](../../models/operations/snusbase-type.md)                  | :heavy_minus_sign:                                                                   | N/A                                                                                  |