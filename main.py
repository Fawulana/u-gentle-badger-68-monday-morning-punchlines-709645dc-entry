#!/usr/bin/env python3
"""Monday Morning Punchlines — writes one joke to /output/entry.txt.

Stdlib only, deterministic, offline: the joke is a fixed string, so every
run produces byte-identical output.
"""

import os

JOKE = (
    "Monday, 9 a.m. standup. 'Any blockers?' 'Yes: the weekend ended.' "
    "'Action items?' 'Survive until Friday.' Same ticket as last week. "
    "It has never once been closed."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: the entry must be 1-200 characters of non-whitespace text.
    if not (1 <= len(JOKE) <= 200 and JOKE.strip()):
        raise ValueError("joke violates the 1-200 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
