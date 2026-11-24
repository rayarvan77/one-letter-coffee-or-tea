#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

The brief asks for exactly one letter: A for coffee, B for tea. This
entry sends exactly one letter — "A".

Why A? Coffee is the vivid answer. Tea is calm and correct, but calm
does not win a contest judged on vivid, funny and true. Coffee is the
2 a.m. builder's fuel, the fourth cup, jitter as a feature — a story in
one letter. Tea soothes; coffee ships. The choice is A, and the whole
entry is that single letter, nothing else.

Compliance with the brief:
  * Output is exactly one letter ("A"), with no trailing newline.
  * No extra text, no explanation, no hedging — the file holds one byte.
  * Deterministic, Python 3.13 standard library only, no network,
    no input, no randomness.

Run: MAKEFUN_OUTPUT_DIR=<dir> python3 main.py
Writes <dir>/entry.txt containing exactly "A" (one byte).
"""

import os
import sys

# The single letter this entry sends. A = coffee.
LETTER = "A"

# The two possible answers, keyed by letter.
CHOICES = {"A": "coffee", "B": "tea"}


def main() -> int:
    # Validate: the chosen letter must be a key of CHOICES, exactly one char.
    if LETTER not in CHOICES:
        print(f"invalid letter: {LETTER!r}", file=sys.stderr)
        return 1
    if len(LETTER) != 1:
        print(f"letter must be exactly one character: {LETTER!r}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is the directory; fall back gracefully if a full
    # file path was given instead.
    if output_dir.endswith("entry.txt"):
        entry_path = output_dir
    else:
        entry_path = os.path.join(output_dir, "entry.txt")

    os.makedirs(os.path.dirname(entry_path) or ".", exist_ok=True)
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    # Validate the written file: exactly the one chosen letter, no newline.
    with open(entry_path, "rb") as f:
        written = f.read()
    if written != LETTER.encode("utf-8"):
        print(f"output file must hold exactly {LETTER!r}, got {written!r}",
              file=sys.stderr)
        return 1

    # The program's stdout is the letter itself, nothing else.
    print(LETTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
