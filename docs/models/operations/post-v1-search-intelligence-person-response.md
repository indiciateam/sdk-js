# PostV1SearchIntelligencePersonResponse

Search successful

## Example Usage

```typescript
import { PostV1SearchIntelligencePersonResponse } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligencePersonResponse = {
  data: {
    local: [
      {
        id: 1386.51,
        startDat: null,
        address: "667 Austyn Street",
        aka1fullname: null,
        aka2fullname: null,
        aka3fullname: "<value>",
        alt1dob: "<value>",
        alt2dob: "<value>",
        alt3dob: "<value>",
        city: "Jurupa Valley",
        countyName: "<value>",
        dob: null,
        firstname: "Agustina",
        lastname: "Brakus",
        middlename: "Hayden",
        nameSuff: "<value>",
        phone1: 3565.52,
        st: "<value>",
        zip: 9021.66,
      },
    ],
    web: [],
  },
  success: false,
};
```

## Fields

| Field                                                                                                               | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                              | [operations.PostV1SearchIntelligencePersonData](../../models/operations/post-v1-search-intelligence-person-data.md) | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `success`                                                                                                           | *boolean*                                                                                                           | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `error`                                                                                                             | *string*                                                                                                            | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |