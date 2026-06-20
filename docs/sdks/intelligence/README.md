# Intelligence

## Overview

### Available Operations

* [searchAddress](#searchaddress) - Address Search (US Only)
* [searchEmail](#searchemail) - Email Search (US Only)
* [geolocateMedia](#geolocatemedia) - Geolocate Media
* [searchGmail](#searchgmail) - Gmail Search
* [searchPerson](#searchperson) - Person Search (US Only)
* [searchPhone](#searchphone) - Phone Search (Individual data US only)
* [searchSeon](#searchseon) - SEON Lookup
* [searchWebDatabases](#searchwebdatabases) - Web Databases
* [searchFace](#searchface) - Reverse Face Search
* [searchHudsonRock](#searchhudsonrock) - Hudson Rock Search

## searchAddress

Address Search (US Only)

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchAddress" method="post" path="/v1/search/intelligence/address" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.searchAddress({
    address1: "<value>",
    city: "South Osbaldo",
    state: "Massachusetts",
    zip: "35947-4056",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceSearchAddress } from "@indiciaosint/sdk/funcs/intelligence-search-address.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceSearchAddress(indicia, {
    address1: "<value>",
    city: "South Osbaldo",
    state: "Massachusetts",
    zip: "35947-4056",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceSearchAddress failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchAddressRequest](../../models/operations/search-address-request.md)                                                                                           | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchAddressResponse](../../models/operations/search-address-response.md)\>**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.SearchAddressInternalServerError | 500                                     | application/json                        |
| errors.IndiciaDefaultError              | 4XX, 5XX                                | \*/\*                                   |

## searchEmail

Search for individuals by email address.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchEmail" method="post" path="/v1/search/intelligence/email" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.searchEmail({
    query: "Yasmeen1@hotmail.com",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceSearchEmail } from "@indiciaosint/sdk/funcs/intelligence-search-email.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceSearchEmail(indicia, {
    query: "Yasmeen1@hotmail.com",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceSearchEmail failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchEmailRequest](../../models/operations/search-email-request.md)                                                                                               | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchEmailResponse](../../models/operations/search-email-response.md)\>**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.SearchEmailInternalServerError | 500                                   | application/json                      |
| errors.IndiciaDefaultError            | 4XX, 5XX                              | \*/\*                                 |

## geolocateMedia

Geolocate an image or video using AI-powered analysis. Streams progress updates via Server-Sent Events.

      Response type:
      ```ts
      interface GeolocationResponse {
        location: string | null;
        coordinates: string | null;
        certainty: string;
        reasoning: string;
        mapsUrl?: `https://www.google.com/maps/search/?api=1&query=${string}`;
      }
    ```
      

### Example Usage: analyzing

<!-- UsageSnippet language="typescript" operationID="geolocateMedia" method="post" path="/v1/search/intelligence/geolocation" example="analyzing" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.geolocateMedia({
    media: "<value>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceGeolocateMedia } from "@indiciaosint/sdk/funcs/intelligence-geolocate-media.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceGeolocateMedia(indicia, {
    media: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceGeolocateMedia failed:", res.error);
  }
}

run();
```
### Example Usage: complete

<!-- UsageSnippet language="typescript" operationID="geolocateMedia" method="post" path="/v1/search/intelligence/geolocation" example="complete" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.geolocateMedia({
    media: "<value>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceGeolocateMedia } from "@indiciaosint/sdk/funcs/intelligence-geolocate-media.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceGeolocateMedia(indicia, {
    media: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceGeolocateMedia failed:", res.error);
  }
}

run();
```
### Example Usage: error

<!-- UsageSnippet language="typescript" operationID="geolocateMedia" method="post" path="/v1/search/intelligence/geolocation" example="error" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.geolocateMedia({
    media: "<value>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceGeolocateMedia } from "@indiciaosint/sdk/funcs/intelligence-geolocate-media.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceGeolocateMedia(indicia, {
    media: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceGeolocateMedia failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.GeolocateMediaRequest](../../models/operations/geolocate-media-request.md)                                                                                         | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[string](../../models/.md)\>**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.GeolocateMediaBadRequestError      | 400                                       | application/json                          |
| errors.GeolocateMediaPaymentRequiredError | 402                                       | application/json                          |
| errors.GeolocateMediaInternalServerError  | 500                                       | application/json                          |
| errors.IndiciaDefaultError                | 4XX, 5XX                                  | \*/\*                                     |

## searchGmail

Fetches Gmail account information based on the provided email address using the Ghunt library.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchGmail" method="post" path="/v1/search/intelligence/gmail" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.searchGmail({
    email: "Myrtle35@hotmail.com",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceSearchGmail } from "@indiciaosint/sdk/funcs/intelligence-search-gmail.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceSearchGmail(indicia, {
    email: "Myrtle35@hotmail.com",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceSearchGmail failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchGmailRequest](../../models/operations/search-gmail-request.md)                                                                                               | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchGmailResponse](../../models/operations/search-gmail-response.md)\>**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.SearchGmailInternalServerError | 500                                   | application/json                      |
| errors.IndiciaDefaultError            | 4XX, 5XX                              | \*/\*                                 |

## searchPerson

Search for individuals by name and state.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchPerson" method="post" path="/v1/search/intelligence/person" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.searchPerson({
    name: "<value>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceSearchPerson } from "@indiciaosint/sdk/funcs/intelligence-search-person.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceSearchPerson(indicia, {
    name: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceSearchPerson failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchPersonRequest](../../models/operations/search-person-request.md)                                                                                             | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchPersonResponse](../../models/operations/search-person-response.md)\>**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.SearchPersonInternalServerError | 500                                    | application/json                       |
| errors.IndiciaDefaultError             | 4XX, 5XX                               | \*/\*                                  |

## searchPhone

Search for individuals by phone number.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchPhone" method="post" path="/v1/search/intelligence/phone" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.searchPhone({
    query: "<value>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceSearchPhone } from "@indiciaosint/sdk/funcs/intelligence-search-phone.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceSearchPhone(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceSearchPhone failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchPhoneRequest](../../models/operations/search-phone-request.md)                                                                                               | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchPhoneResponse](../../models/operations/search-phone-response.md)\>**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.SearchPhoneInternalServerError | 500                                   | application/json                      |
| errors.IndiciaDefaultError            | 4XX, 5XX                              | \*/\*                                 |

## searchSeon

Evaluate potential threats with SEON’s counter fraud intelligence systems.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchSeon" method="post" path="/v1/search/intelligence/seon" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.searchSeon({
    query: "<value>",
    type: "email",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceSearchSeon } from "@indiciaosint/sdk/funcs/intelligence-search-seon.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceSearchSeon(indicia, {
    query: "<value>",
    type: "email",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceSearchSeon failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchSeonRequest](../../models/operations/search-seon-request.md)                                                                                                 | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchSeonResponse](../../models/operations/search-seon-response.md)\>**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.SearchSeonInternalServerError | 500                                  | application/json                     |
| errors.IndiciaDefaultError           | 4XX, 5XX                             | \*/\*                                |

## searchWebDatabases

Deep web intelligence gathering and comprehensive data breach analysis

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchWebDatabases" method="post" path="/v1/search/intelligence/web-dbs" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.searchWebDatabases({
    query: "<value>",
    services: [],
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceSearchWebDatabases } from "@indiciaosint/sdk/funcs/intelligence-search-web-databases.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceSearchWebDatabases(indicia, {
    query: "<value>",
    services: [],
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceSearchWebDatabases failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchWebDatabasesRequest](../../models/operations/search-web-databases-request.md)                                                                                | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchWebDatabasesResponse](../../models/operations/search-web-databases-response.md)\>**

### Errors

| Error Type                                    | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| errors.SearchWebDatabasesPaymentRequiredError | 402                                           | application/json                              |
| errors.SearchWebDatabasesInternalServerError  | 500                                           | application/json                              |
| errors.IndiciaDefaultError                    | 4XX, 5XX                                      | \*/\*                                         |

## searchFace

Search for faces across the internet using facial recognition. Streams progress updates via Server-Sent Events.

      Response type:
      ```ts
      interface FacialSearchResult {
        time: number;
        results: {
          id: string;
          hash: string;
          group: number;
          quality: number;
          imageUrl: string;
          crawledAt: number;
          sourceUrl: string;
          thumbnailUrl: string;
        }[];
        searchHash: string;
        numberOfResults: number;
      }
    ```
      

### Example Usage: error

<!-- UsageSnippet language="typescript" operationID="searchFace" method="post" path="/v1/search/intelligence/facial" example="error" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.searchFace({
    media: "<value>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceSearchFace } from "@indiciaosint/sdk/funcs/intelligence-search-face.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceSearchFace(indicia, {
    media: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceSearchFace failed:", res.error);
  }
}

run();
```
### Example Usage: faces

<!-- UsageSnippet language="typescript" operationID="searchFace" method="post" path="/v1/search/intelligence/facial" example="faces" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.searchFace({
    media: "<value>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceSearchFace } from "@indiciaosint/sdk/funcs/intelligence-search-face.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceSearchFace(indicia, {
    media: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceSearchFace failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchFaceRequest](../../models/operations/search-face-request.md)                                                                                                 | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[string](../../models/.md)\>**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.SearchFaceBadRequestError      | 400                                   | application/json                      |
| errors.SearchFacePaymentRequiredError | 402                                   | application/json                      |
| errors.SearchFaceInternalServerError  | 500                                   | application/json                      |
| errors.IndiciaDefaultError            | 4XX, 5XX                              | \*/\*                                 |

## searchHudsonRock

Search for compromised data on Hudson Rock

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchHudsonRock" method="post" path="/v1/search/intelligence/hudsonrock" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.intelligence.searchHudsonRock({
    query: "<value>",
    type: "ip",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { intelligenceSearchHudsonRock } from "@indiciaosint/sdk/funcs/intelligence-search-hudson-rock.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await intelligenceSearchHudsonRock(indicia, {
    query: "<value>",
    type: "ip",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("intelligenceSearchHudsonRock failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchHudsonRockRequest](../../models/operations/search-hudson-rock-request.md)                                                                                    | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchHudsonRockResponse](../../models/operations/search-hudson-rock-response.md)\>**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.SearchHudsonRockInternalServerError | 500                                        | application/json                           |
| errors.IndiciaDefaultError                 | 4XX, 5XX                                   | \*/\*                                      |