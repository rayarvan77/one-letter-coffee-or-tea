#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

Writes exactly one letter to $MAKEFUN_OUTPUT_DIR/entry.txt:
  A = coffee
  B = tea

The choice is A. Coffee is the vivid answer: the 2 a.m. builder's fuel,
the fourth cup, jitter as a feature. Tea is calm and correct, but calm
does not win a contest judged on vivid, funny and true. Coffee does.

Deterministic, Python 3.13 standard library only, no network, no input.
"""

import os
import sys

# The single letter this entry sends. A = coffee.
LETTER = "A"

VALID_LETTERS = ("A", "B")


def main() -> int:
    # Validate: the output must be exactly one letter, A or B.
    if LETTER not in VALID_LETTERS:
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

    # The program's stdout is the letter itself, nothing else.
    print(LETTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
