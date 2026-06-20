# ProfileContainer

## Example Usage

```typescript
import { ProfileContainer } from "@indiciaosint/sdk/models/operations";

let value: ProfileContainer = {
  maps: {
    photos: [],
    reviews: [
      {
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
      },
      {
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
      },
      {
        "key": "<value>",
        "key1": "<value>",
      },
    ],
    stats: {},
  },
  profile: {
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
    inAppReachability: {
      "key": {
        apps: [
          "<value 1>",
          "<value 2>",
        ],
      },
    },
    names: {
      "key": {
        fullname: "Angelina Barrows",
      },
    },
    personId: "<id>",
    profileInfos: {},
    profilePhotos: {},
    sourceIds: {},
  },
};
```

## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `maps`                                                                           | [operations.Maps](../../models/operations/maps.md)                               | :heavy_check_mark:                                                               | N/A                                                                              |
| `profile`                                                                        | [operations.SearchGmailProfile](../../models/operations/search-gmail-profile.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `calendar`                                                                       | [operations.Calendar](../../models/operations/calendar.md)                       | :heavy_minus_sign:                                                               | N/A                                                                              |
| `playGames`                                                                      | [operations.PlayGames](../../models/operations/play-games.md)                    | :heavy_minus_sign:                                                               | N/A                                                                              |