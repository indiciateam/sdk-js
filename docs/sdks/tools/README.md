# Tools

## Overview

### Available Operations

* [searchAppStore](#searchappstore) - App Store Search
* [lookupDiscordAlt](#lookupdiscordalt) - Discord Alt Lookup
* [bypassDoubleCounter](#bypassdoublecounter) - Bypass Double Counter URL
* [downloadIntelxFile](#downloadintelxfile) - Download IntelX file
* [downloadVirusTotalFile](#downloadvirustotalfile) - Download VirusTotal file

## searchAppStore

Scrape app and developer information from the Google Play Store or Apple App Store. Pass an app/package ID (e.g. com.whatsapp) for full developer contact details, or a name to search.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchAppStore" method="post" path="/v1/tools/appstore" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.tools.searchAppStore({
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
import { toolsSearchAppStore } from "@indiciaosint/sdk/funcs/tools-search-app-store.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await toolsSearchAppStore(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("toolsSearchAppStore failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchAppStoreRequest](../../models/operations/search-app-store-request.md)                                                                                        | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchAppStoreResponse](../../models/operations/search-app-store-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## lookupDiscordAlt

Correlate and identify alternative Discord accounts of a user.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="lookupDiscordAlt" method="post" path="/v1/tools/doogle" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.tools.lookupDiscordAlt({
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
import { toolsLookupDiscordAlt } from "@indiciaosint/sdk/funcs/tools-lookup-discord-alt.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await toolsLookupDiscordAlt(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("toolsLookupDiscordAlt failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.LookupDiscordAltRequest](../../models/operations/lookup-discord-alt-request.md)                                                                                    | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.LookupDiscordAltResponse](../../models/operations/lookup-discord-alt-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## bypassDoubleCounter

Bypass alt detection for Discord servers.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="bypassDoubleCounter" method="post" path="/v1/tools/doublecounter" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.tools.bypassDoubleCounter({
    url: "https://wavy-lay.info/",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { toolsBypassDoubleCounter } from "@indiciaosint/sdk/funcs/tools-bypass-double-counter.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await toolsBypassDoubleCounter(indicia, {
    url: "https://wavy-lay.info/",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("toolsBypassDoubleCounter failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.BypassDoubleCounterRequest](../../models/operations/bypass-double-counter-request.md)                                                                              | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.BypassDoubleCounterResponse](../../models/operations/bypass-double-counter-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## downloadIntelxFile

Download a file from IntelX storage. Use storageId + bucket for a standalone file (5 credits), or systemId with bucket "leaks.logs" for a stealer log (10 credits).

### Example Usage

<!-- UsageSnippet language="typescript" operationID="downloadIntelxFile" method="post" path="/v1/tools/intelx" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.tools.downloadIntelxFile({
    bucket: "leaks.logs",
    systemId: "<id>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { toolsDownloadIntelxFile } from "@indiciaosint/sdk/funcs/tools-download-intelx-file.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await toolsDownloadIntelxFile(indicia, {
    bucket: "leaks.logs",
    systemId: "<id>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("toolsDownloadIntelxFile failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.DownloadIntelxFileRequest](../../models/operations/download-intelx-file-request.md)                                                                                | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.DownloadIntelxFileResponse](../../models/operations/download-intelx-file-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 400                        | application/json           |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## downloadVirusTotalFile

Download a file from VirusTotal by its id. The file is returned base64-encoded.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="downloadVirusTotalFile" method="post" path="/v1/tools/virustotal" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.tools.downloadVirusTotalFile({
    id: "<id>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { toolsDownloadVirusTotalFile } from "@indiciaosint/sdk/funcs/tools-download-virus-total-file.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await toolsDownloadVirusTotalFile(indicia, {
    id: "<id>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("toolsDownloadVirusTotalFile failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.DownloadVirusTotalFileRequest](../../models/operations/download-virus-total-file-request.md)                                                                       | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.DownloadVirusTotalFileResponse](../../models/operations/download-virus-total-file-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 402                        | application/json           |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |