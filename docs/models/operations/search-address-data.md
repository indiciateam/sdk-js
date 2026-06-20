# SearchAddressData

## Example Usage

```typescript
import { SearchAddressData } from "@indiciaosint/sdk/models/operations";

let value: SearchAddressData = {
  local: [
    {
      id: 1493.85,
      startDat: 1240.57,
      address: "6979 Kemmer Vista",
      aka1fullname: "<value>",
      aka2fullname: "<value>",
      aka3fullname: null,
      alt1dob: "<value>",
      alt2dob: "<value>",
      alt3dob: "<value>",
      city: "East Clovis",
      countyName: "<value>",
      dob: "1963-04-09",
      firstname: "Chaya",
      lastname: "Murray",
      middlename: "Hayden",
      nameSuff: "<value>",
      phone1: 390.7,
      st: "<value>",
      zip: null,
    },
  ],
  web: [],
};
```

## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `local`                                                                            | [operations.SearchAddressLocal](../../models/operations/search-address-local.md)[] | :heavy_check_mark:                                                                 | N/A                                                                                |
| `web`                                                                              | [operations.SearchAddressWeb](../../models/operations/search-address-web.md)[]     | :heavy_check_mark:                                                                 | N/A                                                                                |