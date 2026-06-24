# Pricing

## Overview

### Available Operations

* [getPricing](#getpricing) - Gives credit pricing for all Indicia services

## getPricing

Gives credit pricing for all Indicia services

### Example Usage

<!-- UsageSnippet language="typescript" operationID="getPricing" method="get" path="/v1/pricing" -->
```typescript
import { Indicia } from "@indiciaosint/sdk";

const indicia = new Indicia({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const result = await indicia.pricing.getPricing();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { IndiciaCore } from "@indiciaosint/sdk/core.js";
import { pricingGetPricing } from "@indiciaosint/sdk/funcs/pricing-get-pricing.js";

// Use `IndiciaCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const indicia = new IndiciaCore({
  apiKey: process.env["INDICIA_API_KEY"] ?? "",
});

async function run() {
  const res = await pricingGetPricing(indicia);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("pricingGetPricing failed:", res.error);
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

**Promise\<[operations.GetPricingResponse](../../models/operations/get-pricing-response.md)\>**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.IndiciaDefaultError | 4XX, 5XX                   | \*/\*                      |