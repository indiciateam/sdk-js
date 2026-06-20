<!-- Start SDK Example Usage [usage] -->
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