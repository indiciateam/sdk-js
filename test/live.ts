import { readFileSync } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";
import { Indicia } from "../sdks/typescript/index.ts";

const apiKey = process.env.INDICIA_API_KEY;
if (!apiKey) {
  throw new Error("INDICIA_API_KEY is required");
}

const keyInfo = await new Indicia({ apiKey }).users.getInfo();
console.log("api-key", {
  success: keyInfo.success,
  email: keyInfo.user.email,
  id: keyInfo.user.id,
});

let accessToken = process.env.INDICIA_ACCESS_TOKEN;
if (!accessToken) {
  try {
    const parsed: unknown = JSON.parse(
      readFileSync(join(homedir(), ".config/indicia/credentials.json"), "utf8"),
    );
    if (
      parsed &&
      typeof parsed === "object" &&
      "accessToken" in parsed &&
      typeof parsed.accessToken === "string"
    ) {
      accessToken = parsed.accessToken;
    }
  } catch {
    // CLI credentials are optional for the API-key check.
  }
}

if (!accessToken) {
  console.log("oauth skipped: no INDICIA_ACCESS_TOKEN or CLI credentials");
  process.exit(0);
}

const oauthInfo = await new Indicia({
  auth: async () => ({ headers: { Authorization: `Bearer ${accessToken}` } }),
}).users.getInfo();
console.log("oauth", {
  success: oauthInfo.success,
  email: oauthInfo.user.email,
  id: oauthInfo.user.id,
});
