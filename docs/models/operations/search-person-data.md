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
      alt1DOB: 7450.46,
      alt2DOB: 3453.4,
      alt3DOB: 8099.17,
      city: "North Orionfield",
      countyName: "<value>",
      dob: 3040.8,
      firstname: "Mireille",
      lastname: "Thompson",
      middlename: "Reign",
      nameSuff: "<value>",
      phone1: 7162.41,
      st: "<value>",
      zip: 1504.2,
    },
  ],
  web: [
    {},
  ],
};
```

## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `local`                                                                          | [operations.SearchPersonLocal](../../models/operations/search-person-local.md)[] | :heavy_check_mark:                                                               | N/A                                                                              |
| `web`                                                                            | [operations.SearchPersonWeb](../../models/operations/search-person-web.md)[]     | :heavy_check_mark:                                                               | N/A                                                                              |