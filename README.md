<h3>
    <img src="https://indicia.app/branding/wordmark.png" alt="indicia wordmark" width="300">
    <br />
</h3>

# @indiciaosint/sdk

Developer-friendly & type-safe Typescript SDK for the Indicia API. 

[![Built by Speakeasy](https://img.shields.io/badge/Built_by-SPEAKEASY-374151?style=for-the-badge&labelColor=f3f4f6)](https://www.speakeasy.com/?utm_source=@indiciaosint/sdk&utm_campaign=typescript)


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
  const result = await indicia.users.getInfo();

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
  const result = await indicia.users.getInfo();

  console.log(result);
}

run();

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Activity](docs/sdks/activity/README.md)

* [listActivities](docs/sdks/activity/README.md#listactivities) - Get a list of recent activities.
* [getActivity](docs/sdks/activity/README.md#getactivity) - Get a specific activity by its ID.
* [deleteActivity](docs/sdks/activity/README.md#deleteactivity) - Delete a specific activity by its ID.

### [Infrastructure](docs/sdks/infrastructure/README.md)

* [searchIpInfo](docs/sdks/infrastructure/README.md#searchipinfo) - IP Info
* [searchDns](docs/sdks/infrastructure/README.md#searchdns) - DNS Reconnaissance
* [searchShodan](docs/sdks/infrastructure/README.md#searchshodan) - Shodan Search
* [searchWhois](docs/sdks/infrastructure/README.md#searchwhois) - Whois
* [scanPorts](docs/sdks/infrastructure/README.md#scanports) - Port Scan
* [searchCertificates](docs/sdks/infrastructure/README.md#searchcertificates) - Certificate Lookup

### [Intelligence](docs/sdks/intelligence/README.md)

* [searchAddress](docs/sdks/intelligence/README.md#searchaddress) - Address Search (US Only)
* [searchEmail](docs/sdks/intelligence/README.md#searchemail) - Email Search (US Only)
* [geolocateMedia](docs/sdks/intelligence/README.md#geolocatemedia) - Geolocate Media
* [searchGmail](docs/sdks/intelligence/README.md#searchgmail) - Gmail Search
* [searchPerson](docs/sdks/intelligence/README.md#searchperson) - Person Search (US Only)
* [searchPhone](docs/sdks/intelligence/README.md#searchphone) - Phone Search (Individual data US only)
* [searchSeon](docs/sdks/intelligence/README.md#searchseon) - SEON Lookup
* [searchWebDatabases](docs/sdks/intelligence/README.md#searchwebdatabases) - Web Databases
* [searchFace](docs/sdks/intelligence/README.md#searchface) - Reverse Face Search
* [searchHudsonRock](docs/sdks/intelligence/README.md#searchhudsonrock) - Hudson Rock Search

### [Organizations](docs/sdks/organizations/README.md)

* [listOrganizations](docs/sdks/organizations/README.md#listorganizations) - List organizations the authenticated user belongs to.
* [getOrganization](docs/sdks/organizations/README.md#getorganization) - Get details for a specific organization you are a member of.
* [listOrganizationMembers](docs/sdks/organizations/README.md#listorganizationmembers) - List members of an organization you belong to.
* [getOrganizationAuditLog](docs/sdks/organizations/README.md#getorganizationauditlog) - Get the audit log for an organization. Requires owner or admin role.
* [listOrganizationCases](docs/sdks/organizations/README.md#listorganizationcases) - List cases shared with an organization (filtered by your visibility settings).
* [sendOrganizationCredits](docs/sdks/organizations/README.md#sendorganizationcredits) - Send credits from your balance to one or more organization members. Requires owner or admin role.

### [Pricing](docs/sdks/pricing/README.md)

* [getPricing](docs/sdks/pricing/README.md#getpricing) - Gives credit pricing for all Indicia services

### [Socials](docs/sdks/socials/README.md)

* [searchDiscord](docs/sdks/socials/README.md#searchdiscord) - Discord Search
* [searchGithub](docs/sdks/socials/README.md#searchgithub) - GitHub Search
* [searchRoblox](docs/sdks/socials/README.md#searchroblox) - Roblox Search
* [searchTiktok](docs/sdks/socials/README.md#searchtiktok) - TikTok Search
* [searchUsername](docs/sdks/socials/README.md#searchusername) - Username Search V2

### [Tools](docs/sdks/tools/README.md)

* [lookupDiscordAlt](docs/sdks/tools/README.md#lookupdiscordalt) - Discord Alt Lookup
* [bypassDoubleCounter](docs/sdks/tools/README.md#bypassdoublecounter) - Bypass Double Counter URL
* [downloadIntelxFile](docs/sdks/tools/README.md#downloadintelxfile) - Download IntelX file

### [Users](docs/sdks/users/README.md)

* [getInfo](docs/sdks/users/README.md#getinfo) - Get information about the user, also healthcheck endpoint.

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

- [`activityDeleteActivity`](docs/sdks/activity/README.md#deleteactivity) - Delete a specific activity by its ID.
- [`activityGetActivity`](docs/sdks/activity/README.md#getactivity) - Get a specific activity by its ID.
- [`activityListActivities`](docs/sdks/activity/README.md#listactivities) - Get a list of recent activities.
- [`infrastructureScanPorts`](docs/sdks/infrastructure/README.md#scanports) - Port Scan
- [`infrastructureSearchCertificates`](docs/sdks/infrastructure/README.md#searchcertificates) - Certificate Lookup
- [`infrastructureSearchDns`](docs/sdks/infrastructure/README.md#searchdns) - DNS Reconnaissance
- [`infrastructureSearchIpInfo`](docs/sdks/infrastructure/README.md#searchipinfo) - IP Info
- [`infrastructureSearchShodan`](docs/sdks/infrastructure/README.md#searchshodan) - Shodan Search
- [`infrastructureSearchWhois`](docs/sdks/infrastructure/README.md#searchwhois) - Whois
- [`intelligenceGeolocateMedia`](docs/sdks/intelligence/README.md#geolocatemedia) - Geolocate Media
- [`intelligenceSearchAddress`](docs/sdks/intelligence/README.md#searchaddress) - Address Search (US Only)
- [`intelligenceSearchEmail`](docs/sdks/intelligence/README.md#searchemail) - Email Search (US Only)
- [`intelligenceSearchFace`](docs/sdks/intelligence/README.md#searchface) - Reverse Face Search
- [`intelligenceSearchGmail`](docs/sdks/intelligence/README.md#searchgmail) - Gmail Search
- [`intelligenceSearchHudsonRock`](docs/sdks/intelligence/README.md#searchhudsonrock) - Hudson Rock Search
- [`intelligenceSearchPerson`](docs/sdks/intelligence/README.md#searchperson) - Person Search (US Only)
- [`intelligenceSearchPhone`](docs/sdks/intelligence/README.md#searchphone) - Phone Search (Individual data US only)
- [`intelligenceSearchSeon`](docs/sdks/intelligence/README.md#searchseon) - SEON Lookup
- [`intelligenceSearchWebDatabases`](docs/sdks/intelligence/README.md#searchwebdatabases) - Web Databases
- [`organizationsGetOrganization`](docs/sdks/organizations/README.md#getorganization) - Get details for a specific organization you are a member of.
- [`organizationsGetOrganizationAuditLog`](docs/sdks/organizations/README.md#getorganizationauditlog) - Get the audit log for an organization. Requires owner or admin role.
- [`organizationsListOrganizationCases`](docs/sdks/organizations/README.md#listorganizationcases) - List cases shared with an organization (filtered by your visibility settings).
- [`organizationsListOrganizationMembers`](docs/sdks/organizations/README.md#listorganizationmembers) - List members of an organization you belong to.
- [`organizationsListOrganizations`](docs/sdks/organizations/README.md#listorganizations) - List organizations the authenticated user belongs to.
- [`organizationsSendOrganizationCredits`](docs/sdks/organizations/README.md#sendorganizationcredits) - Send credits from your balance to one or more organization members. Requires owner or admin role.
- [`pricingGetPricing`](docs/sdks/pricing/README.md#getpricing) - Gives credit pricing for all Indicia services
- [`socialsSearchDiscord`](docs/sdks/socials/README.md#searchdiscord) - Discord Search
- [`socialsSearchGithub`](docs/sdks/socials/README.md#searchgithub) - GitHub Search
- [`socialsSearchRoblox`](docs/sdks/socials/README.md#searchroblox) - Roblox Search
- [`socialsSearchTiktok`](docs/sdks/socials/README.md#searchtiktok) - TikTok Search
- [`socialsSearchUsername`](docs/sdks/socials/README.md#searchusername) - Username Search V2
- [`toolsBypassDoubleCounter`](docs/sdks/tools/README.md#bypassdoublecounter) - Bypass Double Counter URL
- [`toolsDownloadIntelxFile`](docs/sdks/tools/README.md#downloadintelxfile) - Download IntelX file
- [`toolsLookupDiscordAlt`](docs/sdks/tools/README.md#lookupdiscordalt) - Discord Alt Lookup
- [`usersGetInfo`](docs/sdks/users/README.md#getinfo) - Get information about the user, also healthcheck endpoint.

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
  const result = await indicia.users.getInfo({
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
  const result = await indicia.users.getInfo();

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
    const result = await indicia.intelligence.searchAddress({
      address1: "<value>",
      city: "South Osbaldo",
      state: "Massachusetts",
      zip: "35947-4056",
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
      if (error instanceof errors.SearchAddressInternalServerError) {
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
* [`GeolocateMediaBadRequestError`](./src/models/errors/geolocate-media-bad-request-error.ts): Bad Request. Status code `400`. Applicable to 1 of 35 methods.*
* [`SearchFaceBadRequestError`](./src/models/errors/search-face-bad-request-error.ts): Bad Request. Status code `400`. Applicable to 1 of 35 methods.*
* [`ScanPortsBadRequestError`](./src/models/errors/scan-ports-bad-request-error.ts): Bad Request. Status code `400`. Applicable to 1 of 35 methods.*
* [`DownloadIntelxFileBadRequestError`](./src/models/errors/download-intelx-file-bad-request-error.ts): Bad Request. Status code `400`. Applicable to 1 of 35 methods.*
* [`GeolocateMediaPaymentRequiredError`](./src/models/errors/geolocate-media-payment-required-error.ts): Payment Required - Insufficient Credits. Status code `402`. Applicable to 1 of 35 methods.*
* [`SearchWebDatabasesPaymentRequiredError`](./src/models/errors/search-web-databases-payment-required-error.ts): Payment Required. Status code `402`. Applicable to 1 of 35 methods.*
* [`SearchFacePaymentRequiredError`](./src/models/errors/search-face-payment-required-error.ts): Payment Required - Insufficient Credits. Status code `402`. Applicable to 1 of 35 methods.*
* [`ScanPortsPaymentRequiredError`](./src/models/errors/scan-ports-payment-required-error.ts): Payment Required - Insufficient Credits. Status code `402`. Applicable to 1 of 35 methods.*
* [`SearchAddressInternalServerError`](./src/models/errors/search-address-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchEmailInternalServerError`](./src/models/errors/search-email-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`GeolocateMediaInternalServerError`](./src/models/errors/geolocate-media-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchGmailInternalServerError`](./src/models/errors/search-gmail-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchPersonInternalServerError`](./src/models/errors/search-person-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchPhoneInternalServerError`](./src/models/errors/search-phone-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchSeonInternalServerError`](./src/models/errors/search-seon-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchWebDatabasesInternalServerError`](./src/models/errors/search-web-databases-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchFaceInternalServerError`](./src/models/errors/search-face-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchHudsonRockInternalServerError`](./src/models/errors/search-hudson-rock-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchDiscordInternalServerError`](./src/models/errors/search-discord-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchGithubInternalServerError`](./src/models/errors/search-github-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchRobloxInternalServerError`](./src/models/errors/search-roblox-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchTiktokInternalServerError`](./src/models/errors/search-tiktok-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchUsernameInternalServerError`](./src/models/errors/search-username-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchIpInfoInternalServerError`](./src/models/errors/search-ip-info-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchDnsInternalServerError`](./src/models/errors/search-dns-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchShodanInternalServerError`](./src/models/errors/search-shodan-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchWhoisInternalServerError`](./src/models/errors/search-whois-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`ScanPortsInternalServerError`](./src/models/errors/scan-ports-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`SearchCertificatesInternalServerError`](./src/models/errors/search-certificates-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`LookupDiscordAltInternalServerError`](./src/models/errors/lookup-discord-alt-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
* [`BypassDoubleCounterInternalServerError`](./src/models/errors/bypass-double-counter-internal-server-error.ts): Bypass failed. Status code `500`. Applicable to 1 of 35 methods.*
* [`DownloadIntelxFileInternalServerError`](./src/models/errors/download-intelx-file-internal-server-error.ts): Internal Server Error. Status code `500`. Applicable to 1 of 35 methods.*
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
  const result = await indicia.users.getInfo();

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
