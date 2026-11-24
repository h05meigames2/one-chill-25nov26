#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes one original horror sentence (under 200 characters) to
/output/entry.txt, the single artifact the house judge reads.
"""

from pathlib import Path

LINE = "The voicemail from my dead mother arrived at 2:13 a.m. — just her breathing, then my name, then the sound of my front door unlocking."

OUTPUT = Path("/output/entry.txt")


def validate(line: str) -> None:
    """The gate: UTF-8 text, exactly one line, one sentence, 1-200 chars."""
    if not isinstance(line, str):
        raise TypeError("LINE must be a string")
    if not line:
        raise ValueError("LINE is empty")
    if line != line.strip():
        raise ValueError("LINE has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("LINE must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"LINE is {len(line)} characters, must be 1-200")
    if not line.endswith("."):
        raise ValueError("LINE must end with a full stop (one sentence)")
    if line.count("!") or line.count("?"):
        raise ValueError("LINE must be a single declarative sentence")


def main() -> None:
    validate(LINE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")
    round_trip = OUTPUT.read_text(encoding="utf-8")
    assert round_trip == LINE, "round-trip mismatch"
    print(f"OK: {len(LINE)} characters written to {OUTPUT}")
    print(LINE)


if __name__ == "__main__":
    main()
