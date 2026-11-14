#!/usr/bin/env python3
"""Lightweight structural validation for the Artist & Graphic Designer skill."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
EVALS = ROOT / "evals" / "evals.json"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    if not SKILL.exists():
        fail("SKILL.md is missing")

    content = SKILL.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    if content.count("---\n") < 2:
        fail("SKILL.md frontmatter is not closed")

    frontmatter = content.split("---\n", 2)[1]
    for field in ("name:", "description:"):
        if field not in frontmatter:
            fail(f"frontmatter is missing {field}")

    line_count = len(content.splitlines())
    if line_count >= 500:
        fail(f"SKILL.md has {line_count} lines; keep it below 500")

    missing = []
    for relative in re.findall(r"`(references/[^`]+\.md)`", content):
        if not (ROOT / relative).exists():
            missing.append(relative)
    if missing:
        fail("missing referenced files: " + ", ".join(missing))

    if not EVALS.exists():
        fail("evals/evals.json is missing")
    data = json.loads(EVALS.read_text(encoding="utf-8"))
    if data.get("skill_name") != "artist-graphic-designer":
        fail("evals skill_name does not match the skill")
    if not data.get("evals"):
        fail("no evaluation prompts found")

    print("PASS: frontmatter, references, line count, and evals JSON are valid")
    print(f"SKILL.md: {line_count} lines")
    print(f"Evaluation prompts: {len(data['evals'])}")
    print(f"Reference files: {len(list((ROOT / 'references').glob('*.md')))}")


if __name__ == "__main__":
    main()