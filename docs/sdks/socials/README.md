# Socials

## Overview

### Available Operations

* [searchDiscord](#searchdiscord) - Discord Search
* [searchGithub](#searchgithub) - GitHub Search
* [searchRoblox](#searchroblox) - Roblox Search
* [searchTiktok](#searchtiktok) - TikTok Search
* [searchUsername](#searchusername) - Username Search V2

## searchDiscord

Search Discord users for profile and server info

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchDiscord" method="post" path="/v1/search/socials/discord" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.socials.searchDiscord({
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
import { socialsSearchDiscord } from "@indiciaosint/sdk/funcs/socials-search-discord.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await socialsSearchDiscord(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("socialsSearchDiscord failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchDiscordRequest](../../models/operations/search-discord-request.md)                                                                                           | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchDiscordResponse](../../models/operations/search-discord-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## searchGithub

Search GitHub profiles, info, and commit emails. Streams progress updates via Server-Sent Events.

### Example Usage: error

<!-- UsageSnippet language="typescript" operationID="searchGithub" method="post" path="/v1/search/socials/github" example="error" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.socials.searchGithub({
    query: "<value>",
  });

  for await (const event of result) {
    console.log(event);
  }
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { socialsSearchGithub } from "@indiciaosint/sdk/funcs/socials-search-github.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await socialsSearchGithub(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    for await (const event of result) {
    console.log(event);
  }
  } else {
    console.log("socialsSearchGithub failed:", res.error);
  }
}

run();
```
### Example Usage: heartbeat

<!-- UsageSnippet language="typescript" operationID="searchGithub" method="post" path="/v1/search/socials/github" example="heartbeat" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.socials.searchGithub({
    query: "<value>",
  });

  for await (const event of result) {
    console.log(event);
  }
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { socialsSearchGithub } from "@indiciaosint/sdk/funcs/socials-search-github.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await socialsSearchGithub(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    for await (const event of result) {
    console.log(event);
  }
  } else {
    console.log("socialsSearchGithub failed:", res.error);
  }
}

run();
```
### Example Usage: result

<!-- UsageSnippet language="typescript" operationID="searchGithub" method="post" path="/v1/search/socials/github" example="result" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.socials.searchGithub({
    query: "<value>",
  });

  for await (const event of result) {
    console.log(event);
  }
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { socialsSearchGithub } from "@indiciaosint/sdk/funcs/socials-search-github.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await socialsSearchGithub(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    for await (const event of result) {
    console.log(event);
  }
  } else {
    console.log("socialsSearchGithub failed:", res.error);
  }
}

run();
```
### Example Usage: status

<!-- UsageSnippet language="typescript" operationID="searchGithub" method="post" path="/v1/search/socials/github" example="status" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.socials.searchGithub({
    query: "<value>",
  });

  for await (const event of result) {
    console.log(event);
  }
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { socialsSearchGithub } from "@indiciaosint/sdk/funcs/socials-search-github.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await socialsSearchGithub(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    for await (const event of result) {
    console.log(event);
  }
  } else {
    console.log("socialsSearchGithub failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchGithubRequest](../../models/operations/search-github-request.md)                                                                                             | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[EventStream<operations.GithubSearchEvent>](../../models/.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 400, 402                   | application/json           |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## searchRoblox

Lookup Roblox users, game statistics, and profile information

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchRoblox" method="post" path="/v1/search/socials/roblox" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.socials.searchRoblox({
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
import { socialsSearchRoblox } from "@indiciaosint/sdk/funcs/socials-search-roblox.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await socialsSearchRoblox(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("socialsSearchRoblox failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchRobloxRequest](../../models/operations/search-roblox-request.md)                                                                                             | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchRobloxResponse](../../models/operations/search-roblox-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## searchTiktok

Aggregate intelligence and data of a TikTok account

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchTiktok" method="post" path="/v1/search/socials/tiktok" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.socials.searchTiktok({
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
import { socialsSearchTiktok } from "@indiciaosint/sdk/funcs/socials-search-tiktok.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await socialsSearchTiktok(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("socialsSearchTiktok failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchTiktokRequest](../../models/operations/search-tiktok-request.md)                                                                                             | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchTiktokResponse](../../models/operations/search-tiktok-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## searchUsername

Search various sites for a specific username. Streams progress updates via Server-Sent Events.

### Example Usage: all

<!-- UsageSnippet language="typescript" operationID="searchUsername" method="post" path="/v2/search/socials/username" example="all" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.socials.searchUsername({
    query: "<value>",
  });

  for await (const event of result) {
    console.log(event);
  }
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { socialsSearchUsername } from "@indiciaosint/sdk/funcs/socials-search-username.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await socialsSearchUsername(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    for await (const event of result) {
    console.log(event);
  }
  } else {
    console.log("socialsSearchUsername failed:", res.error);
  }
}

run();
```
### Example Usage: error

<!-- UsageSnippet language="typescript" operationID="searchUsername" method="post" path="/v2/search/socials/username" example="error" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.socials.searchUsername({
    query: "<value>",
  });

  for await (const event of result) {
    console.log(event);
  }
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { socialsSearchUsername } from "@indiciaosint/sdk/funcs/socials-search-username.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await socialsSearchUsername(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    for await (const event of result) {
    console.log(event);
  }
  } else {
    console.log("socialsSearchUsername failed:", res.error);
  }
}

run();
```
### Example Usage: individual

<!-- UsageSnippet language="typescript" operationID="searchUsername" method="post" path="/v2/search/socials/username" example="individual" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.socials.searchUsername({
    query: "<value>",
  });

  for await (const event of result) {
    console.log(event);
  }
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { socialsSearchUsername } from "@indiciaosint/sdk/funcs/socials-search-username.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await socialsSearchUsername(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    for await (const event of result) {
    console.log(event);
  }
  } else {
    console.log("socialsSearchUsername failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchUsernameRequest](../../models/operations/search-username-request.md)                                                                                         | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[EventStream<operations.UsernameSearchEvent>](../../models/.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 400, 402                   | application/json           |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |