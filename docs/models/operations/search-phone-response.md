# SearchPhoneResponse

Search successful

## Example Usage

```typescript
import { SearchPhoneResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchPhoneResponse = {
  data: {
    local: [
      {
        id: 659.61,
        startDat: 8361.94,
        address: "6345 Stracke Park",
        aka1fullname: "<value>",
        aka2fullname: "<value>",
        aka3fullname: "<value>",
        alt1dob: "<value>",
        alt2dob: "<value>",
        alt3dob: "<value>",
        city: "South Cielo",
        countyName: "<value>",
        dob: "1950-08-04",
        firstname: "Maxine",
        lastname: "Harvey",
        middlename: null,
        nameSuff: "<value>",
        phone1: 651.65,
        st: "<value>",
        zip: 2835.1,
      },
    ],
    phone: {
      countryCode: "PH",
      nationalFormat: "<value>",
      phoneNumber: "200.728.6446 x9549",
      valid: false,
    },
    web: [
      {
        aka: [
          "<value 1>",
        ],
        associates: [
          "<value 1>",
          "<value 2>",
        ],
        children: 595.39,
        currentAddress: "<value>",
        emails: [
          "<value 1>",
          "<value 2>",
          "<value 3>",
        ],
        maritalStatus: "<value>",
        name: null,
        pastAddresses: [
          "<value 1>",
        ],
        phones: [],
      },
    ],
  },
  success: false,
};
```

## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `data`                                                                     | [operations.SearchPhoneData](../../models/operations/search-phone-data.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `success`                                                                  | *boolean*                                                                  | :heavy_check_mark:                                                         | N/A                                                                        |
| `error`                                                                    | *string*                                                                   | :heavy_minus_sign:                                                         | N/A                                                                        |