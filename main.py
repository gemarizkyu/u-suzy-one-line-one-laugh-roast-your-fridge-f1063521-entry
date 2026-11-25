#!/usr/bin/env python3
"""Roast Your Fridge — one-line roast writer.

Writes a single roast line (1-200 characters, one line, UTF-8) to
/output/entry.txt, where the make.fun program/v1 harness reads it.

Deterministic by design: no network, no randomness, no clock, no model
calls and no secrets. The line is fixed in this file, so every run of
the program produces exactly the same artifact.
"""

from __future__ import annotations

from pathlib import Path

ROAST = (
    "My fridge hums all night like it's rehearsing for a choir audition, "
    "keeps a mystery container from 2019 as a pet, "
    "and still lets the milk die first."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> str:
    """Hold the line to the gate: 1-200 UTF-8 characters, one line."""
    text = text.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"roast must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    return text


def main() -> None:
    text = validate(ROAST)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {OUTPUT_PATH} ({len(text)} characters)")


if __name__ == "__main__":
    main()
