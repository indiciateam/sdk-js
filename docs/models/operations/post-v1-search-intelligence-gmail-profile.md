# PostV1SearchIntelligenceGmailProfile

## Example Usage

```typescript
import { PostV1SearchIntelligenceGmailProfile } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligenceGmailProfile = {
  coverPhotos: {},
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
  profileInfos: {
    "key": {
      userTypes: [
        "<value 1>",
        "<value 2>",
      ],
    },
  },
  profilePhotos: {
    "key": {
      flathash: "<value>",
      isDefault: true,
      url: "https://lonely-switch.name",
    },
  },
  sourceIds: {
    "key": {
      lastUpdated: "<value>",
    },
  },
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