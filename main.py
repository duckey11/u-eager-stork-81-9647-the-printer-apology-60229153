#!/usr/bin/env python3
"""The Printer Apology — make.fun bounty entry.

Writes one funny one-line apology from an office printer to /output/entry.txt.
The line is a fixed, hand-written string: no randomness, no network, no input,
so every run produces byte-identical output.
"""

import os

ENTRY = "Sorry I printed your breakup text to the whole office. In colour. Twice."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
