# Users

## Overview

### Available Operations

* [getInfo](#getinfo) - Get information about the user, also healthcheck endpoint.

## getInfo

Get information about the user, also healthcheck endpoint.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="getInfo" method="get" path="/v1/info" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.users.getInfo();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { usersGetInfo } from "@indiciaosint/sdk/funcs/users-get-info.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await usersGetInfo(indicia);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("usersGetInfo failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.GetInfoResponse](../../models/operations/get-info-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |