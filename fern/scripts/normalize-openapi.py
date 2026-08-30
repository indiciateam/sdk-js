#!/usr/bin/env python3
"""Fern does not accept OpenAPI 3.2. Rewrite live spec into 3.1."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def convert(node: object) -> None:
    if isinstance(node, dict):
        if "itemSchema" in node and "schema" not in node:
            node["schema"] = node.pop("itemSchema")
        elif "itemSchema" in node:
            node.pop("itemSchema")
        for value in node.values():
            convert(value)
    elif isinstance(node, list):
        for value in node:
            convert(value)


def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "fern/openapi.json")
    data = json.loads(path.read_text())
    convert(data)
    data["openapi"] = "3.1.0"
    path.write_text(json.dumps(data, indent=2) + "\n")


if __name__ == "__main__":
    main()
