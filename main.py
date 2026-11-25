#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office joke, written to /output/entry.txt.

The bounty gate requires /output/entry.txt to hold UTF-8 text of 1-200
characters, not only whitespace. This program writes a single line about
office life: the office coffee is free because nobody would pay for a
drink that tastes like a deadline.
"""

import os
import sys

JOKE = "The office coffee is free because nobody would pay for a drink that tastes like a deadline."


def validate(text: str) -> str:
    """Return the entry text, or raise if it cannot pass the bounty gate."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or whitespace only")
    if len(stripped) > 200:
        raise ValueError(f"entry is {len(stripped)} characters, over the 200 limit")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    return stripped


def main() -> int:
    try:
        text = validate(JOKE)
    except ValueError as exc:
        print(f"entry invalid: {exc}", file=sys.stderr)
        return 1
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
