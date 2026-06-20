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
        alt1DOB: 3161.92,
        alt2DOB: 4250.78,
        alt3DOB: 1359.84,
        city: "Scottsdale",
        countyName: "<value>",
        dob: "1983-10-02",
        firstname: "Charity",
        lastname: "Mueller",
        middlename: "Anderson",
        nameSuff: "<value>",
        phone1: null,
        st: "<value>",
        zip: 9549.72,
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