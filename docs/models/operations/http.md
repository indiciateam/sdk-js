# Http

## Example Usage

```typescript
import { Http } from "@indiciaosint/sdk/models/operations";

let value: Http = {
  components: {
    "key": {},
  },
  favicon: {
    data: "<value>",
    location: "<value>",
  },
  host: "weary-sprinkles.net",
  html: "<value>",
  location: "<value>",
  redirects: [],
  robots: "<value>",
  server: "<value>",
  title: "<value>",
};
```

## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `components`                                                                   | Record<string, [operations.Components](../../models/operations/components.md)> | :heavy_check_mark:                                                             | N/A                                                                            |
| `favicon`                                                                      | [operations.Favicon](../../models/operations/favicon.md)                       | :heavy_check_mark:                                                             | N/A                                                                            |
| `host`                                                                         | *string*                                                                       | :heavy_check_mark:                                                             | N/A                                                                            |
| `html`                                                                         | *string*                                                                       | :heavy_check_mark:                                                             | N/A                                                                            |
| `location`                                                                     | *string*                                                                       | :heavy_check_mark:                                                             | N/A                                                                            |
| `redirects`                                                                    | [operations.Redirect](../../models/operations/redirect.md)[]                   | :heavy_check_mark:                                                             | N/A                                                                            |
| `robots`                                                                       | *string*                                                                       | :heavy_check_mark:                                                             | N/A                                                                            |
| `server`                                                                       | *string*                                                                       | :heavy_check_mark:                                                             | N/A                                                                            |
| `title`                                                                        | *string*                                                                       | :heavy_check_mark:                                                             | N/A                                                                            |