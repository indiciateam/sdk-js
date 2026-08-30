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

const accessToken = process.env.INDICIA_ACCESS_TOKEN;
if (!accessToken) {
  console.log("oauth skipped: set INDICIA_ACCESS_TOKEN");
  process.exit(0);
}

try {
  const oauthInfo = await new Indicia({
    auth: async () => ({ headers: { Authorization: `Bearer ${accessToken}` } }),
  }).users.getInfo();
  console.log("oauth", {
    success: oauthInfo.success,
    email: oauthInfo.user.email,
    id: oauthInfo.user.id,
  });
} catch (error) {
  const body =
    error && typeof error === "object" && "body" in error ? error.body : undefined;
  const statusCode =
    error && typeof error === "object" && "statusCode" in error
      ? error.statusCode
      : undefined;
  console.log("oauth failed", { statusCode, body });
  process.exit(1);
}
