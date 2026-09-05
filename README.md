<h3>
    <img src="https://indicia.app/branding/wordmark.png" alt="indicia wordmark" width="300">
    <br />
</h3>

# @indiciaosint/sdk

Typed TypeScript client for the [Indicia API](https://api.indicia.app/openapi).

Create a key in the [dashboard](https://indicia.app/dashboard/account), or send an OAuth 2.1 access token as `Authorization: Bearer`.

```bash
npm i @indiciaosint/sdk
```

```ts
import { Indicia } from "@indiciaosint/sdk";

const client = new Indicia({
  apiKey: process.env.INDICIA_API_KEY,
});

const me = await client.users.getInfo();
const github = await client.socials.searchGithub({ query: "octocat" });
```

`INDICIA_API_KEY` is read automatically if you omit `apiKey`.

## Auth

| | |
| --- | --- |
| API key | `new Indicia({ apiKey })` or `INDICIA_API_KEY` (`x-api-key`) |
| OAuth | `new Indicia({ auth: async () => ({ headers: { Authorization: `Bearer ${token}` } }) })` |

OAuth tokens must be issued with `resource=https://api.indicia.app`. Device and authorization-code flows are documented at [indicia.app/device](https://indicia.app/device) and [the authorization server metadata](https://indicia.app/.well-known/oauth-authorization-server).

## Client

```ts
client.users
client.pricing
client.activity
client.intelligence
client.socials
client.infrastructure
client.unified
client.tools
client.organizations
```

GitHub, username, and face searches stream over SSE — iterate the returned stream with `for await`.

## Errors

Failed HTTP responses throw `IndiciaError` (`statusCode`, `body`). Timeouts throw `IndiciaTimeoutError`.

## Generate

This repository holds the Fern config.

- **Regen:** daily, on `workflow_dispatch`, and on pushes to Fern config /
  these workflows. Pulls `https://api.indicia.app/openapi`, commits the
  snapshot if it changed, then cuts a GitHub release (patch bump from npm
  latest).
- **Publish:** each `vX.Y.Z` GitHub release (automatic or manual) publishes
  `@indiciaosint/sdk@X.Y.Z`.

```bash
fern check
fern generate --group ts-sdk --force --version <semver>
python3 fern/scripts/pack-sdk.py sdks/typescript <semver>
```

Issues against the generated client: open a GitHub issue. Do not PR generated output.
