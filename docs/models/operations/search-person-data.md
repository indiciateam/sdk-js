# SearchPersonData

## Example Usage

```typescript
import { SearchPersonData } from "@indiciaosint/sdk/models/operations";

let value: SearchPersonData = {
  local: [
    {
      id: 6101.27,
      startDat: 1276.28,
      address: "52838 Gia Spur",
      aka1fullname: "<value>",
      aka2fullname: "<value>",
      aka3fullname: "<value>",
      alt1dob: "<value>",
      alt2dob: "<value>",
      alt3dob: "<value>",
      city: "Ralphberg",
      countyName: "<value>",
      dob: null,
      firstname: "Orion",
      lastname: "Brakus",
      middlename: "Brooklyn",
      nameSuff: "<value>",
      phone1: 8891.51,
      st: "<value>",
      zip: 7843.18,
    },
  ],
  web: [
    {
      aka: [
        "<value 1>",
        "<value 2>",
        "<value 3>",
      ],
      associates: [
        "<value 1>",
        "<value 2>",
      ],
      children: 8275.78,
      currentAddress: "<value>",
      emails: [
        "<value 1>",
        "<value 2>",
      ],
      maritalStatus: "<value>",
      name: "<value>",
      pastAddresses: [
        "<value 1>",
        "<value 2>",
        "<value 3>",
      ],
      phones: [
        "<value 1>",
        "<value 2>",
      ],
    },
  ],
};
```

## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `local`                                                                          | [operations.SearchPersonLocal](../../models/operations/search-person-local.md)[] | :heavy_check_mark:                                                               | N/A                                                                              |
| `web`                                                                            | [operations.SearchPersonWeb](../../models/operations/search-person-web.md)[]     | :heavy_check_mark:                                                               | N/A                                                                              |