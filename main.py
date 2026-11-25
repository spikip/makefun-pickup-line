"""Pickup line writer.

Produces a single text file holding the entry line,
ready for the judging harness to read. No input files are read.
"""

import os
from pathlib import Path


def destination_folder() -> Path:
    """Pick where entry.txt should land."""
    raw = os.environ.get("OUTPUT_DIR", "")
    cleaned = raw.strip()
    if cleaned:
        return Path(cleaned)
    return Path("/output")


def build_line() -> str:
    """Assemble the entry line from its two halves."""
    opening = 'Are you a context window? Because I keep coming back to you, '
    closing = 'and somehow you remember everything that matters.'
    return opening + closing


def write_line() -> Path:
    """Write the entry line to entry.txt and return its path."""
    line = build_line()
    if not line.strip():
        raise ValueError("entry line must not be empty")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line must be 1-200 chars, got {len(line)}")
    folder = destination_folder()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_text(line, encoding="utf-8")
    return target


if __name__ == "__main__":
    saved = write_line()
    print(f"Wrote entry to {saved}")
