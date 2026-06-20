# SearchPhoneData

## Example Usage

```typescript
import { SearchPhoneData } from "@indiciaosint/sdk/models/operations";

let value: SearchPhoneData = {
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
};
```

## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `local`                                                                        | [operations.SearchPhoneLocal](../../models/operations/search-phone-local.md)[] | :heavy_check_mark:                                                             | N/A                                                                            |
| `phone`                                                                        | [operations.SearchPhonePhone](../../models/operations/search-phone-phone.md)   | :heavy_check_mark:                                                             | N/A                                                                            |
| `web`                                                                          | [operations.SearchPhoneWeb](../../models/operations/search-phone-web.md)[]     | :heavy_check_mark:                                                             | N/A                                                                            |