# PostV1SearchIntelligenceAddressResponse

Search for individuals by address.

## Example Usage

```typescript
import { PostV1SearchIntelligenceAddressResponse } from "@indiciaosint/sdk/models/operations";

let value: PostV1SearchIntelligenceAddressResponse = {
  data: {
    local: [
      {
        id: 5372.44,
        startDat: 4485.79,
        address: "7318 Ludwig Via",
        aka1fullname: "<value>",
        aka2fullname: null,
        aka3fullname: "<value>",
        alt1dob: "<value>",
        alt2dob: null,
        alt3dob: "<value>",
        city: "North Estrella",
        countyName: "<value>",
        dob: "1948-05-04",
        firstname: "Cecile",
        lastname: "Gottlieb",
        middlename: "Drew",
        nameSuff: "<value>",
        phone1: 7900.54,
        st: "<value>",
        zip: null,
      },
    ],
    web: [],
  },
  success: true,
};
```

## Fields

| Field                                                                                                                 | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                                | [operations.PostV1SearchIntelligenceAddressData](../../models/operations/post-v1-search-intelligence-address-data.md) | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `success`                                                                                                             | *boolean*                                                                                                             | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |