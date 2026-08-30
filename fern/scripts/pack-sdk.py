#!/usr/bin/env python3
"""Make Fern's core-only TypeScript output publishable."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"


def ensure_client_export(index: Path) -> None:
    if not (index.parent / "Client.ts").exists():
        return
    text = index.read_text()
    if 'from "./Client.js"' in text:
        return
    text = text.replace(
        'export * as Indicia from "./api/index.js";\n',
        'export { Indicia } from "./Client.js";\nexport * as IndiciaApi from "./api/index.js";\n',
        1,
    )
    if 'from "./Client.js"' not in text:
        text = 'export { Indicia } from "./Client.js";\n' + text
    index.write_text(text)


def main() -> None:
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "sdks/typescript")
    version = sys.argv[2] if len(sys.argv) > 2 else "2.0.0"
    if not out.is_dir():
        raise SystemExit(f"missing SDK output: {out}")

    ensure_client_export(out / "index.ts")
    snusbase = out / "api/resources/intelligence/types/SearchWebDatabasesResponse.ts"
    if snusbase.exists():
        snusbase.write_text(
            snusbase.read_text().replace("Data.Snusbase.Item[]", "Data.Snusbase.Value[]")
        )


    pkg_path = out / "package.json"
    pkg = json.loads((TEMPLATES / "package.json").read_text())
    pkg["version"] = version
    if pkg_path.exists():
        existing = json.loads(pkg_path.read_text())
        if existing.get("devDependencies") and existing.get("main"):
            existing["version"] = version
            if existing.get("name") in (None, "", "api", "sdk"):
                existing["name"] = "@indiciaosint/sdk"
            pkg = existing
    pkg_path.write_text(json.dumps(pkg, indent=2) + "\n")

    shutil.copyfile(TEMPLATES / "tsconfig.json", out / "tsconfig.json")

    version_ts = out / "version.ts"
    if version_ts.exists():
        version_ts.write_text(f'export const SDK_VERSION = "{version}";\n')


if __name__ == "__main__":
    main()
