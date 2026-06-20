# @indiciaosint/sdk

Developer-friendly & type-safe Typescript SDK specifically catered to leverage *@indiciaosint/sdk* API.

[![Built by Speakeasy](https://img.shields.io/badge/Built_by-SPEAKEASY-374151?style=for-the-badge&labelColor=f3f4f6)](https://www.speakeasy.com/?utm_source=@indiciaosint/sdk&utm_campaign=typescript)
[![License: MIT](https://img.shields.io/badge/LICENSE_//_MIT-3b5bdb?style=for-the-badge&labelColor=eff6ff)](https://opensource.org/licenses/MIT)


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/indicia/indicia). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Indicia API: Development documentation
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [@indiciaosint/sdk](#indiciaosintsdk)
  * [SDK Installation](#sdk-installation)
  * [Requirements](#requirements)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Standalone functions](#standalone-functions)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either [npm](https://www.npmjs.com/), [pnpm](https://pnpm.io/), [bun](https://bun.sh/) or [yarn](https://classic.yarnpkg.com/en/) package managers.

### NPM

```bash
npm add @indiciaosint/sdk
```

### PNPM

```bash
pnpm add @indiciaosint/sdk
```

### Bun

```bash
bun add @indiciaosint/sdk
```

### Yarn

```bash
yarn add @indiciaosint/sdk
```

> [!NOTE]
> This package is published as an ES Module (ESM) only. For applications using
> CommonJS, use `await import("@indiciaosint/sdk")` to import and use this package.
<!-- End SDK Installation [installation] -->

<!-- Start Requirements [requirements] -->
## Requirements

For supported JavaScript runtimes, please consult [RUNTIMES.md](RUNTIMES.md).
<!-- End Requirements [requirements] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.getV1Info();

  console.log(result);
}

run();

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name         | Type   | Scheme  | Environment Variable   |
| ------------ | ------ | ------- | ---------------------- |
| `apiKeyAuth` | apiKey | API key | `INDICIA_API_KEY_AUTH` |

To authenticate with the API the `apiKeyAuth` parameter must be set when initializing the SDK client instance. For example:
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.getV1Info();

  console.log(result);
}

run();

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Indicia SDK](docs/sdks/indicia/README.md)

* [getV1Info](docs/sdks/indicia/README.md#getv1info) - Get information about the user, also healthcheck endpoint.
* [getV1Pricing](docs/sdks/indicia/README.md#getv1pricing) - Gives credit pricing for all Indicia services
* [getV1Activity](docs/sdks/indicia/README.md#getv1activity) - Get a list of recent activities.
* [getV1ActivityById](docs/sdks/indicia/README.md#getv1activitybyid) - Get a specific activity by its ID.
* [deleteV1ActivityById](docs/sdks/indicia/README.md#deletev1activitybyid) - Delete a specific activity by its ID.
* [postV1SearchIntelligenceAddress](docs/sdks/indicia/README.md#postv1searchintelligenceaddress) - Address Search (US Only)
* [postV1SearchIntelligenceEmail](docs/sdks/indicia/README.md#postv1searchintelligenceemail) - Email Search (US Only)
* [postV1SearchIntelligenceGeolocation](docs/sdks/indicia/README.md#postv1searchintelligencegeolocation) - Geolocate Media
* [postV1SearchIntelligenceGmail](docs/sdks/indicia/README.md#postv1searchintelligencegmail) - Gmail Search
* [postV1SearchIntelligencePerson](docs/sdks/indicia/README.md#postv1searchintelligenceperson) - Person Search (US Only)
* [postV1SearchIntelligencePhone](docs/sdks/indicia/README.md#postv1searchintelligencephone) - Phone Search (Individual data US only)
* [postV1SearchIntelligenceSeon](docs/sdks/indicia/README.md#postv1searchintelligenceseon) - SEON Lookup
* [postV1SearchIntelligenceWebDbs](docs/sdks/indicia/README.md#postv1searchintelligencewebdbs) - Web Databases
* [postV1SearchIntelligenceFacial](docs/sdks/indicia/README.md#postv1searchintelligencefacial) - Reverse Face Search
* [postV1SearchIntelligenceHudsonrock](docs/sdks/indicia/README.md#postv1searchintelligencehudsonrock) - Hudson Rock Search
* [postV1SearchSocialsDiscord](docs/sdks/indicia/README.md#postv1searchsocialsdiscord) - Discord Search
* [postV1SearchSocialsGithub](docs/sdks/indicia/README.md#postv1searchsocialsgithub) - GitHub Search
* [postV1SearchSocialsRoblox](docs/sdks/indicia/README.md#postv1searchsocialsroblox) - Roblox Search
* [postV1SearchSocialsTiktok](docs/sdks/indicia/README.md#postv1searchsocialstiktok) - TikTok Search
* [postV1SearchInfrastructureIpinfo](docs/sdks/indicia/README.md#postv1searchinfrastructureipinfo) - IP Info
* [postV1SearchInfrastructureDns](docs/sdks/indicia/README.md#postv1searchinfrastructuredns) - DNS Reconnaissance
* [postV1SearchInfrastructureShodan](docs/sdks/indicia/README.md#postv1searchinfrastructureshodan) - Shodan Search
* [postV1SearchInfrastructureWhois](docs/sdks/indicia/README.md#postv1searchinfrastructurewhois) - Whois
* [postV1SearchInfrastructurePortscan](docs/sdks/indicia/README.md#postv1searchinfrastructureportscan) - Port Scan
* [postV1SearchInfrastructureCertificates](docs/sdks/indicia/README.md#postv1searchinfrastructurecertificates) - Certificate Lookup
* [postV1ToolsDoogle](docs/sdks/indicia/README.md#postv1toolsdoogle) - Discord Alt Lookup
* [postV1ToolsDoublecounter](docs/sdks/indicia/README.md#postv1toolsdoublecounter) - Bypass Double Counter URL
* [postV1ToolsIntelx](docs/sdks/indicia/README.md#postv1toolsintelx) - Download IntelX file
* [getV1Organizations](docs/sdks/indicia/README.md#getv1organizations) - List organizations the authenticated user belongs to.
* [getV1OrganizationsById](docs/sdks/indicia/README.md#getv1organizationsbyid) - Get details for a specific organization you are a member of.
* [getV1OrganizationsByIdMembers](docs/sdks/indicia/README.md#getv1organizationsbyidmembers) - List members of an organization you belong to.
* [getV1OrganizationsByIdAuditLog](docs/sdks/indicia/README.md#getv1organizationsbyidauditlog) - Get the audit log for an organization. Requires owner or admin role.
* [getV1OrganizationsByIdCases](docs/sdks/indicia/README.md#getv1organizationsbyidcases) - List cases shared with an organization (filtered by your visibility settings).
* [postV1OrganizationsByIdCredits](docs/sdks/indicia/README.md#postv1organizationsbyidcredits) - Send credits from your balance to one or more organization members. Requires owner or admin role.
* [postV2SearchSocialsUsername](docs/sdks/indicia/README.md#postv2searchsocialsusername) - Username Search V2

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Standalone functions [standalone-funcs] -->
## Standalone functions

All the methods listed above are available as standalone functions. These
functions are ideal for use in applications running in the browser, serverless
runtimes or other environments where application bundle size is a primary
concern. When using a bundler to build your application, all unused
functionality will be either excluded from the final bundle or tree-shaken away.

To read more about standalone functions, check [FUNCTIONS.md](./FUNCTIONS.md).

<details>

<summary>Available standalone functions</summary>

- [`deleteV1ActivityById`](docs/sdks/indicia/README.md#deletev1activitybyid) - Delete a specific activity by its ID.
- [`getV1Activity`](docs/sdks/indicia/README.md#getv1activity) - Get a list of recent activities.
- [`getV1ActivityById`](docs/sdks/indicia/README.md#getv1activitybyid) - Get a specific activity by its ID.
- [`getV1Info`](docs/sdks/indicia/README.md#getv1info) - Get information about the user, also healthcheck endpoint.
- [`getV1Organizations`](docs/sdks/indicia/README.md#getv1organizations) - List organizations the authenticated user belongs to.
- [`getV1OrganizationsById`](docs/sdks/indicia/README.md#getv1organizationsbyid) - Get details for a specific organization you are a member of.
- [`getV1OrganizationsByIdAuditLog`](docs/sdks/indicia/README.md#getv1organizationsbyidauditlog) - Get the audit log for an organization. Requires owner or admin role.
- [`getV1OrganizationsByIdCases`](docs/sdks/indicia/README.md#getv1organizationsbyidcases) - List cases shared with an organization (filtered by your visibility settings).
- [`getV1OrganizationsByIdMembers`](docs/sdks/indicia/README.md#getv1organizationsbyidmembers) - List members of an organization you belong to.
- [`getV1Pricing`](docs/sdks/indicia/README.md#getv1pricing) - Gives credit pricing for all Indicia services
- [`postV1OrganizationsByIdCredits`](docs/sdks/indicia/README.md#postv1organizationsbyidcredits) - Send credits from your balance to one or more organization members. Requires owner or admin role.
- [`postV1SearchInfrastructureCertificates`](docs/sdks/indicia/README.md#postv1searchinfrastructurecertificates) - Certificate Lookup
- [`postV1SearchInfrastructureDns`](docs/sdks/indicia/README.md#postv1searchinfrastructuredns) - DNS Reconnaissance
- [`postV1SearchInfrastructureIpinfo`](docs/sdks/indicia/README.md#postv1searchinfrastructureipinfo) - IP Info
- [`postV1SearchInfrastructurePortscan`](docs/sdks/indicia/README.md#postv1searchinfrastructureportscan) - Port Scan
- [`postV1SearchInfrastructureShodan`](docs/sdks/indicia/README.md#postv1searchinfrastructureshodan) - Shodan Search
- [`postV1SearchInfrastructureWhois`](docs/sdks/indicia/README.md#postv1searchinfrastructurewhois) - Whois
- [`postV1SearchIntelligenceAddress`](docs/sdks/indicia/README.md#postv1searchintelligenceaddress) - Address Search (US Only)
- [`postV1SearchIntelligenceEmail`](docs/sdks/indicia/README.md#postv1searchintelligenceemail) - Email Search (US Only)
- [`postV1SearchIntelligenceFacial`](docs/sdks/indicia/README.md#postv1searchintelligencefacial) - Reverse Face Search
- [`postV1SearchIntelligenceGeolocation`](docs/sdks/indicia/README.md#postv1searchintelligencegeolocation) - Geolocate Media
- [`postV1SearchIntelligenceGmail`](docs/sdks/indicia/README.md#postv1searchintelligencegmail) - Gmail Search
- [`postV1SearchIntelligenceHudsonrock`](docs/sdks/indicia/README.md#postv1searchintelligencehudsonrock) - Hudson Rock Search
- [`postV1SearchIntelligencePerson`](docs/sdks/indicia/README.md#postv1searchintelligenceperson) - Person Search (US Only)
- [`postV1SearchIntelligencePhone`](docs/sdks/indicia/README.md#postv1searchintelligencephone) - Phone Search (Individual data US only)
- [`postV1SearchIntelligenceSeon`](docs/sdks/indicia/README.md#postv1searchintelligenceseon) - SEON Lookup
- [`postV1SearchIntelligenceWebDbs`](docs/sdks/indicia/README.md#postv1searchintelligencewebdbs) - Web Databases
- [`postV1SearchSocialsDiscord`](docs/sdks/indicia/README.md#postv1searchsocialsdiscord) - Discord Search
- [`postV1SearchSocialsGithub`](docs/sdks/indicia/README.md#postv1searchsocialsgithub) - GitHub Search
- [`postV1SearchSocialsRoblox`](docs/sdks/indicia/README.md#postv1searchsocialsroblox) - Roblox Search
- [`postV1SearchSocialsTiktok`](docs/sdks/indicia/README.md#postv1searchsocialstiktok) - TikTok Search
- [`postV1ToolsDoogle`](docs/sdks/indicia/README.md#postv1toolsdoogle) - Discord Alt Lookup
- [`postV1ToolsDoublecounter`](docs/sdks/indicia/README.md#postv1toolsdoublecounter) - Bypass Double Counter URL
- [`postV1ToolsIntelx`](docs/sdks/indicia/README.md#postv1toolsintelx) - Download IntelX file
- [`postV2SearchSocialsUsername`](docs/sdks/indicia/README.md#postv2searchsocialsusername) - Username Search V2

</details>
<!-- End Standalone functions [standalone-funcs] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries.  If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API.  However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a retryConfig object to the call:
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.getV1Info({
    retries: {
      strategy: "backoff",
      backoff: {
        initialInterval: 1,
        maxInterval: 50,
        exponent: 1.1,
        maxElapsedTime: 100,
      },
      retryConnectionErrors: false,
    },
  });

  console.log(result);
}

run();

```

If you'd like to override the default retry strategy for all operations that support retries, you can provide a retryConfig at SDK initialization:
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  retryConfig: {
    strategy: "backoff",
    backoff: {
      initialInterval: 1,
      maxInterval: 50,
      exponent: 1.1,
      maxElapsedTime: 100,
    },
    retryConnectionErrors: false,
  },
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.getV1Info();

  console.log(result);
}

run();

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`IndiciaError`](./src/models/errors/indicia-error.ts) is the base class for all HTTP error responses. It has the following properties:

| Property            | Type       | Description                                                                             |
| ------------------- | ---------- | --------------------------------------------------------------------------------------- |
| `error.message`     | `string`   | Error message                                                                           |
| `error.statusCode`  | `number`   | HTTP response status code eg `404`                                                      |
| `error.headers`     | `Headers`  | HTTP response headers                                                                   |
| `error.body`        | `string`   | HTTP body. Can be empty string if no body is returned.                                  |
| `error.rawResponse` | `Response` | Raw HTTP response                                                                       |
| `error.data$`       |            | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```typescript
import { Indicia } from "@indiciaosint/sdk";
import * as errors from "@indiciaosint/sdk/models/errors";

const indicia = new Indicia({
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  try {
    const result = await indicia.postV1SearchIntelligenceAddress({
      address1: "<value>",
      city: "El Monte",
      state: "New York",
      zip: "85601",
    });

    console.log(result);
  } catch (error) {
    // The base class for HTTP error responses
    if (error instanceof errors.IndiciaError) {
      console.log(error.message);
      console.log(error.statusCode);
      console.log(error.body);
      console.log(error.headers);

      // Depending on the method different errors may be thrown
      if (
        error
          instanceof errors.PostV1SearchIntelligenceAddressInternalServerError
      ) {
        console.log(error.data$.success); // boolean
        console.log(error.data$.error); // string
      }
    }
  }
}

run();

```

### Error Classes
**Primary error:**
* [`IndiciaError`](./src/models/errors/indicia-error.ts): The base class for HTTP error responses.

<details><summary>Less common errors (38)</summary>

<br />

**Network errors:**
* [`ConnectionError`](./src/models/errors/http-client-errors.ts): HTTP client was unable to make a request to a server.
* [`RequestTimeoutError`](./src/models/errors/http-client-errors.ts): HTTP request timed out due to an AbortSignal signal.
* [`RequestAbortedError`](./src/models/errors/http-client-errors.ts): HTTP request was aborted by the client.
* [`InvalidRequestError`](./src/models/errors/http-client-errors.ts): Any input used to create a request is invalid.
* [`UnexpectedClientError`](./src/models/errors/http-client-errors.ts): Unrecognised or unexpected error.


**Inherit from [`IndiciaError`](./src/models/errors/indicia-error.ts)**:
* [`PostV1SearchIntelligenceGeolocationBadRequestError`](./src/models/errors/post-v1-search-intelligence-geolocation-bad-request-error.ts): Bad Request. Status code `400`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligenceFacialBadRequestError`](./src/models/errors/post-v1-search-intelligence-facial-bad-request-error.ts): Bad Request. Status code `400`. Applicable to 1 of 35 methods.*
* [`PostV1SearchInfrastructurePortscanBadRequestError`](./src/models/errors/post-v1-search-infrastructure-portscan-bad-request-error.ts): Bad Request. Status code `400`. Applicable to 1 of 35 methods.*
* [`PostV1ToolsIntelxBadRequestError`](./src/models/errors/post-v1-tools-intelx-bad-request-error.ts): Bad Request. Status code `400`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligenceGeolocationPaymentRequiredError`](./src/models/errors/post-v1-search-intelligence-geolocation-payment-required-error.ts): Payment Required - Insufficient Credits. Status code `402`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligenceWebDbsPaymentRequiredError`](./src/models/errors/post-v1-search-intelligence-web-dbs-payment-required-error.ts): Payment Required. Status code `402`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligenceFacialPaymentRequiredError`](./src/models/errors/post-v1-search-intelligence-facial-payment-required-error.ts): Payment Required - Insufficient Credits. Status code `402`. Applicable to 1 of 35 methods.*
* [`PostV1SearchInfrastructurePortscanPaymentRequiredError`](./src/models/errors/post-v1-search-infrastructure-portscan-payment-required-error.ts): Payment Required - Insufficient Credits. Status code `402`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligenceAddressInternalServerError`](./src/models/errors/post-v1-search-intelligence-address-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligenceEmailInternalServerError`](./src/models/errors/post-v1-search-intelligence-email-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligenceGeolocationInternalServerError`](./src/models/errors/post-v1-search-intelligence-geolocation-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligenceGmailInternalServerError`](./src/models/errors/post-v1-search-intelligence-gmail-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligencePersonInternalServerError`](./src/models/errors/post-v1-search-intelligence-person-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligencePhoneInternalServerError`](./src/models/errors/post-v1-search-intelligence-phone-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligenceSeonInternalServerError`](./src/models/errors/post-v1-search-intelligence-seon-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligenceWebDbsInternalServerError`](./src/models/errors/post-v1-search-intelligence-web-dbs-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligenceFacialInternalServerError`](./src/models/errors/post-v1-search-intelligence-facial-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchIntelligenceHudsonrockInternalServerError`](./src/models/errors/post-v1-search-intelligence-hudsonrock-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchSocialsDiscordInternalServerError`](./src/models/errors/post-v1-search-socials-discord-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchSocialsGithubInternalServerError`](./src/models/errors/post-v1-search-socials-github-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchSocialsRobloxInternalServerError`](./src/models/errors/post-v1-search-socials-roblox-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchSocialsTiktokInternalServerError`](./src/models/errors/post-v1-search-socials-tiktok-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchInfrastructureIpinfoInternalServerError`](./src/models/errors/post-v1-search-infrastructure-ipinfo-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchInfrastructureDnsInternalServerError`](./src/models/errors/post-v1-search-infrastructure-dns-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchInfrastructureShodanInternalServerError`](./src/models/errors/post-v1-search-infrastructure-shodan-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchInfrastructureWhoisInternalServerError`](./src/models/errors/post-v1-search-infrastructure-whois-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchInfrastructurePortscanInternalServerError`](./src/models/errors/post-v1-search-infrastructure-portscan-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1SearchInfrastructureCertificatesInternalServerError`](./src/models/errors/post-v1-search-infrastructure-certificates-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1ToolsDoogleInternalServerError`](./src/models/errors/post-v1-tools-doogle-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1ToolsDoublecounterInternalServerError`](./src/models/errors/post-v1-tools-doublecounter-internal-server-error.ts): Bypass failed. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV1ToolsIntelxInternalServerError`](./src/models/errors/post-v1-tools-intelx-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`PostV2SearchSocialsUsernameInternalServerError`](./src/models/errors/post-v2-search-socials-username-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`ResponseValidationError`](./src/models/errors/response-validation-error.ts): Type mismatch between the data returned from the server and the structure expected by the SDK. See `error.rawValue` for the raw value and `error.pretty()` for a nicely formatted multi-line string.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `serverURL: string` optional parameter when initializing the SDK client instance. For example:
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  serverURL: "https://api.indicia.app",
  apiKeyAuth: process.env["INDICIA_API_KEY_AUTH"] ?? "",
});

async function run() {
  const result = await indicia.getV1Info();

  console.log(result);
}

run();

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The TypeScript SDK makes API calls using an `HTTPClient` that wraps the native
[Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). This
client is a thin wrapper around `fetch` and provides the ability to attach hooks
around the request lifecycle that can be used to modify the request or handle
errors and response.

The `HTTPClient` constructor takes an optional `fetcher` argument that can be
used to integrate a third-party HTTP client or when writing tests to mock out
the HTTP client and feed in fixtures.

The following example shows how to:
- route requests through a proxy server using [undici](https://www.npmjs.com/package/undici)'s ProxyAgent
- use the `"beforeRequest"` hook to add a custom header and a timeout to requests
- use the `"requestError"` hook to log errors

```typescript
import { Indicia } from "@indiciaosint/sdk";
import { ProxyAgent } from "undici";
import { HTTPClient } from "@indiciaosint/sdk/lib/http";

const dispatcher = new ProxyAgent("http://proxy.example.com:8080");

const httpClient = new HTTPClient({
  // 'fetcher' takes a function that has the same signature as native 'fetch'.
  fetcher: (input, init) =>
    // 'dispatcher' is specific to undici and not part of the standard Fetch API.
    fetch(input, { ...init, dispatcher } as RequestInit),
});

httpClient.addHook("beforeRequest", (request) => {
  const nextRequest = new Request(request, {
    signal: request.signal || AbortSignal.timeout(5000)
  });

  nextRequest.headers.set("x-custom-header", "custom value");

  return nextRequest;
});

httpClient.addHook("requestError", (error, request) => {
  console.group("Request Error");
  console.log("Reason:", `${error}`);
  console.log("Endpoint:", `${request.method} ${request.url}`);
  console.groupEnd();
});

const sdk = new Indicia({ httpClient: httpClient });
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass a logger that matches `console`'s interface as an SDK option.

> [!WARNING]
> Beware that debug logging will reveal secrets, like API tokens in headers, in log messages printed to a console or files. It's recommended to use this feature only during local development and not in production.

```typescript
import { Indicia } from "@indiciaosint/sdk";

const sdk = new Indicia({ debugLogger: console });
```

You can also enable a default debug logger by setting an environment variable `INDICIA_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=@indiciaosint/sdk&utm_campaign=typescript)
