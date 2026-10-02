from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED_TOP_LEVEL = {
    "id",
    "status",
    "intent",
    "thesis",
    "context",
    "evidence",
    "tokens",
    "formats",
    "constraints",
    "human_decisions",
}


def extract_yaml_block(text: str) -> str:
    match = re.search(r"```yaml\s*\n(.*?)\n```", text, re.DOTALL)
    if not match:
        raise ValueError("editorial packet must contain a fenced yaml block")
    return match.group(1)


def top_level_keys(yaml_text: str) -> set[str]:
    keys: set[str] = set()
    for line in yaml_text.splitlines():
        if not line or line[0].isspace() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", line)
        if match:
            keys.add(match.group(1))
    return keys


def scalar_value(yaml_text: str, key: str) -> str | None:
    pattern = re.compile(rf"^\s+{re.escape(key)}:\s*(.*?)\s*$", re.MULTILINE)
    match = pattern.search(yaml_text)
    return match.group(1) if match else None


def validate_packet_text(text: str, stage: str = "draft") -> list[str]:
    errors: list[str] = []
    try:
        yaml_text = extract_yaml_block(text)
    except ValueError as exc:
        return [str(exc)]

    missing = sorted(REQUIRED_TOP_LEVEL - top_level_keys(yaml_text))
    if missing:
        errors.append("missing top-level fields: " + ", ".join(missing))

    if stage == "ready":
        thesis = scalar_value(yaml_text, "approved_thesis")
        question = scalar_value(yaml_text, "open_question")
        if thesis in (None, "null", "") and question in (None, "null", ""):
            errors.append("ready packet requires approved_thesis or open_question")

        pending = scalar_value(yaml_text, "pending")
        if pending not in ("[]", None):
            errors.append("ready packet cannot contain pending human decisions")

        approved_by = scalar_value(yaml_text, "approved_by")
        approved_at = scalar_value(yaml_text, "approved_at")
        if approved_by in (None, "null", "") or approved_at in (None, "null", ""):
            errors.append("ready packet requires approved_by and approved_at")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Cereja Editorial Packet contract.")
    parser.add_argument("packet", type=Path)
    parser.add_argument("--stage", choices=("draft", "ready"), default="draft")
    args = parser.parse_args()

    errors = validate_packet_text(args.packet.read_text(encoding="utf-8"), args.stage)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: editorial packet contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
