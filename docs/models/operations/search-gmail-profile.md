# SearchGmailProfile

## Example Usage

```typescript
import { SearchGmailProfile } from "@indiciaosint/sdk/models/operations";

let value: SearchGmailProfile = {
  coverPhotos: {
    "key": {
      flathash: "<value>",
      isDefault: true,
      url: "https://favorable-pecan.biz/",
    },
  },
  emails: {},
  extendedData: {
    dynamiteData: {
      customerId: "<id>",
      dndState: "<value>",
      entityType: "<value>",
      presence: "<value>",
    },
    gplusData: {
      contentRestriction: "<value>",
      isEntrepriseUser: true,
    },
  },
  inAppReachability: {},
  names: {},
  personId: "<id>",
  profileInfos: {},
  profilePhotos: {},
  sourceIds: {},
};
```

## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `coverPhotos`                                                                                  | Record<string, [operations.CoverPhotos](../../models/operations/cover-photos.md)>              | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `emails`                                                                                       | Record<string, [operations.Emails](../../models/operations/emails.md)>                         | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `extendedData`                                                                                 | [operations.ExtendedData](../../models/operations/extended-data.md)                            | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `inAppReachability`                                                                            | Record<string, [operations.InAppReachability](../../models/operations/in-app-reachability.md)> | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `names`                                                                                        | Record<string, [operations.Names](../../models/operations/names.md)>                           | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `personId`                                                                                     | *string*                                                                                       | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `profileInfos`                                                                                 | Record<string, [operations.ProfileInfos](../../models/operations/profile-infos.md)>            | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `profilePhotos`                                                                                | Record<string, [operations.ProfilePhotos](../../models/operations/profile-photos.md)>          | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `sourceIds`                                                                                    | Record<string, [operations.SourceIds](../../models/operations/source-ids.md)>                  | :heavy_check_mark:                                                                             | N/A                                                                                            |