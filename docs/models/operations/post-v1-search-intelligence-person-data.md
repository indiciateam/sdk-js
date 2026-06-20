# PostV1SearchIntelligencePersonData

## Example Usage

```typescript
import { PostV1SearchIntelligencePersonData } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligencePersonData = {
  local: [],
  web: [
    {
      aka: [
        "<value 1>",
      ],
      associates: [
        "<value 1>",
        "<value 2>",
        "<value 3>",
      ],
      children: 5516.16,
      currentAddress: "<value>",
      emails: [
        "<value 1>",
        "<value 2>",
      ],
      maritalStatus: "<value>",
      name: "<value>",
      pastAddresses: [],
      phones: [
        "<value 1>",
        "<value 2>",
        "<value 3>",
      ],
    },
  ],
};
```

## Fields

| Field                                                                                                                   | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `local`                                                                                                                 | [operations.PostV1SearchIntelligencePersonLocal](../../models/operations/post-v1-search-intelligence-person-local.md)[] | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `web`                                                                                                                   | [operations.PostV1SearchIntelligencePersonWeb](../../models/operations/post-v1-search-intelligence-person-web.md)[]     | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |