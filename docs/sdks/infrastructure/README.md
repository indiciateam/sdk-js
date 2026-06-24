# Infrastructure

## Overview

### Available Operations

* [searchIpInfo](#searchipinfo) - IP Info
* [searchDns](#searchdns) - DNS Reconnaissance
* [searchShodan](#searchshodan) - Shodan Search
* [searchWhois](#searchwhois) - Whois
* [scanPorts](#scanports) - Port Scan
* [searchCertificates](#searchcertificates) - Certificate Lookup

## searchIpInfo

Analyze details of an IP Address.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchIpInfo" method="post" path="/v1/search/infrastructure/ipinfo" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.infrastructure.searchIpInfo({
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
import { infrastructureSearchIpInfo } from "@indiciaosint/sdk/funcs/infrastructure-search-ip-info.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await infrastructureSearchIpInfo(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("infrastructureSearchIpInfo failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchIpInfoRequest](../../models/operations/search-ip-info-request.md)                                                                                            | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchIpInfoResponse](../../models/operations/search-ip-info-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## searchDns

Perform deep DNS analysis and find hidden subdomains

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchDns" method="post" path="/v1/search/infrastructure/dns" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.infrastructure.searchDns({
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
import { infrastructureSearchDns } from "@indiciaosint/sdk/funcs/infrastructure-search-dns.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await infrastructureSearchDns(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("infrastructureSearchDns failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchDnsRequest](../../models/operations/search-dns-request.md)                                                                                                   | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchDnsResponse](../../models/operations/search-dns-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## searchShodan

IP service and software intelligence

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchShodan" method="post" path="/v1/search/infrastructure/shodan" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.infrastructure.searchShodan({
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
import { infrastructureSearchShodan } from "@indiciaosint/sdk/funcs/infrastructure-search-shodan.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await infrastructureSearchShodan(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("infrastructureSearchShodan failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchShodanRequest](../../models/operations/search-shodan-request.md)                                                                                             | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchShodanResponse](../../models/operations/search-shodan-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## searchWhois

Return information on a domain and its registration

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchWhois" method="post" path="/v1/search/infrastructure/whois" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.infrastructure.searchWhois({
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
import { infrastructureSearchWhois } from "@indiciaosint/sdk/funcs/infrastructure-search-whois.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await infrastructureSearchWhois(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("infrastructureSearchWhois failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchWhoisRequest](../../models/operations/search-whois-request.md)                                                                                               | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchWhoisResponse](../../models/operations/search-whois-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## scanPorts

Perform a port scan on a given IP address or domain.

### Example Usage: analyzing

<!-- UsageSnippet language="typescript" operationID="scanPorts" method="post" path="/v1/search/infrastructure/portscan" example="analyzing" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.infrastructure.scanPorts({
    host: "unconscious-elevator.info",
    options: {},
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
import { infrastructureScanPorts } from "@indiciaosint/sdk/funcs/infrastructure-scan-ports.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await infrastructureScanPorts(indicia, {
    host: "unconscious-elevator.info",
    options: {},
  });
  if (res.ok) {
    const { value: result } = res;
    for await (const event of result) {
    console.log(event);
  }
  } else {
    console.log("infrastructureScanPorts failed:", res.error);
  }
}

run();
```
### Example Usage: complete

<!-- UsageSnippet language="typescript" operationID="scanPorts" method="post" path="/v1/search/infrastructure/portscan" example="complete" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.infrastructure.scanPorts({
    host: "unconscious-elevator.info",
    options: {},
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
import { infrastructureScanPorts } from "@indiciaosint/sdk/funcs/infrastructure-scan-ports.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await infrastructureScanPorts(indicia, {
    host: "unconscious-elevator.info",
    options: {},
  });
  if (res.ok) {
    const { value: result } = res;
    for await (const event of result) {
    console.log(event);
  }
  } else {
    console.log("infrastructureScanPorts failed:", res.error);
  }
}

run();
```
### Example Usage: error

<!-- UsageSnippet language="typescript" operationID="scanPorts" method="post" path="/v1/search/infrastructure/portscan" example="error" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.infrastructure.scanPorts({
    host: "unconscious-elevator.info",
    options: {},
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
import { infrastructureScanPorts } from "@indiciaosint/sdk/funcs/infrastructure-scan-ports.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await infrastructureScanPorts(indicia, {
    host: "unconscious-elevator.info",
    options: {},
  });
  if (res.ok) {
    const { value: result } = res;
    for await (const event of result) {
    console.log(event);
  }
  } else {
    console.log("infrastructureScanPorts failed:", res.error);
  }
}

run();
```
### Example Usage: progress

<!-- UsageSnippet language="typescript" operationID="scanPorts" method="post" path="/v1/search/infrastructure/portscan" example="progress" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.infrastructure.scanPorts({
    host: "unconscious-elevator.info",
    options: {},
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
import { infrastructureScanPorts } from "@indiciaosint/sdk/funcs/infrastructure-scan-ports.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await infrastructureScanPorts(indicia, {
    host: "unconscious-elevator.info",
    options: {},
  });
  if (res.ok) {
    const { value: result } = res;
    for await (const event of result) {
    console.log(event);
  }
  } else {
    console.log("infrastructureScanPorts failed:", res.error);
  }
}

run();
```
### Example Usage: scanning

<!-- UsageSnippet language="typescript" operationID="scanPorts" method="post" path="/v1/search/infrastructure/portscan" example="scanning" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.infrastructure.scanPorts({
    host: "unconscious-elevator.info",
    options: {},
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
import { infrastructureScanPorts } from "@indiciaosint/sdk/funcs/infrastructure-scan-ports.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await infrastructureScanPorts(indicia, {
    host: "unconscious-elevator.info",
    options: {},
  });
  if (res.ok) {
    const { value: result } = res;
    for await (const event of result) {
    console.log(event);
  }
  } else {
    console.log("infrastructureScanPorts failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.ScanPortsRequest](../../models/operations/scan-ports-request.md)                                                                                                   | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[EventStream<operations.PortscanEvent>](../../models/.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 400, 402                   | application/json           |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## searchCertificates

Lookup details about a TLS certificate by domain.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="searchCertificates" method="post" path="/v1/search/infrastructure/certificates" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.infrastructure.searchCertificates({
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
import { infrastructureSearchCertificates } from "@indiciaosint/sdk/funcs/infrastructure-search-certificates.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await infrastructureSearchCertificates(indicia, {
    query: "<value>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("infrastructureSearchCertificates failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SearchCertificatesRequest](../../models/operations/search-certificates-request.md)                                                                                 | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SearchCertificatesResponse](../../models/operations/search-certificates-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.FailedResponseError | 500                        | application/json           |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |