# Organizations

## Overview

### Available Operations

* [listOrganizations](#listorganizations) - List organizations the authenticated user belongs to.
* [getOrganization](#getorganization) - Get details for a specific organization you are a member of.
* [listOrganizationMembers](#listorganizationmembers) - List members of an organization you belong to.
* [getOrganizationAuditLog](#getorganizationauditlog) - Get the audit log for an organization. Requires owner or admin role.
* [listOrganizationCases](#listorganizationcases) - List cases shared with an organization (filtered by your visibility settings).
* [sendOrganizationCredits](#sendorganizationcredits) - Send credits from your balance to one or more organization members. Requires owner or admin role.

## listOrganizations

List organizations the authenticated user belongs to.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="listOrganizations" method="get" path="/v1/organizations" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.organizations.listOrganizations();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { organizationsListOrganizations } from "@indiciaosint/sdk/funcs/organizations-list-organizations.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await organizationsListOrganizations(indicia);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("organizationsListOrganizations failed:", res.error);
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

**Promise\<[operations.ListOrganizationsResponse](../../models/operations/list-organizations-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## getOrganization

Get details for a specific organization you are a member of.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="getOrganization" method="get" path="/v1/organizations/{id}" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.organizations.getOrganization({
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
import { organizationsGetOrganization } from "@indiciaosint/sdk/funcs/organizations-get-organization.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await organizationsGetOrganization(indicia, {
    id: "<id>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("organizationsGetOrganization failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.GetOrganizationRequest](../../models/operations/get-organization-request.md)                                                                                       | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.GetOrganizationResponse](../../models/operations/get-organization-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## listOrganizationMembers

List members of an organization you belong to.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="listOrganizationMembers" method="get" path="/v1/organizations/{id}/members" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.organizations.listOrganizationMembers({
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
import { organizationsListOrganizationMembers } from "@indiciaosint/sdk/funcs/organizations-list-organization-members.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await organizationsListOrganizationMembers(indicia, {
    id: "<id>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("organizationsListOrganizationMembers failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.ListOrganizationMembersRequest](../../models/operations/list-organization-members-request.md)                                                                      | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ListOrganizationMembersResponse](../../models/operations/list-organization-members-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## getOrganizationAuditLog

Get the audit log for an organization. Requires owner or admin role.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="getOrganizationAuditLog" method="get" path="/v1/organizations/{id}/audit-log" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.organizations.getOrganizationAuditLog({
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
import { organizationsGetOrganizationAuditLog } from "@indiciaosint/sdk/funcs/organizations-get-organization-audit-log.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await organizationsGetOrganizationAuditLog(indicia, {
    id: "<id>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("organizationsGetOrganizationAuditLog failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.GetOrganizationAuditLogRequest](../../models/operations/get-organization-audit-log-request.md)                                                                     | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.GetOrganizationAuditLogResponse](../../models/operations/get-organization-audit-log-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## listOrganizationCases

List cases shared with an organization (filtered by your visibility settings).

### Example Usage

<!-- UsageSnippet language="typescript" operationID="listOrganizationCases" method="get" path="/v1/organizations/{id}/cases" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.organizations.listOrganizationCases({
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
import { organizationsListOrganizationCases } from "@indiciaosint/sdk/funcs/organizations-list-organization-cases.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await organizationsListOrganizationCases(indicia, {
    id: "<id>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("organizationsListOrganizationCases failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.ListOrganizationCasesRequest](../../models/operations/list-organization-cases-request.md)                                                                          | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.ListOrganizationCasesResponse](../../models/operations/list-organization-cases-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |

## sendOrganizationCredits

Send credits from your balance to one or more organization members. Requires owner or admin role.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="sendOrganizationCredits" method="post" path="/v1/organizations/{id}/credits" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.organizations.sendOrganizationCredits({
    id: "<id>",
    body: {
      creditsEach: 590.1,
      recipientMemberIds: [
        "<value 1>",
      ],
    },
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { organizationsSendOrganizationCredits } from "@indiciaosint/sdk/funcs/organizations-send-organization-credits.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const res = await organizationsSendOrganizationCredits(indicia, {
    id: "<id>",
    body: {
      creditsEach: 590.1,
      recipientMemberIds: [
        "<value 1>",
      ],
    },
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("organizationsSendOrganizationCredits failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [operations.SendOrganizationCreditsRequest](../../models/operations/send-organization-credits-request.md)                                                                      | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.SendOrganizationCreditsResponse](../../models/operations/send-organization-credits-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |