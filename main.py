"""Monday Morning Punchlines entry.

Writes a single original joke about Monday mornings to /output/entry.txt.
Deterministic, offline, stdlib-only: the joke is a fixed string, so every
run produces byte-identical output.
"""

import os

JOKE = "Monday morning: my alarm served my dreams an eviction notice. My bed hired a lawyer."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: the entry must be 1-200 characters of non-whitespace text.
    if not (1 <= len(JOKE) <= 200 and JOKE.strip()):
        raise ValueError("joke violates the 1-200 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
