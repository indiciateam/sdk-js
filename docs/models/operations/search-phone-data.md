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
      alt1DOB: 2045.85,
      alt2DOB: 5355.59,
      alt3DOB: 4846.99,
      city: "Croninland",
      countyName: "<value>",
      dob: 977.8,
      firstname: "Gustave",
      lastname: "Bergnaum",
      middlename: "Bowie",
      nameSuff: "<value>",
      phone1: 7271.61,
      st: null,
      zip: null,
    },
  ],
  phone: {
    countryCode: "AF",
    nationalFormat: "<value>",
    phoneNumber: "486.546.9549 x7725",
    valid: true,
  },
  web: [
    {},
  ],
};
```

## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `local`                                                                        | [operations.SearchPhoneLocal](../../models/operations/search-phone-local.md)[] | :heavy_check_mark:                                                             | N/A                                                                            |
| `phone`                                                                        | [operations.SearchPhonePhone](../../models/operations/search-phone-phone.md)   | :heavy_check_mark:                                                             | N/A                                                                            |
| `web`                                                                          | [operations.SearchPhoneWeb](../../models/operations/search-phone-web.md)[]     | :heavy_check_mark:                                                             | N/A                                                                            |