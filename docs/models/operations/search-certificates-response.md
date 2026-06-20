# SearchCertificatesResponse

Search successful

## Example Usage

```typescript
import { SearchCertificatesResponse } from "@indiciaosint/sdk/models/operations";

let value: SearchCertificatesResponse = {
  data: [
    {
      commonName: "<value>",
      entryTimestamp: "<value>",
      id: 4005.78,
      issuerCaId: 8116.44,
      issuerName: "<value>",
      nameValue: "<value>",
      notAfter: "<value>",
      notBefore: "<value>",
      serialNumber: "<value>",
    },
  ],
  success: true,
};
```

## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `data`                                                                                     | [operations.SearchCertificatesData](../../models/operations/search-certificates-data.md)[] | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `success`                                                                                  | *boolean*                                                                                  | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `error`                                                                                    | *string*                                                                                   | :heavy_minus_sign:                                                                         | N/A                                                                                        |