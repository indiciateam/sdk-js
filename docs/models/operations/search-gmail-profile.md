# SearchGmailProfile

## Example Usage

```typescript
import { SearchGmailProfile } from "@indiciaosint/sdk/models/operations";

let value: SearchGmailProfile = {
  emails: {
    "key": {
      value: "<value>",
    },
  },
  personId: "<id>",
  sourceIds: {},
};
```

## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `emails`                                                            | Record<string, *operations.EmailsUnion*>                            | :heavy_check_mark:                                                  | N/A                                                                 |
| `personId`                                                          | *string*                                                            | :heavy_check_mark:                                                  | N/A                                                                 |
| `sourceIds`                                                         | Record<string, *operations.SourceIdsUnion*>                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `coverPhotos`                                                       | Record<string, *operations.CoverPhotosUnion*>                       | :heavy_minus_sign:                                                  | N/A                                                                 |
| `extendedData`                                                      | [operations.ExtendedData](../../models/operations/extended-data.md) | :heavy_minus_sign:                                                  | N/A                                                                 |
| `inAppReachability`                                                 | Record<string, *operations.InAppReachabilityUnion*>                 | :heavy_minus_sign:                                                  | N/A                                                                 |
| `names`                                                             | Record<string, *operations.NamesUnion*>                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `profileInfos`                                                      | Record<string, *operations.ProfileInfosUnion*>                      | :heavy_minus_sign:                                                  | N/A                                                                 |
| `profilePhotos`                                                     | Record<string, *operations.ProfilePhotosUnion*>                     | :heavy_minus_sign:                                                  | N/A                                                                 |