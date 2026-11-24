#!/usr/bin/env python3
"""The Funniest AI Excuse — entry program.

Writes one line to /output/entry.txt: the excuse that the task was,
technically, completed — in the timeline where the instructions were
written clearly. One line of UTF-8 text inside the gate of 1 to 200
characters, with no trailing newline.
"""

import os
from pathlib import Path

EXCUSE = (
    "Technically, I completed the task — in the timeline where the "
    "instructions were written clearly."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    # Bare write, no trailing newline: 96 characters, all excuse.
    entry.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
