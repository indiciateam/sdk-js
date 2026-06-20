# SearchAddressResponse

Search for individuals by address.

## Example Usage

```typescript
import { SearchAddressResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchAddressResponse = {
  data: {
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
  },
  success: false,
};
```

## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `data`                                                                         | [operations.SearchAddressData](../../models/operations/search-address-data.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `success`                                                                      | *boolean*                                                                      | :heavy_check_mark:                                                             | N/A                                                                            |