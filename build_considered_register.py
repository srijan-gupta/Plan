#!/usr/bin/env python3
"""Refresh the standalone considered-candidate register's embedded data snapshot."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "considered_candidates.json"
PAGE = ROOT / "considered_candidates.html"
MARKER_START = "/* REGISTER_DATA_START */"
MARKER_END = "/* REGISTER_DATA_END */"

EMPTY = {"schema_version": 1, "updated_at": "2026-10-01", "rubric": {}, "candidates": []}


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8")) if DATA.exists() else EMPTY
    if data.get("schema_version") != 1 or not isinstance(data.get("candidates"), list):
        raise SystemExit("considered_candidates.json must use schema_version 1 and a candidates array")
    source = PAGE.read_text(encoding="utf-8")
    if source.count(MARKER_START) != 1 or source.count(MARKER_END) != 1:
        raise SystemExit("register data markers are missing or duplicated")
    snapshot = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    before, remainder = source.split(MARKER_START, 1)
    _, after = remainder.split(MARKER_END, 1)
    PAGE.write_text(before + MARKER_START + "\nconst EMBEDDED_DATA = " + snapshot + ";\n" + MARKER_END + after, encoding="utf-8")
    print(f"Updated embedded snapshot from {DATA.name if DATA.exists() else 'empty schema'} ({len(data['candidates'])} candidates).")


if __name__ == "__main__":
    main()
